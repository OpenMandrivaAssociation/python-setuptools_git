%define module setuptools_git
Name:           python-%module
Version:        0.3
Release:        %mkrel 1
Summary:        Setuptools_git package
License:        BSD License
Group:          Development/Python
Source:         %module-%{version}.tar.gz
URL:            http://ygingras.net/b/tag/%modules
BuildRequires:  python-devel
Buildrequires:	 python-setuptools
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
buildarch:	noarch


%description
This is a plugin for setuptools that enables git integration. Once
installed, Setuptools can be told to include in a package distribution
all the files tracked by git. This is an alternative to explicit
inclusion specifications with `MANIFEST.in`.

%prep
%setup -q -n %{module}-%{version}

%build
CFLAGS="%{optflags}" python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --root $RPM_BUILD_ROOT --install-purelib=%{python_sitelib}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{python_sitelib}/*

