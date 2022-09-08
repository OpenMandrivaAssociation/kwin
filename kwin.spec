%define effectsmajor 13
%define effectsname %mklibname keffects %{effectsmajor}
%define effectsdname %mklibname keffects -d

%define glutilsmajor 13
%define glutilsname %mklibname kwinglutils %{glutilsmajor}
%define glutilsdname %mklibname kwinglutils -d

%define xrenderutilsmajor 13
%define xrenderutilsname %mklibname kwinxrenderutils %{xrenderutilsmajor}
%define xrenderutilsdname %mklibname kwinxrenderutils -d

%define kcmkwincommonmajor 5
%define kcmkwincommon %mklibname kcmkwincommon %{kcmkwincommonmajor}

%define plasmaver %(echo %{version} |cut -d. -f1-3)

%define stable %([ "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

# (tpg) optimize it a bit
%global optflags %{optflags} -O3

Summary: The KWin window manager
Name: kwin
Version: 5.25.5
Release: 2
URL: http://kde.org/
License: GPL
Group: System/Libraries
Source0: http://download.kde.org/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
Source1000: %{name}.rpmlintrc
#Patch0: kwin-5.10.3-workaround-clang-bug-33617.patch
# (tpg) is it still needed ?
#Patch1: kwin-5.3.0-enable-minimizeall.patch
# (tpg) this patch add supports for Panfrost Mali driver just to adjust supported effects
# (bero) extended the patch to do the same for Lima, VC4 and VC3D
Patch100: kwin-5.21.4-add-support-for-panfrost-driver.patch

BuildRequires: qt5-qtmultimedia
# Some of the cmake(*) stuff below is provided by both kdelibs4-devel and
# libKF5KDELibs4Support-devel - let's make sure we pick the right one
BuildRequires: %mklibname -d KF5KDELibs4Support
BuildRequires: pkgconfig(egl)
BuildRequires: %{_lib}EGL_mesa-devel
BuildRequires: pkgconfig(epoxy)
BuildRequires: pkgconfig(Qt5Concurrent)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Multimedia)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: pkgconfig(Qt5QuickWidgets)
BuildRequires: pkgconfig(Qt5Script)
BuildRequires: pkgconfig(Qt5Sensors)
BuildRequires: pkgconfig(Qt5UiTools)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(libinput)
BuildRequires: pkgconfig(libxcvt)
BuildRequires: pkgconfig(gbm)
BuildRequires: pkgconfig(udev)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-cursor)
BuildRequires: pkgconfig(wayland-egl)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-composite)
BuildRequires: pkgconfig(xcb-cursor)
BuildRequires: pkgconfig(xcb-damage)
BuildRequires: pkgconfig(xcb-glx)
BuildRequires: pkgconfig(xcb-icccm)
BuildRequires: pkgconfig(xcb-image)
BuildRequires: pkgconfig(xcb-keysyms)
BuildRequires: pkgconfig(xcb-randr)
BuildRequires: pkgconfig(xcb-render)
BuildRequires: pkgconfig(xcb-shape)
BuildRequires: pkgconfig(xcb-shm)
BuildRequires: pkgconfig(xcb-sync)
BuildRequires: pkgconfig(xcb-xfixes)
BuildRequires: pkgconfig(xcb-xtest)
BuildRequires: pkgconfig(xcb-event)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(xi)
BuildRequires: pkgconfig(sm)
BuildRequires: pkgconfig(libcap)
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5)
BuildRequires: cmake(KF5Activities)
BuildRequires: cmake(KF5Declarative)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(KF5NewStuff)
BuildRequires: cmake(KF5KCMUtils)
BuildRequires: cmake(KF5Crash)
BuildRequires: cmake(KF5Init)
BuildRequires: cmake(KF5Notifications)
BuildRequires: cmake(KF5Plasma)
BuildRequires: cmake(KF5PlasmaQuick)
BuildRequires: cmake(KF5Wayland)
BuildRequires: cmake(KDecoration2)
BuildRequires: cmake(KF5IdleTime)
BuildRequires: cmake(KF5GlobalAccel)
BuildRequires: cmake(KScreenLocker)
BuildRequires: cmake(Breeze)
BuildRequires: cmake(KF5Kirigami2)
BuildRequires: cmake(KWaylandServer)
BuildRequires: cmake(QAccessibilityClient)
BuildRequires: cmake(KF5Runner)
BuildRequires: cmake(Qt5XkbCommonSupport)
BuildRequires: cmake(Qt5ServiceSupport)
BuildRequires: cmake(PlasmaWaylandProtocols)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(lcms2)
BuildRequires: pkgconfig(libpipewire-0.3)
BuildRequires: x11-server-xwayland
BuildRequires: qt5-qtvirtualkeyboard
BuildRequires: qt5-qtwayland
BuildRequires: qt5-qtquickcontrols
BuildRequires: qt5-qtwayland-private-devel
BuildRequires: hwdata
#BuildRequires: libhybris
BuildRequires: %mklibname -d -s qt5eventdispatchersupport
BuildRequires: %mklibname -d -s qt5fontdatabasesupport
BuildRequires: %mklibname -d -s qt5themesupport
Requires: %{name}-windowsystem = %{EVRD}
Requires: qt5-qtmultimedia
Requires: qt5-qtvirtualkeyboard
Requires: qt5-qtquickcontrols
Requires: plasma-framework
#(tpg) this is needed for kcm_kwin_effects
Requires: glib-networking
# Obsolete packages that used to be split out solely for old policy reasons
%define effectmajor 1
%define effectname %mklibname kwin4_effect_builtins 1
Obsoletes: %{effectname} < %{EVRD}
%if %omvver > 4050000
Requires: %{name}-wayland
%endif

%description
The KWin window manager.

%package x11
Summary: X11 Window System support for KWin
Requires: %{name} = %{EVRD}
Provides: %{name}-windowsystem = %{EVRD}
Requires: %{_lib}qt5-output-driver-default
Requires: kwindowsystem-x11
Requires: libkscreen-x11
Group: System/Libraries

%description x11
X11 Window System support for KWin.

%package wayland
Summary: Wayland Window System support for KWin
Requires: %{name} = %{EVRD}
Provides: %{name}-windowsystem = %{EVRD}
Requires: kwayland-integration
Requires: %{_lib}qt5-output-driver-default
Requires: xwayland
Requires: kwindowsystem-wayland
Requires: kwayland-server
Requires: libkscreen-wayland
Group: System/Libraries

%description wayland
Wayland Window System support for KWin.

%package -n %{effectsname}
Summary: KWin effects library
Group: System/Libraries
Requires: %{name} = %{EVRD}
Obsoletes: %{mklibname kwineffects 12} < 5.20.90

%description -n %{effectsname}
KWin effects library.

%package -n %{glutilsname}
Summary: KWin GL utils library
Group: System/Libraries
Requires: %{name} = %{EVRD}
Obsoletes: %{mklibname kwinglutils 7} < 5.6.0
Obsoletes: %{mklibname kwinglutils 8} < 5.8.2
Obsoletes: %{mklibname kwinglutils 11} < 5.14.90
Obsoletes: %{mklibname kwinglutils 12} < 5.20.90

%description -n %{glutilsname}
KWin GL utils library.

%package -n %{xrenderutilsname}
Summary: KWin XRender utils library
Group: System/Libraries
Requires: %{name} = %{EVRD}
Obsoletes: %{mklibname kwinxrenderutils 7} < 5.6.0
Obsoletes: %{mklibname kwinxrenderutils 8} < 5.8.2
Obsoletes: %{mklibname kwinxrenderutils 11} < 5.14.90
Obsoletes: %{mklibname kwinxrenderutils 12} < 5.20.90

%description -n %{xrenderutilsname}
KWin XRender utils library.

%package -n %{kcmkwincommon}
Summary: KWin KCM library
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{kcmkwincommon}
KWin KCM library.

%package devel
Summary: Development files for the KDE Frameworks 5 Win library
Group: Development/KDE and Qt
Requires: %{effectsname} = %{EVRD}
Requires: %{glutilsname} = %{EVRD}
Requires: %{xrenderutilsname} = %{EVRD}
Provides: %{effectsdname} = %{EVRD}
Provides: %{glutilsdname} = %{EVRD}
Provides: %{xrenderutilsdname} = %{EVRD}

%description devel
Development files for the KDE Frameworks 5 Win library.

%libpackage kwin 5

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

# (tpg) add missing symlinks
ln -s %{_datadir}/kservicetypes5/kwineffect.desktop %{buildroot}%{_datadir}/kservicetypes5/kwin-effect.desktop
ln -s %{_datadir}/kservicetypes5/kwinscript.desktop %{buildroot}%{_datadir}/kservicetypes5/kwin-script.desktop

%find_lang %{name} --all-name --with-html --with-man

%files -f %{name}.lang
%{_datadir}/config.kcfg/*
%{_datadir}/kconf_update/*.upd
%{_datadir}/kconf_update/*.pl
%{_datadir}/kconf_update/*.py
%{_datadir}/kconf_update/*.sh
%{_datadir}/kwin
%{_datadir}/kservices5/*
%{_datadir}/kservicetypes5/*
%{_datadir}/knotifications5/*
%{_datadir}/kpackage/kcms/kcm_kwin_virtualdesktops
%{_datadir}/icons/*/*/*/*
%{_datadir}/dbus-1/*/*
%{_libdir}/qt5/qml/org/kde/kwin
%{_libdir}/qt5/plugins/kwin
%{_libdir}/qt5/plugins/org.kde.kdecoration2
%{_libdir}/qt5/plugins/kpackage/*
%dir %{_libdir}/qt5/plugins/org.kde.kwin.platforms
%{_libdir}/kconf_update_bin/kwin5_update_default_rules
%{_libdir}/libexec/kwin*
%{_datadir}/qlogging-categories5/*
%{_datadir}/knsrcfiles/*.knsrc
%{_datadir}/kpackage/kcms/kcm_kwin_effects
%{_datadir}/kpackage/kcms/kcm_kwindecoration
%{_datadir}/kpackage/kcms/kcm_kwinrules
%{_datadir}/krunner/dbusplugins/kwin-runner-windows.desktop
%{_datadir}/kpackage/kcms/kcm_virtualkeyboard
%{_datadir}/applications/org.kde.kwin_rules_dialog.desktop
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_kwin_effects.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_kwin_scripts.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_kwin_virtualdesktops.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_kwindecoration.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_kwinrules.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_virtualkeyboard.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings_qwidgets/kcm_kwinoptions.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings_qwidgets/kcm_kwinscreenedges.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings_qwidgets/kcm_kwintabbox.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings_qwidgets/kcm_kwintouchscreen.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings_qwidgets/kwincompositing.so
%{_libdir}/qt5/qml/org/kde/kwin.2
%{_datadir}/applications/kcm_kwin_effects.desktop
%{_datadir}/applications/kcm_kwin_scripts.desktop
%{_datadir}/applications/kcm_kwin_virtualdesktops.desktop
%{_datadir}/applications/kcm_kwindecoration.desktop
%{_datadir}/applications/kcm_kwinoptions.desktop
%{_datadir}/applications/kcm_kwinrules.desktop
%{_datadir}/applications/kcm_kwinscreenedges.desktop
%{_datadir}/applications/kcm_kwintouchscreen.desktop
%{_datadir}/applications/kcm_virtualkeyboard.desktop
%{_datadir}/applications/kwincompositing.desktop
%{_datadir}/kpackage/kcms/kcm_kwin_scripts/contents/ui/main.qml

%files x11
%{_bindir}/kwin_x11
%{_libdir}/qt5/plugins/org.kde.kwin.platforms/KWinX11Platform.so
%{_prefix}/lib/systemd/user/plasma-kwin_x11.service

%files wayland
%caps(cap_sys_resource+ep) %{_bindir}/kwin_wayland
%{_bindir}/kwin_wayland_wrapper
%{_libdir}/qt5/plugins/org.kde.kwin.waylandbackends
%{_prefix}/lib/systemd/user/plasma-kwin_wayland.service

%files -n %{effectsname}
%{_libdir}/libkwineffects.so.%{effectsmajor}
%{_libdir}/libkwineffects.so.%{plasmaver}

%files -n %{glutilsname}
%{_libdir}/libkwingl*utils.so.%{glutilsmajor}
%{_libdir}/libkwingl*utils.so.%{plasmaver}

%files -n %{xrenderutilsname}
%{_libdir}/libkwinxrenderutils.so.%{xrenderutilsmajor}
%{_libdir}/libkwinxrenderutils.so.%{plasmaver}

%files -n %{kcmkwincommon}
%{_libdir}/libkcmkwincommon.so.%{kcmkwincommonmajor}
%{_libdir}/libkcmkwincommon.so.%{plasmaver}

%files devel
%{_includedir}/*
%{_libdir}/libkwineffects.so
%{_libdir}/libkwingl*utils.so
%{_libdir}/libkwinxrenderutils.so
%{_libdir}/cmake/KWinDBusInterface
%{_libdir}/cmake/KWinEffects
