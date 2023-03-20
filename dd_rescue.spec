Summary:	Does copy data from one file or block device to another
Name:		dd_rescue
Version:	1.99.13
Release:	1
License:	GPL
Group:		System/Kernel and hardware
URL:		http://www.garloff.de/kurt/linux/ddrescue/
Source0:	https://downloads.sourceforge.net/ddrescue/%{name}-%{version}.tar.bz2
#Source0:	http://www.garloff.de/kurt/linux/ddrescue/%{name}-%{version}.tar.bz2
Patch0:		dd-rescue_use_default_compiler_adn_flags.patch

BuildRequires:	pkgconfig(lzo2)
BuildRequires:	pkgconfig(openssl)

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

%files
%doc README.dd_rescue
%{_bindir}/%{name}
%{_libdir}/libddr_*.so
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man1/ddr_*.1.*

#--------------------------------------------------------------------

%prep 
%autosetup -p1

%build
autoreconf -vif
%configure
%make_build RPM_OPT_FLAGS="%{optflags}" LIB=%{_lib}

%install
%make_install INSTASROOT="" INSTALLFLAGS="" LIB=%{_lib}

