# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif
%global pyver_bin python%{pyver}
%global pyver_sitelib %python%{pyver}_sitelib
%global pyver_install %py%{pyver}_install
%global pyver_build %py%{pyver}_build
# End of macros for py2/py3 compatibility
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global package_name UcsSdk

Name:           python-%{package_name}
Version:        XXX
Release:        XXX
Summary:        Python SDK for Cisco UCS Manager

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/%{package_name}
Source0:        https://pypi.io/packages/source/U/UcsSdk/UcsSdk-%{upstream_version}.tar.gz

BuildArch:      noarch

%description
Python development kit for Cisco UCS

%package -n     python%{pyver}-%{package_name}
Summary:        Python SDK for Cisco UCS Manager
%{?python_provide:%python_provide python%{pyver}-%{package_name}}

BuildRequires:  python%{pyver}-devel
BuildRequires:  python%{pyver}-setuptools

%description -n     python%{pyver}-%{package_name}
Python development kit for Cisco UCS

%prep
%setup -q -n %{package_name}-%{upstream_version}

%build
%{pyver_build}

%install
%{pyver_install}

%files -n     python%{pyver}-%{package_name}
%{pyver_sitelib}/%{package_name}/
%{pyver_sitelib}/%{package_name}*.egg-info
%doc README.md
%license LICENSE.txt

%changelog
