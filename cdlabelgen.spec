%define name cdlabelgen
%define version 4.1.0
%define release %mkrel 7

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


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 4.1.0-5mdv2011.0
+ Revision: 663359
- mass rebuild

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 4.1.0-4mdv2011.0
+ Revision: 603819
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 4.1.0-3mdv2010.1
+ Revision: 522338
- rebuilt for 2010.1

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 4.1.0-2mdv2010.0
+ Revision: 413223
- rebuild

* Sun Mar 22 2009 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 4.1.0-1mdv2009.1
+ Revision: 360104
- Updated to version 4.1.0

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 4.0.0-3mdv2009.1
+ Revision: 350220
- 2009.1 rebuild

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 4.0.0-2mdv2009.0
+ Revision: 264344
- rebuild early 2009.0 package (before pixel changes)

* Fri May 02 2008 Funda Wang <fwang@mandriva.org> 4.0.0-1mdv2009.0
+ Revision: 200004
- New version 4.0.0

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Jun 19 2007 Adam Williamson <awilliamson@mandriva.org> 3.6.0-3mdv2008.0
+ Revision: 41189
- minor description cleanup; rebuild for 2008
- Import cdlabelgen



* Wed Aug 02 2006 Lenny Cartier <lenny@mandriva.com> 3.6.0-2mdv2007.0
- rebuild

* Wed Oct 26 2005 Lenny Cartier <lenny@mandriva.com> 3.6.0-1mdk
- 3.6.0

* Mon Jun 27 2005 Götz Waschk <waschk@mandriva.org> 3.5.0-1mdk
- drop prefix
- New release 3.5.0

* Fri Dec 17 2004 Lenny Cartier <lenny@mandrakesoft.com> 3.0.0-2mdk
- rebuild

* Mon Nov 17 2003 Lenny Cartier <lenny@mandrakesoft.com> 3.0.0-1mdk
- 3.0.0

* Thu Sep 18 2003 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 2.6.1-2mdk
- fix build on lib64 platforms

* Mon Aug 18 2003 Lenny Cartier <lenny@mandrakesoft.com> 2.6.1-1mdk
- 2.6.1

* Wed Jun 04 2003 Lenny Cartier <lenny@mandrakesoft.com> 2.6.0-1mdk
- 2.6.0

* Thu Nov 07 2002 Lenny Cartier <lenny@mandrakesoft.com> 2.5.0-1mdk
- 2.5.0
- move manpage

* Mon Oct 21 2002 Lenny Cartier <lenny@mandrakesoft.com> 2.4.0-1mdk
- 2.4.0

* Mon May 27 2002 Lenny Cartier <lenny@mandrakesoft.com> 2.3.0-1mdk
- 2.3.0
- new url
- maintain templates files in /usr/share despite what makefiles does

* Sat Jul 28 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.5.0-3mdk
- url

* Fri Jan 05 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.5.0-2mdk
- rebuild

* Mon Oct  2 2000 Renaud Chaillat <rchaillat@mandrakesoft.com> 1.5.0-1mdk
- First spec file for Mandrake distribution.
- Override BASE_DIR in make install

# end of file
