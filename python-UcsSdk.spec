%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global package_name UcsSdk

Name:           python-%{package_name}
Version:        0.8.2.5
Release:        1%{?dist}
Summary:        Python SDK for Cisco UCS Manager

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/%{package_name}
Source0:        https://pypi.io/packages/source/U/UcsSdk/UcsSdk-%{upstream_version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-setuptools

%description
Python development kit for Cisco UCS

%prep
%setup -q -n %{package_name}-%{upstream_version}

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%files
%{python2_sitelib}/%{package_name}/
%{python2_sitelib}/%{package_name}*.egg-info
%doc README.md
%license LICENSE.txt

%changelog
* Wed Sep 14 2016 Haïkel Guémar <hguemar@fedoraproject.org> - 0.8.2.5-1
- Upstream 0.8.2.5

