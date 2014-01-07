Name:           python-gnupg
Version:        0.3.5
Release:        4%{?dist}
Summary:        Python module for GnuPG
Group:          Development/Languages
License:        BSD
URL:            http://pythonhosted.org/python-gnupg/
Source0:        http://python-gnupg.googlecode.com/files/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python2-devel
Requires:       gnupg
# Patch required for raw (non-ascii) key exports - required for hash-slinger's use
# submitted to upstream: http://code.google.com/p/python-gnupg/issues/detail?id=94
Patch1:         python-gnupg-0.3.5-export.patch

%description
GnuPG bindings for python. This uses the gpg command.

%prep
%setup -q
%patch1 -p1

%build
%{__python2} setup.py build
mv README README.org
tr -d '\r' < README.org > README

%install
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}

%files
%doc PKG-INFO LICENSE README
%{python_sitelib}/gnupg*.py*
%{python_sitelib}/python_gnupg-%{version}-py*.egg-info

%changelog
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
