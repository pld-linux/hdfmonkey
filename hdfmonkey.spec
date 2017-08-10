Summary:	A Swiss Army Knife for manipulating HDF disk images
Name:		hdfmonkey
Version:	0.4
Release:	1
License:	GPL v3+
Group:		Applications/System
Source0:	http://files.zxdemo.org/gasman/speccy/hdfmonkey/%{name}-%{version}.tar.gz
# Source0-md5:	77324a62834d050038a39309e2bbf687
URL:		http://github.com/gasman/hdfmonkey
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
hdfmonkey provides a suite of tools for working with FAT filesystems
contained in HDF disk images. HDF is the standard format used for
virtual hard disks in ZX Spectrum emulators such as Fuse
<http://fuse-emulator.sourceforge.net/>, so hdfmonkey allows these
disk images to be prepared without having to go through a physical
disk as an intermediate step - particularly useful when developing
software for FAT-supporting systems like ESXDOS and ResiDOS.

%prep
%setup -q

%build
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README
%attr(755,root,root) %{_bindir}/hdfmonkey
