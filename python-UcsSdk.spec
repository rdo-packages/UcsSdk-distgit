%global package_name UcsSdk

Name:           python-%{package_name}
Version:        0.8.2.4
Release:        1%{?dist}
Summary:        Python SDK for Cisco UCS Manager

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/%{package_name}
Source0:        https://pypi.python.org/packages/source/U/UcsSdk/UcsSdk-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel

%description
Python development kit for Cisco UCS

%prep
%setup -q -n %{package_name}-%{version}

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
* Wed Jul 30 2015 Brian Demers <brdemers@cisco.com> 0.8.2.4-1
- Initial RPM release

