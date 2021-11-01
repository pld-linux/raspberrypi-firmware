Summary:	Firmware for the Broadcom bcm283x/bcm2711 used in the Raspberry Pi
Name:		raspberrypi-firmware
Version:	20210405
Release:	1
# see LICENSE.broadcom
# DT Overlays covered under Linux Kernel GPLv2
License:	Redistributable, no modification permitted
Group:		Base/Kernel
# git clone https://github.com/raspberrypi/firmware.git
# cd firmware/boot
# tar cJf ../raspberrypi-firmware-%{version}.tar.xz *bin *dat *elf bcm*dtb LICENCE.broadcom COPYING.linux overlays/
Source0:	%{name}-%{version}.tar.xz
# Source0-md5:	4dd61c53af0f6e8d361f7a454001ee29
URL:		https://github.com/raspberrypi/firmware/
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
ExclusiveArch:	%{arm} aarch64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		no_install_post_strip	1

%description
Firmware for the Broadcom bcm283x and bcm2711 series of systems on a
chip as shipped in the Raspberry Pi series of devices.

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/boot/firmware
cp -pr *.{bin,dat,elf,dtb} overlays $RPM_BUILD_ROOT/boot/firmware

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENCE.broadcom COPYING.linux
%dir /boot/firmware
/boot/firmware/*.dtb
/boot/firmware/fixup*.dat
/boot/firmware/start*.elf
/boot/firmware/bootcode.bin
/boot/firmware/overlays
