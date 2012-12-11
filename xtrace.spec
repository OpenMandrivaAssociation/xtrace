Summary:	An strace like program for tracing X11 connections
Name:		xtrace
Version:	1.2.0
Release:	%mkrel 3
License:	BSD 
Group:		System/Kernel and hardware
URL:		https://alioth.debian.org/projects/xtrace/
Source0:	http://ftp.de.debian.org/debian/pool/main/x/xtrace/%{name}_%{version}.orig.tar.gz
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot
#Conflicts:	glibc-utils

%description
What strace is for system calls, xtrace is for X11 connections:
you hook it between one or more X11 clients and an X server and
it prints the requests going from client to server and the replies,
events and errors going the other way.


%prep
%setup -q
%configure2_5x

%build
CFLAGS="%{optflags} -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE"
%make

%install
rm -rf %{buildroot}
#mkdir -p $RPM_BUILD_ROOT/ % _bindir
#install -m 755 mbootpack $RPM_BUILD_ROOT/ % _bindir/
%makeinstall_std
mv %{buildroot}/%_bindir/xtrace %buildroot/%_bindir/xtrace-x11
mv %{buildroot}/%_mandir/man1/xtrace.1 %buildroot/%_mandir/man1/xtrace-x11.1
mv %{buildroot}/%_datadir/%{name} %buildroot/%_datadir/%{name}-x11/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README NEWS
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/%{name}-x11/*.proto


%changelog
* Tue Sep 20 2011 Alexander Barakin <abarakin@mandriva.org> 1.2.0-3mdv2012.0
+ Revision: 700554
- man dir fix

* Tue Sep 20 2011 Alexander Barakin <abarakin@mandriva.org> 1.2.0-2
+ Revision: 700549
- resolve dupe names

* Wed Mar 16 2011 Stéphane Téletchéa <steletch@mandriva.org> 1.2.0-1
+ Revision: 645492
- update to new version 1.2.0

* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-2mdv2011.0
+ Revision: 615746
- the mass rebuild of 2010.1 packages

* Thu Feb 11 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.0.2-1mdv2010.1
+ Revision: 504307
- update to 1.0.2

* Sat Nov 07 2009 Frederik Himpe <fhimpe@mandriva.org> 1.0.1-1mdv2010.1
+ Revision: 462688
- Update to new version 1.0.1

* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 0.8.0-6mdv2010.0
+ Revision: 435321
- rebuild
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.8.0-4mdv2009.0
+ Revision: 257835
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Fri Nov 23 2007 Pixel <pixel@mandriva.com> 0.8.0-2mdv2008.1
+ Revision: 111654
- glibc-utils also provides /usr/bin/xtrace, explicit conflict is needed

* Wed Sep 05 2007 Thierry Vignaud <tv@mandriva.org> 0.8.0-1mdv2008.0
+ Revision: 80033
- new release


* Fri Nov 24 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.7.0-1mdv2007.0
+ Revision: 87136
- Import xtrace

* Fri Nov 24 2006 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.7.0-1mdv2007.1
- new release
- fix URL

* Sat Oct 14 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.6.0-1mdv2007.1
- initial release

