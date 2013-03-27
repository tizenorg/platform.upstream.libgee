%define baseline 0.9
%define apiversion 0.8


Name:           libgee
Version:        0.10.0
Release:        0
Summary:        GObject-based library providing commonly used data structures
License:        LGPL-2.1+
Group:          System/Libraries
Url:            http://live.gnome.org/Libgee
Source:         http://download.gnome.org/sources/libgee/%{baseline}/%{name}-%{version}.tar.xz

BuildRequires:  gnome-common
BuildRequires:  vala
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)


Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
Libgee is a collection library providing GObject-based interfaces and
classes for commonly used data structures.


%package -n typelib-Gee
Summary:        GObject-based library providing common data structures -- Introspection binding
Group:          System/Libraries

%description -n typelib-Gee
Libgee is a collection library providing GObject-based interfaces and
classes for commonly used data structures.

This package provides the GObject Introspection bindings for libgee.


%package devel
Summary:        GObject-based library providing useful data structures - Development Files
Group:          Development/Libraries
Requires:       %{name} = %{version}
Requires:       typelib-Gee = %{version}

%description -n libgee-devel
Libgee is a collection library providing GObject-based interfaces and
classes for commonly used data structures.

%prep
%setup -q


%build

%autogen \
 --disable-static

make %{?jobs:-j%jobs}

%install
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-, root, root)
%license COPYING
%{_libdir}/*.so.*


%files -n typelib-Gee
%defattr(-,root,root)
%{_libdir}/girepository-1.0/Gee-%{apiversion}.typelib


%files devel
%defattr(-, root, root)
%{_includedir}/gee-%{apiversion}/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/*.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/*.vapi

