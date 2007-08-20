%define name	dd_rescue
%define version 1.12
%define release %mkrel 1

%define _bindir /bin

Summary:	Does copy data from one file or block device to another
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		System/Kernel and hardware
Source0:	http://www.garloff.de/kurt/linux/ddrescue/%name-%version.tar.bz2
URL:		http://www.garloff.de/kurt/linux/ddrescue/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires(post): info-install
Requires(postun): info-install
    
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
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755) 
%doc README.dd_rescue
%{_bindir}/*


