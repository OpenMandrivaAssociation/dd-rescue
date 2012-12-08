%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define name	dd_rescue
%define version 1.28
%define release %mkrel 1

%define _bindir /bin

Summary:	Does copy data from one file or block device to another
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		System/Kernel and hardware
Source0:	http://www.garloff.de/kurt/linux/ddrescue/%name-%version.tar.gz
URL:		http://www.garloff.de/kurt/linux/ddrescue/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
 
%description
Like dd, dd_rescue does copy data from one file or block device to another.
You can specify file positions (called seek and Skip in dd). There are several 
differences: 
  o dd_rescue does not provide character conversions.
  o The command syntax is different. Call dd_rescue -h.
  o dd_rescue does not abort on errors on the input file, unless you specify a 
    maximum error number. Then dd_rescue will abort when this number is reached
  o dd_rescue does not truncate the output file, unless asked to.
  o You can tell dd_rescue to start from the end of a file and move bcakwards.
  o It uses two block sizes, a large (soft) block size and a small (hard) block
    size. In case of errors, the size falls back to the small one and is
    promoted again after a while without errors.

%prep 
%setup -q -n %name

%build

%make CFLAGS="%{optflags}"

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std INSTASROOT=""

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755) 
%doc README.dd_rescue
%{_bindir}/*




%changelog
* Thu Aug 26 2010 Funda Wang <fwang@mandriva.org> 1.20-1mdv2011.0
+ Revision: 573402
- update to new version 1.20

* Sat Aug 21 2010 Funda Wang <fwang@mandriva.org> 1.18-1mdv2011.0
+ Revision: 571577
- update to new version 1.18

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 1.14-3mdv2010.0
+ Revision: 427956
- rebuild

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.14-2mdv2009.0
+ Revision: 266557
- rebuild early 2009.0 package (before pixel changes)

* Mon May 05 2008 Colin Guthrie <cguthrie@mandriva.org> 1.14-1mdv2009.0
+ Revision: 201512
- Update to 1.14

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.12-3mdv2008.1
+ Revision: 140721
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 23 2007 Thierry Vignaud <tv@mandriva.org> 1.12-3mdv2008.0
+ Revision: 69964
- fix build
- kill unused info-install require
- kill file require on info-install


* Tue Aug 08 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/08/06 00:32:21 (54347)
- 1.12

* Tue Aug 08 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/08/06 00:30:44 (54346)
Import dd_rescue

* Sun Oct 16 2005 Olivier Thauvin <nanardon@mandriva.org> 1.11-1mdk
- Initial spec file based on ddrescue

* Thu Oct 13 2005 Lenny Cartier <lenny@mandriva.com> 1.1-1mdk
- 1.1

* Sat Oct 01 2005 Olivier Thauvin <nanardon@mandriva.org> 1.0-2mdk
- from club, introduce in contrib
- clean + mdv policy

* Fri Jun 03 2005 Jose Ramon Villa <capi_x@capix.sytes.net> - 1.0-1mdk
- Created specfile for Mandriva

