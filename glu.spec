%define major 1
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d
%global optflags %{optflags} -O3

# glu is used by freeglut, freeglut is used by wine
%ifarch %{x86_64}
%bcond_without compat32
%else
%bcond_with compat32
%endif
%define lib32name lib%{name}%{major}
%define dev32name lib%{name}-devel

Name:		glu
Version:	9.0.1
Release:	3
Summary:	Mesa libGLU library
Group:		System/Libraries
License:	MIT
Url:		http://mesa3d.org/
Source0:	https://mesa.freedesktop.org/archive/glu/%{name}-%{version}.tar.xz
Source2:	make-git-snapshot.sh

BuildRequires:	libtool
BuildRequires:	pkgconfig(gl)
%if %{with compat32}
BuildRequires:	devel(libGL)
%endif

%description
Mesa implementation of the standard GLU OpenGL utility API.

%package -n	%{libname}
Summary:	Files for Mesa (GLU libs)
Group:		System/Libraries
Provides:	libmesaglu = %{version}-%{release}
# Fix installing apps like Google Earth by providing mesa-libGLU (angry)
Provides:	mesa-libGLU = %{version}-%{release}
Provides:	mesa-libglu = %{version}-%{release}
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

%if %{with compat32}
%package -n	%{lib32name}
Summary:	Files for Mesa (GLU libs) (32-bit)
Group:		System/Libraries

%description -n	%{lib32name}
GLU is the OpenGL Utility Library.
It provides a number of functions upon the base OpenGL library to provide
higher-level drawing routines from the more primitive routines provided by
OpenGL.

%package -n	%{dev32name}
Summary:	Development files for GLU libs (32-bit)
Group:		Development/C
Requires:	%{devname} = %{version}-%{release}
Requires:	%{lib32name} = %{version}-%{release}

%description -n	%{dev32name}
This package contains the headers needed to compile programs with GLU.
%endif

%prep
%autosetup -p1
export CONFIGURE_TOP="$(pwd)"
%if %{with compat32}
mkdir build32
cd build32
%configure32
cd ..
%endif
mkdir build
cd build
%configure

%build
%if %{with compat32}
%make_build -C build32
%endif
%make_build -C build

%install
%if %{with compat32}
%make_install -C build32
%endif
%make_install -C build
rm -rf %{buildroot}%{_datadir}/man/man3/gl[A-Z]*

%files -n %{libname}
%{_libdir}/libGLU.so.%{major}*

%files -n %{devname}
%{_includedir}/GL/glu.h
%{_includedir}/GL/glu_mangle.h
%{_libdir}/libGLU.so
%{_libdir}/pkgconfig/glu.pc

%if %{with compat32}
%files -n %{lib32name}
%{_prefix}/lib/libGLU.so.%{major}*

%files -n %{dev32name}
%{_prefix}/lib/libGLU.so
%{_prefix}/lib/pkgconfig/glu.pc
%endif
