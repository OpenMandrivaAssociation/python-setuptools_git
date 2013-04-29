%define module setuptools_git
Name:           python-%module
Version:        0.3
Release:        2
Summary:        Setuptools_git package
License:        BSD License
Group:          Development/Python
Source:         %module-%{version}.tar.gz
URL:            http://ygingras.net/b/tag/%module
BuildRequires:  python-devel
BuildRequires:	 python-setuptools
BuildArch:	noarch


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
%{__python} setup.py install --root %{buildroot} --install-purelib=%{python_sitelib}

%files
%{python_sitelib}/*

