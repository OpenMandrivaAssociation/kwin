%define debug_package %{nil}

%define decorationsmajor 5
%define decorationsname %mklibname kdecorations %{decorationsmajor}
%define decorationsdname %mklibname kdecorations -d

%define effectmajor 1
%define effectname %mklibname kwin4_effect_builtins %{effectmajor}
%define effectdname %mklibname kwin4_effect_builtins -d

%define effectsmajor 5
%define effectsname %mklibname keffects %{effectsmajor}
%define effectsdname %mklibname keffects -d

%define glutilsmajor 5
%define glutilsname %mklibname kwinglutils %{glutilsmajor}
%define glutilsdname %mklibname kwinglutils -d

%define xrenderutilsmajor 5
%define xrenderutilsname %mklibname kwinxrenderutils %{xrenderutilsmajor}
%define xrenderutilsdname %mklibname kwinxrenderutils -d

Name: kwin
Version: 4.96.0
Release: 3
Source0: http://ftp5.gwdg.de/pub/linux/kde/unstable/frameworks/%{version}/%{name}-%{version}.tar.xz
Summary: The KWin window manager
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: qmake5
BuildRequires: extra-cmake-modules5
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(Qt5Multimedia)
BuildRequires: cmake(KF5)
BuildRequires: cmake(KF5)
BuildRequires: cmake(KF5Activities)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(OpenGL)
BuildRequires: cmake(OpenGLES)
BuildRequires: cmake(EGL)
BuildRequires: cmake(Wayland)
BuildRequires: cmake(XKB)
BuildRequires: cmake(XCB)
BuildRequires: cmake(XCB)
BuildRequires: cmake(Gettext)
BuildRequires: cmake(KF5NewStuff)
BuildRequires: cmake(KF5KCMUtils)
BuildRequires: cmake(KF5Crash)
BuildRequires: cmake(KF5Init)
BuildRequires: cmake(KF5Notifications)
BuildRequires: cmake(KF5Plasma)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-image)
BuildRequires: pkgconfig(xcb-icccm)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-cursor)
BuildRequires: pkgconfig(wayland-egl)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: ninja

%description
The KWin window manager

%package -n %{decorationsname}
Summary: KWin effect library
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{decorationsname}
KWin effect library

%package -n %{effectname}
Summary: KWin effect library
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{effectname}
KWin effect library

%package -n %{effectsname}
Summary: KWin effects library
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{effectsname}
KWin effects library

%package -n %{glutilsname}
Summary: KWin GL utils library
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{glutilsname}
KWin GL utils library

%package -n %{xrenderutilsname}
Summary: KWin XRender utils library
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{xrenderutilsname}
KWin XRender utils library

%package devel
Summary: Development files for the KDE Frameworks 5 Win library
Group: Development/KDE and Qt
Requires: %{decorationsname} = %{EVRD}
Requires: %{effectname} = %{EVRD}
Requires: %{effectsname} = %{EVRD}
Requires: %{glutilsname} = %{EVRD}
Requires: %{xrenderutilsname} = %{EVRD}
Provides: %{decorationsdname} = %{EVRD}
Provides: %{effectdname} = %{EVRD}
Provides: %{effectsdname} = %{EVRD}
Provides: %{glutilsdname} = %{EVRD}
Provides: %{xrenderutilsdname} = %{EVRD}

%description devel
Development files for the KDE Frameworks 5 Win library

%prep
%setup -q
%cmake -G Ninja

%build
ninja -C build

%install
DESTDIR="%{buildroot}" ninja -C build install %{?_smp_mflags}

%files
%{_bindir}/kwin
%{_datadir}/kwin
%{_datadir}/kwincompositing
%{_datadir}/kservices5/*
%{_datadir}/kservicetypes5/*
%{_datadir}/knotifications5/*
%{_datadir}/icons/*/*/*/*
%{_datadir}/dbus-1/*/*
%{_libdir}/qml/org/kde/kwin
%{_libdir}/plugins/kwin
%{_libdir}/plugins/kwincompositing.so
%{_libdir}/plugins/kcm_kwin*
%{_libdir}/kconf_update_bin/kwin5_update_default_rules
%{_libdir}/libexec/kwin*
%{_libdir}/libkdeinit5_kwin.so
%{_libdir}/libkdeinit5_kwin_rules_dialog.so
%{_datadir}/config.kcfg/kwin.kcfg
%{_sysconfdir}/xdg/*
%doc %{_docdir}/HTML/en/kcontrol/desktop
%doc %{_docdir}/HTML/en/kcontrol/kwin*
%doc %{_docdir}/HTML/en/kcontrol/windowbehaviour
%doc %{_docdir}/HTML/en/kcontrol/windowspecific

%files -n %{effectname}
%{_libdir}/libkwin4_effect_builtins.so.%{effectmajor}*

%files -n %{decorationsname}
%{_libdir}/libkdecorations.so.%{decorationsmajor}
%{_libdir}/libkdecorations.so.%{version}

%files -n %{effectsname}
%{_libdir}/libkwineffects.so.%{effectsmajor}
%{_libdir}/libkwineffects.so.%{version}

%files -n %{glutilsname}
%{_libdir}/libkwinglutils.so.%{glutilsmajor}
%{_libdir}/libkwinglutils.so.%{version}

%files -n %{xrenderutilsname}
%{_libdir}/libkwinxrenderutils.so.%{xrenderutilsmajor}
%{_libdir}/libkwinxrenderutils.so.%{version}

%files devel
%{_includedir}/*
%{_libdir}/libkwin4_effect_builtins.so
%{_libdir}/libkdecorations.so
%{_libdir}/libkwineffects.so
%{_libdir}/libkwinglutils.so
%{_libdir}/libkwinxrenderutils.so
%{_libdir}/cmake/KDecorations
%{_libdir}/cmake/KWinDBusInterface
