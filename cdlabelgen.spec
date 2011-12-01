%define name cdlabelgen
%define version 4.1.0
%define release %mkrel 5

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
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%_mandir/man1

# [gb] they meant DATA_DIR
make install \
	BASE_DIR=%{buildroot}%{_prefix} \
	LIB_DIR=%{buildroot}%{_datadir}/%{name} \
	MAN_DIR=%{buildroot}%{_mandir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/%{name}/*
%_mandir/man1/*
%defattr(0644,root,root,755)
%doc ChangeLog INSTALL README
