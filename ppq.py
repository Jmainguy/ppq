#!/usr/bin/python
# Author: Jonathan Mainguy @jmainguy on github
# License: GPLv2

import argparse
import apt
import sys
import os

parser = argparse.ArgumentParser(description='A clone of the rpm command for debian, with less options, literally just -qa and -ql')

# Allow either or for arguments, do not allow qa and ql to be passed at the same time for example. Mutually Exclusive
group = parser.add_mutually_exclusive_group(required=True)

# Allow 0 or 1 arguments to be passed to -qa, also print 'Package' instead of QA in help
group.add_argument('-qa', help='List installed packages', type=str, metavar='Package', nargs='?')

group.add_argument('-ql', help='List files installed by package', type=str, metavar='Package')
args = parser.parse_args()

def querya(pkg_name):
  if pkg_name == 'all':
    deblist = []
    cache = apt.Cache()
    for pkg in cache:
      if pkg.candidate is not None and pkg.installed:
        packagename =  pkg.name + '-' + pkg.candidate.version + '.' + pkg.candidate.architecture
        deblist.append(packagename)

    for pkg in deblist:
      print pkg
  else:
    cache = apt.Cache()
    try:
      pkg = cache[pkg_name]
    except KeyError as k:
      print k
      sys.exit(1)

    if pkg.candidate is not None and pkg.installed:
      packagename =  pkg.name + '-' + pkg.candidate.version + '.' + pkg.candidate.architecture
      print packagename

def queryl(pkg_name):
  cache = apt.Cache()
  try:
    pkg = cache[pkg_name]
  except KeyError as k:
    print k
    sys.exit(1)

  for files in pkg.installed_files:
    # Only print files, not directories
    if os.path.isfile(files):
      print files
  sys.exit(0)

def main(args):
    qa = args.qa
    ql = args.ql
    arglist = list()

    if ql:
      queryl(ql)
    elif qa is None:
      qa = 'all'

    querya(qa)
main(args)
