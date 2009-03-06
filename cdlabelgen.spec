%define name cdlabelgen
%define version 4.0.0
%define release %mkrel 3

Summary: Program for generating inserts for CDs
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.aczoom.com/pub/tools/%name-%version.tgz
License: GPLv2+
Url: http://www.aczoom.com/tools/cdinsert/
Group: Archiving/Cd burning
BuildRoot: %{_tmppath}/%{name}-buildroot
Buildarch: noarch

%description
cdlabelgen is a program for generating frontcards and traycards for CDs.
Use it to make labels for your archive CDs, CDs full of oggs, or
even make a label for that CD that you lost the case for! 
This package is used by the gcombust CD writing application.

%prep

%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
mkdir -p $RPM_BUILD_ROOT%_mandir/man1

# [gb] they meant DATA_DIR
make install \
	BASE_DIR=$RPM_BUILD_ROOT%{_prefix} \
	LIB_DIR=$RPM_BUILD_ROOT%{_datadir}/%{name} \
	MAN_DIR=$RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/%{name}/*
%_mandir/man1/*
%defattr(0644,root,root,755)
%doc ChangeLog INSTALL README
