Summary:	An strace like program for tracing X11 connections
Name:		xtrace
Version:	0.8.0
Release:	%mkrel 1
License:	BSD 
Group:		System/Kernel and hardware
URL:		http://packages.debian.org/xtrace
Source:		ftp.debian.org/debian/pool/main/x/xtrace/%{name}-%{version}.tar.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

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
#mkdir -p $RPM_BUILD_ROOT/%_bindir
#install -m 755 mbootpack $RPM_BUILD_ROOT/%_bindir/
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README NEWS
%{_bindir}/*
%{_mandir}/man1/*


