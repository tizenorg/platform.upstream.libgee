Name:           libgee
Version:        0.6.7
Release:        0
Summary:        GObject-based library providing commonly used data structures
License:        LGPL-2.1+
Group:          Development/Libraries/GNOME
Url:            http://live.gnome.org/Libgee
Source:         http://download.gnome.org/sources/libgee/0.6/%{name}-%{version}.tar.xz

BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  vala
BuildRequires:  gnome-common

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Libgee is a collection library providing GObject-based interfaces and
classes for commonly used data structures.


%package -n typelib-Gee
Summary:        GObject-based library providing commonly used data structures -- Introspection bindings
Group:          System/Libraries

%description -n typelib-Gee
Libgee is a collection library providing GObject-based interfaces and
classes for commonly used data structures.

This package provides the GObject Introspection bindings for libgee.

%package -n libgee-devel
Summary:        GObject-based library providing useful data structures - Development Files
Group:          Development/Libraries/GNOME
Requires:       libgee = %{version}
Requires:       typelib-Gee = %{version}

%description -n libgee-devel
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
%doc COPYING
%{_libdir}/*.so.*

%files -n typelib-Gee
%defattr(-,root,root)
%{_libdir}/girepository-1.0/Gee-1.0.typelib

%files -n libgee-devel
%defattr(-, root, root)
%{_includedir}/gee-1.0/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/*.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/*.vapi
