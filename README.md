# ppq
This is only useful for debian based systems.

Python Package Query (A apt clone of rpm -qa and -ql from rpm based systems)

Please note dpkg provides all the features below, and faster. However if you
enjoy the rpm -qa and -ql style output, you might like this.

```
usage: ppq [-h] (-qa [Package] | -ql Package)

A clone of the rpm command for debian, with less options, literally just -qa
and -ql

optional arguments:
  -h, --help     show this help message and exit
  -qa [Package]  List installed packages
  -ql Package    List files installed by package
```

## deb
To create and install a .deb of this script

```
apt-get install python-stdeb fakeroot python-all dh-python
python setup.py --command-packages=stdeb.command bdist_deb

```

Then dpkg -i the resulting .deb created

```
dpkg -i deb_dist/python-ppq_0.1-1_all.deb
```
