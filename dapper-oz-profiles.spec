Name:    dapper-oz-profiles
Version: 1
Release: 12
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
install -m 755 dapper-oz-install %{buildroot}%{_bindir}
install -m 755 dapper-oz-uninstall %{buildroot}%{_bindir}

%posttrans
dapper-oz-install

%preun
dapper-oz-uninstall

%files
%{_sysconfdir}/oz/generic-blacklist.seccomp
%{_sharedstatedir}/oz/cells.d/*
%{_bindir}/dapper-oz-install
%{_bindir}/dapper-oz-uninstall

%changelog
* Wed Feb 22 2017 Matthew Ruffell <msr50@uclive.ac.nz>
- Added gedit and pdfshuffler. Fixed dbus autostart problems. Removed blacklists for mozilla products.

* Wed Feb 15 2017 Matthew Ruffell <msr50@uclive.ac.nz>
- Added many more profiles and install scripts

* Fri Dec 16 2016 Matthew Ruffell <msr50@uclive.ac.nz>
- Initial profile packaging
