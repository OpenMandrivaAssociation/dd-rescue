Name:		dd-rescue
Version:	1.25
Release:	1
Summary:	Similar to dd but can copy from source with errors
Group:		System/Configuration/Hardware
License:	GPLv3
URL:		http://www.garloff.de/kurt/linux/ddrescue
Source0:	http://www.garloff.de/kurt/linux/ddrescue/dd_rescue-%{version}.tar.gz


%description
Imagine, one of your partitions is crashed, and as there are some hard errors, you don't want to write to this hard disk any more.
Just getting all the data off it and retiring it seems to be suitable. However, you can't access the files, as the file system is damaged.
Now, you want to copy the whole partition into a file. You burn it on CD-Rom, just to never lose it again. 
You can setup a loop device, and repair (fsck) it and hopefully are able to mount it.
Copying this partition with normal Un*x tools like cat or dd will fail, as those tools abort on error.
dd_rescue instead will try to read and if it fails, it will go on with the next sectors. 
The output file naturally will have holes in it, of course. You can write a log file, to see, where all these errors are located.
The data rate drops very low, when errors are encountered.
If you interrupt the process of copying, you don't lose anything. You can just continue at any position later. 
The output file will just be filled in further and not truncated as with other Un*x tools.
If you have one spot of bad sectors within the partition, it might be a good idea, to approach this spot from both sides.
Reverse direction copy is your friend.
The two block sizes are a performance optimization. Large block sizes result in superior performance, but in case of errors, you want to try to salvage every single sector.
So hardbs is best be set to the hardware sector size (most often 512 bytes) and softbs to a large value, such as the default 16k.


%prep
%setup -q -n dd_rescue

%build

%make

%install
mkdir -p %{buildroot}%{_bindir}
install -s -m 755 dd_rescue %{buildroot}/%{_bindir}/%{name}

%files
%{_bindir}/%{name}
