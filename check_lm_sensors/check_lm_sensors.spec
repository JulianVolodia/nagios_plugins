%define version 3.1.0
%define release 0
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
Requires: perl-Nagios-Plugin

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
* Tue Jun 10 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 3.1.0-0
- repackaging and cleanup

* Thu Oct  4 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 3.0.1-0
- packaged version 3.0.1

* Wed Oct  3 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 3.0.0-2
- added the perl-Nagios-Plugin dependency

* Wed Oct  3 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 3.0.0-1
- included the updated ChangeLog and NEWS files

* Wed Oct  3 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 3.0.0-0
- Upgraded to 3.0.0

* Tue Jul 10 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 2.0-1
- updated to 2.0

* Wed Jun 20 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 1.1-4
- Requires perl and hddtemp

* Mon Jun 18 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 1.0-0
- Initial release
