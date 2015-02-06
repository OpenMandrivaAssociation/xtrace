Summary:	An strace like program for tracing X11 connections
Name:		xtrace
Version:	1.3.1
Release:	2
License:	BSD 
Group:		System/Kernel and hardware
URL:		https://alioth.debian.org/projects/xtrace/
Source0:	http://ftp.de.debian.org/debian/pool/main/x/xtrace/%{name}_%{version}.orig.tar.gz

%description
What strace is for system calls, xtrace is for X11 connections:
you hook it between one or more X11 clients and an X server and
it prints the requests going from client to server and the replies,
events and errors going the other way.


%prep
%setup -q
%configure

%build
CFLAGS="%{optflags} -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE"
%make

%install
%makeinstall_std
mv %{buildroot}/%_bindir/xtrace %buildroot/%_bindir/xtrace-x11
mv %{buildroot}/%_mandir/man1/xtrace.1 %buildroot/%_mandir/man1/xtrace-x11.1
mv %{buildroot}/%_datadir/%{name} %buildroot/%_datadir/%{name}-x11/

%files
%doc README NEWS
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/%{name}-x11/*.proto
