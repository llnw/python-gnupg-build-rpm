LLNW python26-gnupg packaging for RPM
=====================================

The RPM spec is in the [el5 branch], compatible with python26 from [EPEL].

* Upstream:  http://pkgs.fedoraproject.org/cgit/python-gnupg.git/

Building the package with mock:
-------------------------------

mock builds the package in a chroot and avoids pitfalls of building on the build host.

* Enable [EPEL]
* `yum install mock`
* `ln --force -s /etc/mock/epel-5-x86_64.cfg /etc/mock/default.cfg`
* Fetch the [current version] and save it in `~/rpmbuild/SOURCES/`
* Build the SRPM:
  `mock -r epel-5-x86_64 --buildsrpm --spec ~/rpmbuild/SPECS/python-gnupg.spec --sources ~/rpmbuild/SOURCES/`
* Build the RPM:
  `mock -r epel-5-x86_64 --no-clean --rebuild /var/lib/mock/epel-5-x86_64/result/python26-gnupg-X.Y.Z-NN.src.rpm`
* The results will be in `/var/lib/mock/epel-5-x86_64/result/`
* Repeat as needed for other environments

Building the package native:
----------------------------

This is easier but will pollute your build environment with dependencies.

* Enable [EPEL]
* Fetch the [current version] and save it in `~/rpmbuild/SOURCES/`
* rpmbuild -bb collectd.spec
* The results will be in `~/rpmbuild/RPMS/x86_64/`

  [el5 branch]: https://github.com/llnw/python-gnupg-build-rpm/tree/el5
  [current version]: https://pypi.python.org/packages/source/p/python-gnupg/python-gnupg-0.3.7.tar.gz#md5=ce600421b8168bd7d9470d6b451594d5
  [EPEL]: http://dl.fedoraproject.org/pub/epel/

