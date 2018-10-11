%define debug_package %{nil}

%define effectmajor 1
%define effectname %mklibname kwin4_effect_builtins %{effectmajor}
%define effectdname %mklibname kwin4_effect_builtins -d

%define effectsmajor 11
%define effectsname %mklibname keffects %{effectsmajor}
%define effectsdname %mklibname keffects -d

%define glutilsmajor 11
%define glutilsname %mklibname kwinglutils %{glutilsmajor}
%define glutilsdname %mklibname kwinglutils -d

%define xrenderutilsmajor 11
%define xrenderutilsname %mklibname kwinxrenderutils %{xrenderutilsmajor}
%define xrenderutilsdname %mklibname kwinxrenderutils -d

%define plasmaver %(echo %{version} |cut -d. -f1-3)

%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

# (tpg) optimize it a bit
%global optflags %{optflags} -O3

Name: kwin
Version: 5.14.0
Release: 2
Source0: http://download.kde.org/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
Source1000: %{name}.rpmlintrc
#Patch0: kwin-5.10.3-workaround-clang-bug-33617.patch
# (tpg) is it still needed ?
#Patch1: kwin-5.3.0-enable-minimizeall.patch
Patch2: kwin-5.10.5-aarch64-compile.patch
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
BuildRequires: pkgconfig(Qt5Sensors)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5UiTools)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(libinput)
BuildRequires: pkgconfig(gbm)
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
BuildRequires: pkgconfig(xi)
BuildRequires: pkgconfig(sm)
BuildRequires: pkgconfig(libcap)
BuildRequires: cmake(KF5DocTools)
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
BuildRequires: x11-server-xwayland
BuildRequires: qt5-qtvirtualkeyboard
BuildRequires: qt5-qtquickcontrols
#BuildRequires: libhybris
BuildRequires: %mklibname -d -s qt5eventdispatchersupport
BuildRequires: %mklibname -d -s qt5fontdatabasesupport
BuildRequires: %mklibname -d -s qt5themesupport
Requires: %{name}-windowsystem = %{EVRD}
Requires: qt5-qtmultimedia
Requires: qt5-qtvirtualkeyboard
Requires: qt5-qtquickcontrols
Requires: plasma-framework
Obsoletes: %{name}-wayland < 5.4.0
Provides: %{name}-wayland = 5.4.0

%description
The KWin window manager.

%package x11
Summary: X11 Window System support for KWin
Requires: %{name} = %{EVRD}
Provides: %{name}-windowsystem = %{EVRD}
Requires: %{_lib}qt5-output-driver-default
Group: System/Libraries

%description x11
X11 Window System support for KWin.

%package wayland
Summary: Wayland Window System support for KWin
Requires: %{name} = %{EVRD}
Provides: %{name}-windowsystem = %{EVRD}
Requires: kwayland-integration
Requires: %{_lib}qt5-output-driver-default
Requires: x11-server-xwayland
Requires(post): libcap-utils
Group: System/Libraries

%description wayland
Wayland Window System support for KWin.

%package -n %{effectname}
Summary: KWin effect library
Group: System/Libraries
Requires: %{name} = %{EVRD}
Obsoletes: %{mklibname keffects 7} < 5.6.0
Obsoletes: %{mklibname keffects 8} < 5.8.2

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
Obsoletes: %{mklibname kwinglutils 7} < 5.6.0
Obsoletes: %{mklibname kwinglutils 8} < 5.8.2

%description -n %{glutilsname}
KWin GL utils library.

%package -n %{xrenderutilsname}
Summary: KWin XRender utils library
Group: System/Libraries
Requires: %{name} = %{EVRD}
Obsoletes: %{mklibname kwinxrenderutils 7} < 5.6.0
Obsoletes: %{mklibname kwinxrenderutils 8} < 5.8.2

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

# (tpg) add missing symlinks
ln -s %{_datadir}/kservicetypes5/kwineffect.desktop %{buildroot}%{_datadir}/kservicetypes5/kwin-effect.desktop
ln -s %{_datadir}/kservicetypes5/kwinscript.desktop %{buildroot}%{_datadir}/kservicetypes5/kwin-script.desktop

%find_lang %{name} --all-name --with-html --with-man

%post wayland
%{_sbindir}/setcap "CAP_SYS_RESOURCE=+ep" %{_bindir}/kwin_wayland

%files -f %{name}.lang
%{_datadir}/kconf_update/kwin.upd
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
%{_libdir}/qt5/plugins/kpackage/*
%dir %{_libdir}/qt5/plugins/org.kde.kwin.platforms
%dir %{_libdir}/qt5/plugins/org.kde.kwin.scenes
%{_libdir}/qt5/plugins/kf5/org.kde.kidletime.platforms/KF5IdleTimeKWinWaylandPrivatePlugin.so
%{_libdir}/qt5/plugins/platforms/KWinQpaPlugin.so
%{_libdir}/qt5/plugins/org.kde.kwin.scenes/KWinSceneQPainter.so
%{_libdir}/qt5/plugins/org.kde.kwin.scenes/KWinSceneOpenGL.so
%{_libdir}/kconf_update_bin/kwin5_update_default_rules
%{_libdir}/libexec/kwin*
%{_libdir}/libexec/org_kde_kwin_xclipboard_syncer
%{_libdir}/libkdeinit5_kwin_rules_dialog.so
%{_datadir}/config.kcfg/kwin.kcfg
%{_datadir}/config.kcfg/kwin_colorcorrect.kcfg
%{_sysconfdir}/xdg/*

%files x11
%{_bindir}/kwin_x11
%{_libdir}/libkdeinit5_kwin_x11.so
%{_libdir}/qt5/plugins/org.kde.kwin.platforms/KWinX11Platform.so
%{_libdir}/qt5/plugins/org.kde.kwin.scenes/KWinSceneXRender.so

%files wayland
%{_bindir}/kwin_wayland
%{_libdir}/qt5/plugins/org.kde.kwin.waylandbackends

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
