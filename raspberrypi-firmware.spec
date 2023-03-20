Summary:	Firmware for the Broadcom bcm283x/bcm2711 used in the Raspberry Pi
Name:		raspberrypi-firmware
Version:	1.20230317
Release:	1
Epoch:		1
# see LICENSE.broadcom
# DT Overlays covered under Linux Kernel GPLv2
License:	Redistributable, no modification permitted
Group:		Base/Kernel
Source0:	https://github.com/raspberrypi/firmware/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	e2523259a8e244741cf21d3ca31a1b62
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
%setup -q -n firmware-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/boot/firmware
cd boot
cp -pr *.{bin,dat,elf,dtb} overlays $RPM_BUILD_ROOT/boot/firmware

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc boot/LICENCE.broadcom boot/COPYING.linux
%dir /boot/firmware
/boot/firmware/*.dtb
/boot/firmware/fixup*.dat
/boot/firmware/start*.elf
/boot/firmware/bootcode.bin
/boot/firmware/overlays
