Summary:	Program for generating inserts for CDs
Name:		cdlabelgen
Version:	4.3.0
Release:	1
License:	GPLv2+
Group:		Archiving/Cd burning
Url:		http://www.aczoom.com/tools/cdinsert/
Source0:	http://www.aczoom.com/pub/tools/%{name}-%{version}.tgz
Buildarch:	noarch

%description
cdlabelgen is a program for generating frontcards and traycards for CDs.
Use it to make labels for your archive CDs, CDs full of oggs, or
even make a label for that CD that you lost the case for! 
This package is used by the gcombust CD writing application.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_mandir}/man1

# [gb] they meant DATA_DIR
make install \
	BASE_DIR=%{buildroot}%{_prefix} \
	LIB_DIR=%{buildroot}%{_datadir}/%{name} \
	MAN_DIR=%{buildroot}%{_mandir}

%files
%{_bindir}/*
%{_datadir}/%{name}/*
%{_mandir}/man1/*
%doc ChangeLog INSTALL README
