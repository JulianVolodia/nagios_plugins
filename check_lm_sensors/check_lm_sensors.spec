%define version 2.0
%define release 2
%define name    check_lm_sensors
%define _prefix /usr/lib/nagios/plugins/contrib

Summary:   A Nagios plugin to monitor sensors values
Name:      %{name}
Version:   %{version}
Release:   %{release}
License:   GPL
Packager:  Matteo Corti <matteo.corti@id.ethz.ch>
Group:     Applications/System
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Source:    http://www.id.ethz.ch/people/allid_list/corti/%{name}-%{version}.tar.gz
BuildArch: noarch

Requires: hddtemp
Requires: perl

%description
check_lm_sensors is a Nagios plugin to monitor the values of on board sensors and hard
disk temperatures on Linux systems

%prep
%setup -q

%build

%install
make DESTDIR=$RPM_BUILD_ROOT%{_prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root, 0644)
%doc AUTHORS ChangeLog NEWS README INSTALL TODO COPYING VERSION
%attr(0755, root, root) %{_prefix}/check_lm_sensors

%changelog
* Tue Jul 10 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 2.0-1
- updated to 2.0

* Wed Jun 20 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 1.1-4
- Requires perl and hddtemp

* Mon Jun 18 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 1.0-0
- Initial release
