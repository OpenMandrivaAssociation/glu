%define major 1
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Name:		glu
Version:	9.0.0
Release:	15
Summary:	Mesa libGLU library
Group:		System/Libraries
License:	MIT
Url:		http://mesa3d.org/
# snapshot only at this point
Source0:	ftp://ftp.freedesktop.org/pub/mesa/glu/%{name}-%{version}.tar.bz2
Source2:	make-git-snapshot.sh

BuildRequires:	libtool
BuildRequires:	pkgconfig(gl)

%description
Mesa implementation of the standard GLU OpenGL utility API.

%package -n	%{libname}
Summary:	Files for Mesa (GLU libs)
Group:		System/Libraries
Provides:	libmesaglu = %{version}-%{release}
Obsoletes:	%{_lib}mesaglu1 < 9.0

%description -n	%{libname}
GLU is the OpenGL Utility Library.
It provides a number of functions upon the base OpenGL library to provide
higher-level drawing routines from the more primitive routines provided by
OpenGL.

%package -n	%{devname}
Summary:	Development files for GLU libs
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}mesaglu1-devel < 9.0

%description -n	%{devname}
This package contains the headers needed to compile programs with GLU.

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std
rm -rf %{buildroot}%{_datadir}/man/man3/gl[A-Z]*

%files -n %{libname}
%{_libdir}/libGLU.so.%{major}*

%files -n %{devname}
%{_includedir}/GL/glu.h
%{_includedir}/GL/glu_mangle.h
%{_libdir}/libGLU.so
%{_libdir}/pkgconfig/glu.pc

