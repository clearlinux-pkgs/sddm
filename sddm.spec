#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sddm
Version  : 0.18.0
Release  : 5
URL      : https://github.com/sddm/sddm/releases/download/v0.18.0/sddm-0.18.0.tar.gz
Source0  : https://github.com/sddm/sddm/releases/download/v0.18.0/sddm-0.18.0.tar.gz
Source1  : sddm.tmpfiles
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 CC-BY-3.0 CC-BY-SA-3.0 GPL-2.0
Requires: sddm-bin = %{version}-%{release}
Requires: sddm-config = %{version}-%{release}
Requires: sddm-data = %{version}-%{release}
Requires: sddm-lib = %{version}-%{release}
Requires: sddm-libexec = %{version}-%{release}
Requires: sddm-license = %{version}-%{release}
Requires: sddm-services = %{version}-%{release}
BuildRequires : Linux-PAM-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules pkgconfig(xcb) xcb-util-cursor-dev xcb-util-image-dev xcb-util-keysyms-dev xcb-util-renderutil-dev xcb-util-wm-dev xcb-util-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(systemd)
BuildRequires : pkgconfig(xcb)
BuildRequires : pkgconfig(xcb-xkb)
BuildRequires : qtbase-dev mesa-dev
Patch1: 0001-Install-the-PAM-config-files-where-Clear-expects-the.patch
Patch2: 0002-sddm.pam-Update-system-login-to-login.patch

%description
This theme is part of the Simple Desktop Display Manager distribution. This theme is based QtQuick2.

%package autostart
Summary: autostart components for the sddm package.
Group: Default

%description autostart
autostart components for the sddm package.


%package bin
Summary: bin components for the sddm package.
Group: Binaries
Requires: sddm-data = %{version}-%{release}
Requires: sddm-libexec = %{version}-%{release}
Requires: sddm-config = %{version}-%{release}
Requires: sddm-license = %{version}-%{release}
Requires: sddm-services = %{version}-%{release}

%description bin
bin components for the sddm package.


%package config
Summary: config components for the sddm package.
Group: Default

%description config
config components for the sddm package.


%package data
Summary: data components for the sddm package.
Group: Data

%description data
data components for the sddm package.


%package lib
Summary: lib components for the sddm package.
Group: Libraries
Requires: sddm-data = %{version}-%{release}
Requires: sddm-libexec = %{version}-%{release}
Requires: sddm-license = %{version}-%{release}

%description lib
lib components for the sddm package.


%package libexec
Summary: libexec components for the sddm package.
Group: Default
Requires: sddm-config = %{version}-%{release}
Requires: sddm-license = %{version}-%{release}

%description libexec
libexec components for the sddm package.


%package license
Summary: license components for the sddm package.
Group: Default

%description license
license components for the sddm package.


%package services
Summary: services components for the sddm package.
Group: Systemd services

%description services
services components for the sddm package.


%prep
%setup -q -n sddm-0.18.0
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1548466343
mkdir -p clr-build
pushd clr-build
%cmake .. -DUID_MIN=1000 -DUID_MAX=60000 -DDBUS_CONFIG_FILENAME=sddm_org.fredesktop.DisplayManager.conf
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1548466343
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/sddm
cp LICENSE %{buildroot}/usr/share/package-licenses/sddm/LICENSE
cp LICENSE.CC-BY-3.0 %{buildroot}/usr/share/package-licenses/sddm/LICENSE.CC-BY-3.0
cp data/themes/maldives/LICENSE %{buildroot}/usr/share/package-licenses/sddm/data_themes_maldives_LICENSE
cp data/themes/maya/LICENSE %{buildroot}/usr/share/package-licenses/sddm/data_themes_maya_LICENSE
cp src/greeter/theme/LICENSE %{buildroot}/usr/share/package-licenses/sddm/src_greeter_theme_LICENSE
pushd clr-build
%make_install
popd
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/tmpfiles.d/sddm.conf
## install_append content
install -D -d -m 00755 %{buildroot}/usr/lib/systemd/system/graphical.target.wants
ln -sv ../sddm.service %{buildroot}/usr/lib/systemd/system/graphical.target.wants/sddm.service
## install_append end

%files
%defattr(-,root,root,-)

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/graphical.target.wants/sddm.service

%files bin
%defattr(-,root,root,-)
/usr/bin/sddm
/usr/bin/sddm-greeter

%files config
%defattr(-,root,root,-)
/usr/lib/tmpfiles.d/sddm.conf

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/system.d/sddm_org.fredesktop.DisplayManager.conf
/usr/share/pam.d/sddm
/usr/share/pam.d/sddm-autologin
/usr/share/pam.d/sddm-greeter
/usr/share/sddm/faces/.face.icon
/usr/share/sddm/faces/root.face.icon
/usr/share/sddm/flags/ae.png
/usr/share/sddm/flags/am.png
/usr/share/sddm/flags/ar.png
/usr/share/sddm/flags/at.png
/usr/share/sddm/flags/az.png
/usr/share/sddm/flags/be.png
/usr/share/sddm/flags/bg.png
/usr/share/sddm/flags/bh.png
/usr/share/sddm/flags/br.png
/usr/share/sddm/flags/by.png
/usr/share/sddm/flags/ca.png
/usr/share/sddm/flags/ch.png
/usr/share/sddm/flags/cu.png
/usr/share/sddm/flags/cz.png
/usr/share/sddm/flags/de.png
/usr/share/sddm/flags/dj.png
/usr/share/sddm/flags/dk.png
/usr/share/sddm/flags/dz.png
/usr/share/sddm/flags/ee.png
/usr/share/sddm/flags/eg.png
/usr/share/sddm/flags/es.png
/usr/share/sddm/flags/eu.png
/usr/share/sddm/flags/fi.png
/usr/share/sddm/flags/fr.png
/usr/share/sddm/flags/gb.png
/usr/share/sddm/flags/ge.png
/usr/share/sddm/flags/gr.png
/usr/share/sddm/flags/hr.png
/usr/share/sddm/flags/hu.png
/usr/share/sddm/flags/il.png
/usr/share/sddm/flags/in.png
/usr/share/sddm/flags/iq.png
/usr/share/sddm/flags/is.png
/usr/share/sddm/flags/it.png
/usr/share/sddm/flags/jo.png
/usr/share/sddm/flags/jp.png
/usr/share/sddm/flags/km.png
/usr/share/sddm/flags/kr.png
/usr/share/sddm/flags/kw.png
/usr/share/sddm/flags/la.png
/usr/share/sddm/flags/lb.png
/usr/share/sddm/flags/lt.png
/usr/share/sddm/flags/lv.png
/usr/share/sddm/flags/ly.png
/usr/share/sddm/flags/ma.png
/usr/share/sddm/flags/mk.png
/usr/share/sddm/flags/mn.png
/usr/share/sddm/flags/mx.png
/usr/share/sddm/flags/nl.png
/usr/share/sddm/flags/no.png
/usr/share/sddm/flags/om.png
/usr/share/sddm/flags/pl.png
/usr/share/sddm/flags/ps.png
/usr/share/sddm/flags/pt.png
/usr/share/sddm/flags/qa.png
/usr/share/sddm/flags/qc.png
/usr/share/sddm/flags/ro.png
/usr/share/sddm/flags/ru.png
/usr/share/sddm/flags/sa.png
/usr/share/sddm/flags/sd.png
/usr/share/sddm/flags/se.png
/usr/share/sddm/flags/si.png
/usr/share/sddm/flags/sk.png
/usr/share/sddm/flags/so.png
/usr/share/sddm/flags/sr.png
/usr/share/sddm/flags/sy.png
/usr/share/sddm/flags/th.png
/usr/share/sddm/flags/tn.png
/usr/share/sddm/flags/tr.png
/usr/share/sddm/flags/ua.png
/usr/share/sddm/flags/uk.png
/usr/share/sddm/flags/un.png
/usr/share/sddm/flags/us.png
/usr/share/sddm/flags/uy.png
/usr/share/sddm/flags/vn.png
/usr/share/sddm/flags/ye.png
/usr/share/sddm/flags/yu.png
/usr/share/sddm/flags/zz.png
/usr/share/sddm/scripts/Xsession
/usr/share/sddm/scripts/Xsetup
/usr/share/sddm/scripts/Xstop
/usr/share/sddm/scripts/wayland-session
/usr/share/sddm/themes/elarun/Main.qml
/usr/share/sddm/themes/elarun/README
/usr/share/sddm/themes/elarun/angle-down.png
/usr/share/sddm/themes/elarun/elarun.jpg
/usr/share/sddm/themes/elarun/images/background.png
/usr/share/sddm/themes/elarun/images/lock.png
/usr/share/sddm/themes/elarun/images/login_active.png
/usr/share/sddm/themes/elarun/images/login_normal.png
/usr/share/sddm/themes/elarun/images/rectangle.png
/usr/share/sddm/themes/elarun/images/rectangle_overlay.png
/usr/share/sddm/themes/elarun/images/session_normal.png
/usr/share/sddm/themes/elarun/images/system_hibernate.png
/usr/share/sddm/themes/elarun/images/system_reboot.png
/usr/share/sddm/themes/elarun/images/system_shutdown.png
/usr/share/sddm/themes/elarun/images/system_suspend.png
/usr/share/sddm/themes/elarun/images/system_switch_user.png
/usr/share/sddm/themes/elarun/images/user_icon.png
/usr/share/sddm/themes/elarun/metadata.desktop
/usr/share/sddm/themes/elarun/theme.conf
/usr/share/sddm/themes/maldives/LICENSE
/usr/share/sddm/themes/maldives/Main.qml
/usr/share/sddm/themes/maldives/README
/usr/share/sddm/themes/maldives/angle-down.png
/usr/share/sddm/themes/maldives/background.jpg
/usr/share/sddm/themes/maldives/maldives.jpg
/usr/share/sddm/themes/maldives/metadata.desktop
/usr/share/sddm/themes/maldives/rectangle.png
/usr/share/sddm/themes/maldives/theme.conf
/usr/share/sddm/themes/maya/LICENSE
/usr/share/sddm/themes/maya/Main.qml
/usr/share/sddm/themes/maya/README
/usr/share/sddm/themes/maya/components/SpButton.qml
/usr/share/sddm/themes/maya/components/SpClock.qml
/usr/share/sddm/themes/maya/fonts/OpenSans_CondLight.ttf
/usr/share/sddm/themes/maya/images/ic_arrow_drop_down_white_24px.svg
/usr/share/sddm/themes/maya/images/ic_power_settings_new_white_24px.svg
/usr/share/sddm/themes/maya/images/ic_refresh_white_24px.svg
/usr/share/sddm/themes/maya/images/ic_warning_white_24px.svg
/usr/share/sddm/themes/maya/metadata.desktop
/usr/share/sddm/themes/maya/screenshots/hi_IN.png
/usr/share/sddm/themes/maya/theme.conf
/usr/share/sddm/translations/ar.qm
/usr/share/sddm/translations/bn.qm
/usr/share/sddm/translations/ca.qm
/usr/share/sddm/translations/cs.qm
/usr/share/sddm/translations/da.qm
/usr/share/sddm/translations/de.qm
/usr/share/sddm/translations/es.qm
/usr/share/sddm/translations/et.qm
/usr/share/sddm/translations/fi.qm
/usr/share/sddm/translations/fr.qm
/usr/share/sddm/translations/hi_IN.qm
/usr/share/sddm/translations/hu.qm
/usr/share/sddm/translations/is.qm
/usr/share/sddm/translations/it.qm
/usr/share/sddm/translations/ja.qm
/usr/share/sddm/translations/kk.qm
/usr/share/sddm/translations/ko.qm
/usr/share/sddm/translations/lt.qm
/usr/share/sddm/translations/lv.qm
/usr/share/sddm/translations/nb.qm
/usr/share/sddm/translations/nl.qm
/usr/share/sddm/translations/nn.qm
/usr/share/sddm/translations/pl.qm
/usr/share/sddm/translations/pt_BR.qm
/usr/share/sddm/translations/pt_PT.qm
/usr/share/sddm/translations/ro.qm
/usr/share/sddm/translations/ru.qm
/usr/share/sddm/translations/sk.qm
/usr/share/sddm/translations/sr.qm
/usr/share/sddm/translations/sr@ijekavian.qm
/usr/share/sddm/translations/sr@ijekavianlatin.qm
/usr/share/sddm/translations/sr@latin.qm
/usr/share/sddm/translations/sv.qm
/usr/share/sddm/translations/tr.qm
/usr/share/sddm/translations/uk.qm
/usr/share/sddm/translations/zh_CN.qm
/usr/share/sddm/translations/zh_TW.qm

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/qml/SddmComponents/Background.qml
/usr/lib64/qt5/qml/SddmComponents/Button.qml
/usr/lib64/qt5/qml/SddmComponents/Clock.qml
/usr/lib64/qt5/qml/SddmComponents/ComboBox.qml
/usr/lib64/qt5/qml/SddmComponents/ImageButton.qml
/usr/lib64/qt5/qml/SddmComponents/LayoutBox.qml
/usr/lib64/qt5/qml/SddmComponents/Menu.qml
/usr/lib64/qt5/qml/SddmComponents/PasswordBox.qml
/usr/lib64/qt5/qml/SddmComponents/PictureBox.qml
/usr/lib64/qt5/qml/SddmComponents/TextBox.qml
/usr/lib64/qt5/qml/SddmComponents/TextConstants.qml
/usr/lib64/qt5/qml/SddmComponents/qmldir
/usr/lib64/qt5/qml/SddmComponents/warning.png

%files libexec
%defattr(-,root,root,-)
/usr/libexec/sddm-helper

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sddm/LICENSE
/usr/share/package-licenses/sddm/LICENSE.CC-BY-3.0
/usr/share/package-licenses/sddm/data_themes_maldives_LICENSE
/usr/share/package-licenses/sddm/data_themes_maya_LICENSE
/usr/share/package-licenses/sddm/src_greeter_theme_LICENSE

%files services
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/graphical.target.wants/sddm.service
/usr/lib/systemd/system/sddm.service
