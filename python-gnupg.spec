Name:           python-gnupg
Version:        0.3.6
Release:        2%{?dist}
Summary:        Python module for GnuPG
Group:          Development/Languages
License:        BSD
URL:            http://pythonhosted.org/python-gnupg/
Source0:        https://pypi.python.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
Patch1:         python-gnupg-0.3.6-encoding.patch

BuildArch:      noarch
BuildRequires:  python2-devel
Requires:       gnupg

%description
GnuPG bindings for python. This uses the gpg command.

%prep
%setup -q
%patch1 -p1

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}

%files
%doc PKG-INFO LICENSE README
%{python_sitelib}/gnupg*.py*
%{python_sitelib}/python_gnupg-%{version}-py*.egg-info

%changelog
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
