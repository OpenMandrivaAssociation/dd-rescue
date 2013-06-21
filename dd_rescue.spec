%bcond_without	uclibc

Summary:	Does copy data from one file or block device to another
Name:		dd_rescue
Version:	1.33
Release:	1
License:	GPL
Group:		System/Kernel and hardware
Source0:	http://www.garloff.de/kurt/linux/ddrescue/%{name}-%{version}.tar.gz
URL:		http://www.garloff.de/kurt/linux/ddrescue/
%if %{with uclibc}
BuildRequires:	uClibc-devel
%endif
 
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

%package -n	uclibc-%{name}
Summary:	Does copy data from one file or block device to another (uClibc build)
Group:		System/Kernel and hardware

%description -n	uclibc-%{name}
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
%setup -q -n %{name}

%build
%if %{with uclibc}
mkdir -p .uclibc
cp -a * .uclibc
pushd .uclibc
%make CC="%{uclibc_cc}" CFLAGS_OPT="%{uclibc_cflags}"
popd
%endif

mkdir -p .glibc
cp -a * .glibc
pushd .glibc
%make CFLAGS="%{optflags} -Ofast"
popd

%install
%if %{with uclibc}
install -m755 .uclibc/dd_rescue -D %{buildroot}%{uclibc_root}/bin/dd_rescue
%endif

%makeinstall_std INSTALLFLAGS="" INSTASROOT="" -C .glibc

%files
%doc README.dd_rescue
/bin/*

%if %{with uclibc}
%files -n uclibc-%{name}
%{uclibc_root}/bin/dd_rescue
%endif
