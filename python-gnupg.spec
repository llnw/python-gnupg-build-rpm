%global __os_install_post %{__python26_os_install_post}
%global __python2 /usr/bin/python2.6

%{!?python_sitelib: %define python_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%global oname python-gnupg

Name:           python26-gnupg
Version:        0.3.7
Release:        2%{?dist}
Summary:        Python module for GnuPG
Group:          Development/Languages
License:        BSD
URL:            http://pythonhosted.org/python-gnupg/
Source0:        https://pypi.python.org/packages/source/p/%{oname}/%{oname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python26-devel
Requires:       gnupg
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
GnuPG bindings for python. This uses the gpg command.

%prep
%setup -q -n %{oname}-%{version}

%build
%{__python2} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc PKG-INFO LICENSE.txt README.rst
%{python_sitelib}/gnupg*.py*
%{python_sitelib}/python_gnupg-%{version}-py*.egg-info

%changelog
* Fri Jan 09 2015 Kevin Bowling <kbowling@llnw.com> - 0.3.7-2
- Package for EPEL5

* Tue Jan 06 2015 Paul Wouters <pwouters@redhat.com> - 0.3.7-1
- Updated to 0.3.7 Merged in export-minimal and armor options, many encoding fixes

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 17 2014 Paul Wouters <pwouters@redhat.com> - 0.3.6-3
- Removed patch as gpg.decode_errors=ignore works well

* Thu Apr 17 2014 Paul Wouters <pwouters@redhat.com> - 0.3.6-2
- Re-instate part of export patch that fixed encoding bug

* Thu Feb 06 2014 Paul Wouters <pwouters@redhat.com> - 0.3.6-1
- Updated to 0.3.6 which includes Security fix (CVE-2014-XXXX)
- Upstream including our export patch and converted README file
- Upstream switched to new download site

* Mon Jan 06 2014 Paul Wouters <pwouters@redhat.com> - 0.3.5-4
- Require gnupg (duh)
- Remove cleaning in install target
- Fix license to BSD
- Link to upstream bug tracker for included patch

* Sat Jan 04 2014 Paul Wouters <pwouters@redhat.com> - 0.3.5-3
- Remove unused global, fix python macro, buildroot macro
- Converted README from DOS to unix (and reported upstream)

* Tue Dec 31 2013 Paul Wouters <pwouters@redhat.com> - 0.3.5-2
- Added minimal= and armor= options to export_keys()

* Sun Dec 22 2013 Paul Wouters <pwouters@redhat.com> - 0.3.5-1
- Initial package
