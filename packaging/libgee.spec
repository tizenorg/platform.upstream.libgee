%define baseline 0.9
%define apiversion 0.8
%define _suffix 2_1


Name:           libgee
Version:        0.9.0
Release:        0
Summary:        GObject-based library providing commonly used data structures
License:        LGPL-2.1+
Group:          Development/Libraries
Url:            http://live.gnome.org/Libgee
Source:         http://download.gnome.org/sources/libgee/%{baseline}/%{name}-%{version}.tar.xz

BuildRequires:  glib2-devel
BuildRequires:  gnome-common
BuildRequires:  gobject-introspection-devel
BuildRequires:  vala

%description
Libgee is a collection library providing GObject-based interfaces and
classes for commonly used data structures.


%package -n %{name}%{_suffix}
Summary:        GObject-based library providing common data structures -- Introspection binding
Group:          System/Libraries

Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description  -n %{name}%{_suffix}
Libgee is a collection library providing GObject-based interfaces and
classes for commonly used data structures.


%package -n typelib-Gee%{_suffix}
Summary:        GObject-based library providing common data structures -- Introspection binding
Group:          System/Libraries

%description -n typelib-Gee%{_suffix}
Libgee is a collection library providing GObject-based interfaces and
classes for commonly used data structures.

This package provides the GObject Introspection bindings for libgee.


%package -n libgee%{_suffix}-devel
Summary:        GObject-based library providing useful data structures - Development Files
Group:          Development/Libraries
Requires:       libgee%{_suffix} = %{version}
Requires:       typelib-Gee%{_suffix} = %{version}

%description -n libgee%{_suffix}-devel
Libgee is a collection library providing GObject-based interfaces and
classes for commonly used data structures.

%prep
%setup -q
touch ChangeLog

%build

%autogen \
 --disable-static

make %{?jobs:-j%jobs}

%install
%make_install

%post -n %{name}%{_suffix} -p /sbin/ldconfig

%postun -n %{name}%{_suffix} -p /sbin/ldconfig


%files -n %{name}%{_suffix}
%defattr(-, root, root)
%license COPYING
%{_libdir}/*.so.*


%files -n typelib-Gee%{_suffix}
%defattr(-,root,root)
%{_libdir}/girepository-1.0/Gee-%{apiversion}.typelib


%files -n libgee%{_suffix}-devel
%defattr(-, root, root)
%{_includedir}/gee-%{apiversion}/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/*.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/*.vapi

