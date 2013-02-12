%define baseline 0.9
%define apiversion 0.8
%define suffix 2_1


Name:           libgee
Version:        0.9.0
Release:        0
Summary:        GObject-based library providing commonly used data structures
License:        LGPL-2.1+
Group:          Development/Libraries
Url:            http://live.gnome.org/Libgee
Source:         http://download.gnome.org/sources/libgee/%{baseline}/%{name}-%{version}.tar.xz

BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  vala
BuildRequires:  gnome-common


%description
Libgee is a collection library providing GObject-based interfaces and
classes for commonly used data structures.


%package -n typelib-Gee%{suffix}
Summary:        GObject-based library providing common data structures -- Introspection binding
Group:          System/Libraries

%description -n typelib-Gee%{suffix}
Libgee is a collection library providing GObject-based interfaces and
classes for commonly used data structures.

This package provides the GObject Introspection bindings for libgee.


%package -n libgee%{suffix}-devel
Summary:        GObject-based library providing useful data structures - Development Files
Group:          Development/Libraries
Requires:       libgee%{suffix} = %{version}
Requires:       typelib-Gee%{suffix} = %{version}

%description -n libgee%{suffix}-devel
Libgee is a collection library providing GObject-based interfaces and
classes for commonly used data structures.

%prep
%setup -q
touch ChangeLog

%build
%autogen
%reconfigure --disable-static

make %{?jobs:-j%jobs}

%install
%make_install

%post  -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-, root, root)
%license COPYING
%{_libdir}/*.so.*


%files -n typelib-Gee%{suffix}
%defattr(-,root,root)
%{_libdir}/girepository-1.0/Gee-%{apiversion}.typelib


%files -n libgee%{suffix}-devel
%defattr(-, root, root)
%{_includedir}/gee-%{apiversion}/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/*.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/*.vapi

