Name:    dapper-oz-profiles
Version: 1
Release: 2
Summary: Dapper Linux OZ Sandboxing Profiles
URL:     https://github.com/dapperlinux/dapper-oz-profiles
License: GPLv3+
BuildArch: noarch
Source0: %{name}-%{version}.tar.gz

%description
Dapper Oz Profiles are used by the oz sandboxing framework and dictate how sandboxes are constructed for
specific applications. 

%prep
%autosetup

%build

%install
mkdir -p %{buildroot}%{_sysconfdir}/oz
mkdir -p %{buildroot}%{_sharedstatedir}/oz/cells.d/
mkdir -p %{buildroot}%{_bindir}
cp profiles/generic-blacklist.seccomp %{buildroot}%{_sysconfdir}/oz/
cp profiles/* %{buildroot}%{_sharedstatedir}/oz/cells.d/
install -m 755 dapper-oz-install.sh %{buildroot}%{_bindir}
install -m 755 oz-install.sh %{buildroot}%{_bindir}


%files
%{_sysconfdir}/oz/generic-blacklist.seccomp
%{_sharedstatedir}/oz/cells.d/*
%{_bindir}/dapper-oz-install.sh
%{_bindir}/oz-install.sh

%changelog
* Wed Feb 15 2017 Matthew Ruffell <msr50@uclive.ac.nz>
- Added many more profiles and install scripts

* Fri Dec 16 2016 Matthew Ruffell <msr50@uclive.ac.nz>
- Initial profile packaging
