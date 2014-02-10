%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define _bindir /bin

Summary:	Does copy data from one file or block device to another
Name:		dd_rescue
Version:	1.40
Release:	1
License:	GPL
Group:		System/Kernel and hardware
Source0:	http://www.garloff.de/kurt/linux/ddrescue/%{name}-%{version}.tar.gz
URL:		http://www.garloff.de/kurt/linux/ddrescue/
 
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
%setup -qn %{name}

%build

%make

%install
%makeinstall_std INSTASROOT=""

%clean

%files
%defattr(-,root,root,0755) 
%doc README.dd_rescue
%{_bindir}/*
%{_mandir}/man1/*
