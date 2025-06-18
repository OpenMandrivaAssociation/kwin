%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
#define git 20240222
%define gitbranch Plasma/6.0
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

# (tpg) optimize it a bit
%global optflags %{optflags} -O3

Summary: The KWin window manager
Name: kwin
Version: 6.4.0
Release: %{?git:0.%{git}.}1
URL: https://kde.org/
License: GPL
Group: System/Libraries
%if 0%{?git:1}
Source0:	https://invent.kde.org/plasma/kwin/-/archive/%{gitbranch}/kwin-%{gitbranchd}.tar.bz2#/kwin-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{stable}/plasma/%{plasmaver}/kwin-%{version}.tar.xz
%endif
Patch0: kwin-6.3.3-wayland-egl-is-wayland.patch
# (tpg) is it still needed ?
#Patch1: kwin-5.3.0-enable-minimizeall.patch

BuildRequires: appstream
BuildRequires: pkgconfig(egl)
BuildRequires: %{_lib}EGL_mesa-devel
BuildRequires: pkgconfig(epoxy)
BuildRequires: cmake(QAccessibilityClient6)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Concurrent)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Multimedia)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6QmlCore)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6QuickWidgets)
BuildRequires: cmake(Qt6Sensors)
BuildRequires: cmake(Qt6UiTools)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6UiPlugin)
BuildRequires: cmake(Qt6UiTools)
BuildRequires: cmake(Qt6Core5Compat)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6Service)
BuildRequires: cmake(KF6Svg)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(libinput)
BuildRequires: pkgconfig(libxcvt)
BuildRequires: pkgconfig(gbm)
BuildRequires: pkgconfig(udev)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(libcanberra)
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
BuildRequires: pkgconfig(xkbcommon-x11)
BuildRequires: pkgconfig(xi)
BuildRequires: pkgconfig(sm)
BuildRequires: pkgconfig(libcap)
BuildRequires: pkgconfig(libei-1.0)
BuildRequires: pkgconfig(libeis-1.0)
BuildRequires: cmake(ECM)
BuildRequires: cmake(PlasmaActivities)
BuildRequires: cmake(KF6Declarative)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6NewStuff)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(Plasma) >= 5.90.0
BuildRequires: cmake(PlasmaQuick) >= 5.90.0
BuildRequires: cmake(Wayland) >= 5.90.0
BuildRequires: cmake(KDecoration3)
BuildRequires: cmake(KF6IdleTime)
BuildRequires: cmake(KF6GlobalAccel)
BuildRequires: cmake(KScreenLocker) > 5.27.50
BuildRequires: cmake(Breeze)
BuildRequires: cmake(KF6Kirigami2)
BuildRequires: cmake(KF6Runner)
BuildRequires: cmake(KF6GlobalAccel)
BuildRequires: cmake(KF6Auth)
BuildRequires: cmake(KGlobalAccelD)
BuildRequires: cmake(PlasmaWaylandProtocols)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(lcms2)
BuildRequires: pkgconfig(libpipewire-0.3)
BuildRequires: pkgconfig(libdisplay-info)
BuildRequires: cmake(KPipeWire) > 5.27.50
BuildRequires: cmake(KWayland)
BuildRequires: pkgconfig(vulkan)
BuildRequires: cmake(VulkanHeaders)
# FIXME Package QAccessibilityClient6 and BR it
BuildRequires: x11-server-xwayland
BuildRequires: hwdata
#BuildRequires: libhybris
Requires: libplasma plasma-framework-common
#(tpg) this is needed for kcm_kwin_effects
Requires: glib-networking
# Obsolete packages that used to be split out solely for old policy reasons
%define effectmajor 1
%define effectname %mklibname kwin4_effect_builtins 1
Obsoletes: %{effectname} < %{EVRD}
BuildSystem: cmake
BuildOption: -DBUILD_QCH:BOOL=ON
BuildOption: -DBUILD_WITH_QT6:BOOL=ON
BuildOption: -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
Requires: %mklibname Qt6WaylandCompositor
Requires: %mklibname Qt6WlShellIntegration
# Renamed 2025-05-01 after 6.0
%rename plasma6-kwin
%rename plasma6-kwin-wayland

%description
The KWin window manager.

%package devel
Summary: Development files for the KDE Frameworks 5 Win library
Group: Development/KDE and Qt
# Renamed 2025-05-01 after 6.0
%rename plasma6-kwin-devel

%description devel
Development files for the KDE Frameworks 5 Win library.

%files -f %{name}.lang
%{_datadir}/applications/kcm_kwintabbox.desktop
%{_datadir}/config.kcfg/*
%{_datadir}/knotifications6/*
%{_datadir}/icons/*/*/*/*
%{_datadir}/dbus-1/*/*
%{_libdir}/kconf_update_bin/kwin5_update_default_rules
%{_qtdir}/plugins/kf6/packagestructure/*
%{_qtdir}/qml/org/kde/kwin
%{_qtdir}/plugins/kwin
%{_libdir}/libexec/kwin*
%{_datadir}/qlogging-categories6/*
%{_datadir}/knsrcfiles/*.knsrc
%{_datadir}/krunner/dbusplugins/kwin-runner-windows.desktop
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_kwin_effects.so
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_kwin_scripts.so
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_kwin_virtualdesktops.so
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_kwindecoration.so
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_kwinrules.so
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_virtualkeyboard.so
%{_qtdir}/plugins/plasma/kcms/systemsettings_qwidgets/kcm_kwinoptions.so
%{_qtdir}/plugins/plasma/kcms/systemsettings_qwidgets/kcm_kwinscreenedges.so
%{_qtdir}/plugins/plasma/kcms/systemsettings_qwidgets/kcm_kwintabbox.so
%{_qtdir}/plugins/plasma/kcms/systemsettings_qwidgets/kcm_kwintouchscreen.so
%{_datadir}/applications/kcm_kwin_effects.desktop
%{_datadir}/applications/kcm_kwin_scripts.desktop
%{_datadir}/applications/kcm_kwin_virtualdesktops.desktop
%{_datadir}/applications/kcm_kwindecoration.desktop
%{_datadir}/applications/kcm_kwinoptions.desktop
%{_datadir}/applications/kcm_kwinrules.desktop
%{_datadir}/applications/kcm_virtualkeyboard.desktop
%{_datadir}/applications/org.kde.kwin.killer.desktop
%{_libdir}/libkcmkwincommon.so*
%{_libdir}/libkwin.so*
%{_datadir}/kconf_update/*.upd
%{_libdir}/kconf_update_bin/kwin-6.0-delete-desktop-switching-shortcuts
%{_libdir}/kconf_update_bin/kwin-6.0-reset-active-mouse-screen
%{_libdir}/kconf_update_bin/kwin-6.0-remove-breeze-tabbox-default
%{_libdir}/kconf_update_bin/kwin-6.1-remove-gridview-expose-shortcuts
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_animations.so
%{_datadir}/applications/kcm_animations.desktop
%caps(cap_sys_nice+ep) %{_bindir}/kwin_wayland
%{_bindir}/kwin_wayland_wrapper
%{_prefix}/lib/systemd/user/plasma-kwin_wayland.service
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_kwinxwayland.so
%{_datadir}/applications/kcm_kwinxwayland.desktop
%{_datadir}/kwin-wayland

%files devel
%{_includedir}/*
%{_libdir}/cmake/KWinDBusInterface
%{_libdir}/cmake/KWin
