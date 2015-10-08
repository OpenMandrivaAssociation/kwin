%define debug_package %{nil}

%define effectmajor 1
%define effectname %mklibname kwin4_effect_builtins %{effectmajor}
%define effectdname %mklibname kwin4_effect_builtins -d

%define effectsmajor 6
%define effectsname %mklibname keffects %{effectsmajor}
%define effectsdname %mklibname keffects -d

%define glutilsmajor 6
%define glutilsname %mklibname kwinglutils %{glutilsmajor}
%define glutilsdname %mklibname kwinglutils -d

%define xrenderutilsmajor 6
%define xrenderutilsname %mklibname kwinxrenderutils %{xrenderutilsmajor}
%define xrenderutilsdname %mklibname kwinxrenderutils -d

%define plasmaver %(echo %{version} |cut -d. -f1-3)

%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kwin
Version: 5.4.2
Release: 1
Source0: http://download.kde.org/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
Source1000: %{name}.rpmlintrc
Patch1: kwin-5.3.0-enable-minimizeall.patch
Summary: The KWin window manager
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: qt5-qtmultimedia
# Some of the cmake(*) stuff below is provided by both kdelibs4-devel and
# libKF5KDELibs4Support-devel - let's make sure we pick the right one
BuildRequires: %mklibname -d KF5KDELibs4Support
BuildRequires: pkgconfig(egl)
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
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5UiTools)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(libinput)
BuildRequires: pkgconfig(udev)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-cursor)
BuildRequires: pkgconfig(wayland-egl)
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
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(sm)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5)
BuildRequires: cmake(KF5Activities)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(KF5NewStuff)
BuildRequires: cmake(KF5KCMUtils)
BuildRequires: cmake(KF5Crash)
BuildRequires: cmake(KF5Init)
BuildRequires: cmake(KF5Notifications)
BuildRequires: cmake(KF5Plasma)
BuildRequires: cmake(KF5Wayland)
BuildRequires: cmake(KDecoration2)
Requires: %{name}-windowsystem = %{EVRD}
Requires: qt5-qtmultimedia
Obsoletes: %{name}-wayland < 5.4.0
Provides: %{name}-wayland = 5.4.0

%description
The KWin window manager.

%package x11
Summary: X11 Window System support for KWin
Requires: %{name} = %{EVRD}
Provides: %{name}-windowsystem = %{EVRD}
Requires: qt5-output-driver-default
Group: System/Libraries

%description x11
X11 Window System support for KWin.

%package -n %{effectname}
Summary: KWin effect library
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{effectname}
KWin effect library.

%package -n %{effectsname}
Summary: KWin effects library
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{effectsname}
KWin effects library.

%package -n %{glutilsname}
Summary: KWin GL utils library
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{glutilsname}
KWin GL utils library.

%package -n %{xrenderutilsname}
Summary: KWin XRender utils library
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{xrenderutilsname}
KWin XRender utils library.

%package devel
Summary: Development files for the KDE Frameworks 5 Win library
Group: Development/KDE and Qt
Requires: %{effectname} = %{EVRD}
Requires: %{effectsname} = %{EVRD}
Requires: %{glutilsname} = %{EVRD}
Requires: %{xrenderutilsname} = %{EVRD}
Provides: %{effectdname} = %{EVRD}
Provides: %{effectsdname} = %{EVRD}
Provides: %{glutilsdname} = %{EVRD}
Provides: %{xrenderutilsdname} = %{EVRD}

%description devel
Development files for the KDE Frameworks 5 Win library.

%libpackage kwin 5

%prep
%setup -q
%apply_patches
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang kcm-kwin-scripts
%find_lang kcm_kwindesktop
%find_lang kcm_kwintabbox
%find_lang kcmkwincompositing
%find_lang kcmkwindecoration
%find_lang kcmkwinrules
%find_lang kcmkwinscreenedges
%find_lang kcmkwm
%find_lang kwin
%find_lang kwin_clients
%find_lang kwin_effects
%find_lang kwin_scripting
cat *.lang >kwin-all.lang

%files -f kwin-all.lang
%{_bindir}/kwin_wayland
%{_datadir}/kwin
%{_datadir}/kwincompositing
%{_datadir}/kservices5/*
%{_datadir}/kservicetypes5/*
%{_datadir}/knotifications5/*
%{_datadir}/icons/*/*/*/*
%{_datadir}/dbus-1/*/*
%{_libdir}/qt5/qml/org/kde/kwin
%{_libdir}/qt5/plugins/kwin
%{_libdir}/qt5/plugins/kwincompositing.so
%{_libdir}/qt5/plugins/kcm_kwin*
%{_libdir}/qt5/plugins/org.kde.kdecoration2
%{_libdir}/qt5/plugins/org.kde.kglobalaccel5.platforms
%{_libdir}/qt5/plugins/org.kde.kwin.waylandbackends
%{_libdir}/kconf_update_bin/kwin5_update_default_rules
%{_libdir}/libexec/kwin*
%{_libdir}/libkdeinit5_kwin_rules_dialog.so
%{_datadir}/config.kcfg/kwin.kcfg
%{_sysconfdir}/xdg/*
%doc %{_docdir}/HTML/en/kcontrol/desktop
%doc %{_docdir}/HTML/en/kcontrol/kwindecoration
%doc %{_docdir}/HTML/en/kcontrol/kwinscreenedges
%doc %{_docdir}/HTML/en/kcontrol/kwintabbox
%doc %{_docdir}/HTML/en/kcontrol/windowbehaviour
%doc %{_docdir}/HTML/en/kcontrol/windowspecific

%files x11
%{_bindir}/kwin_x11
%{_libdir}/libkdeinit5_kwin_x11.so

%files -n %{effectname}
%{_libdir}/libkwin4_effect_builtins.so.%{effectmajor}*

%files -n %{effectsname}
%{_libdir}/libkwineffects.so.%{effectsmajor}
%{_libdir}/libkwineffects.so.%{plasmaver}

%files -n %{glutilsname}
%{_libdir}/libkwingl*utils.so.%{glutilsmajor}
%{_libdir}/libkwingl*utils.so.%{plasmaver}

%files -n %{xrenderutilsname}
%{_libdir}/libkwinxrenderutils.so.%{xrenderutilsmajor}
%{_libdir}/libkwinxrenderutils.so.%{plasmaver}

%files devel
%{_includedir}/*
%{_libdir}/libkwin4_effect_builtins.so
%{_libdir}/libkwineffects.so
%{_libdir}/libkwingl*utils.so
%{_libdir}/libkwinxrenderutils.so
%{_libdir}/cmake/KWinDBusInterface
