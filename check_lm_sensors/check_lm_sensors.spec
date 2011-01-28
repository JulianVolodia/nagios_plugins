################################################################################
# File version information:
# $Id: check_updates.spec 1208 2010-11-18 10:45:55Z corti $
# $Revision: 1208 $
# $HeadURL: https://svn.id.ethz.ch/nagios_plugins/check_updates/check_updates.spec $
# $Date: 2010-11-18 11:45:55 +0100 (Thu, 18 Nov 2010) $
################################################################################

%define version          4.0.0
%define release          0
%define sourcename       check_lm_sensors
%define packagename      nagios-plugins-check-lm-sensors
%define nagiospluginsdir %{_libdir}/nagios/plugins

# No binaries in this package
%define debug_package    %{nil}

Summary:       A Nagios plugin to monitor sensors values
Name:          %{packagename}
Version:       %{version}
Obsoletes:     check_lm_sensors
Release:       %{release}%{?dist}
License:       GPLv3+
Packager:      Matteo Corti <matteo.corti@id.ethz.ch>
Group:         Applications/System
BuildRoot:     %{_tmppath}/%{packagename}-%{version}-%{release}-root-%(%{__id_u} -n)
Source:        http://www.id.ethz.ch/people/allid_list/corti/%{sourcename}-%{version}.tar.gz

Requires: hddtemp

# Fedora build requirement (not needed for EPEL{4,5})
BuildRequires: perl(ExtUtils::MakeMaker)

Requires:      nagios-plugins

%description
check_lm_sensors is a Nagios plugin to monitor the values of on board sensors and hard
disk temperatures on Linux systems

%prep
%setup -q -n %{sourcename}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor \
    INSTALLSCRIPT=%{nagiospluginsdir} \
    INSTALLVENDORSCRIPT=%{nagiospluginsdir}
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name "*.pod" -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} %{buildroot}/*

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS Changes NEWS README TODO COPYING COPYRIGHT
%{nagiospluginsdir}/%{sourcename}
%{_mandir}/man1/%{sourcename}.1*

%changelog
* Fri Oct 17 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 3.1.1-0
- short pause before reading the output of 'sensors'

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
