%{!?directory:%define directory /usr}

%define buildroot %{_tmppath}/%{name}

Name:          mpexpr
Summary:       Multiple precision math for Tcl
Version:       1.2
Release:       0
License:       TCL
Group:         Development/Libraries/Tcl
Source:        mpexpr-1.2.tar.gz
Patch0:        makefile.patch
URL:           http://core.tcl.tk/mpexpr
BuildRequires: autoconf
BuildRequires: make
BuildRequires: tcl-devel >= 7.6
Requires:      tcl >= 7.6
BuildRoot:     %{buildroot}

%description
Tcl extension (adding mpexpr and mpformat) that supports multiple
precision math for Tcl.

%prep
%setup -q -n %{name}-%{version}
%patch0

%build
cd unix
./configure \
	--prefix=%{directory} \
	--exec-prefix=%{directory} \
	--libdir=%{directory}/%{_lib}/tcl \
	--mandir=%{directory}/share/man \
%ifarch x86_64
	--enable-64bit=yes \
%endif
	--with-tcl=%{directory}/%{_lib}
make 

%install
cd unix
make DESTDIR=%{buildroot} install

%clean
rm -rf %buildroot

%files
%doc LICENSE.TERMS README
%defattr(-,root,root)
%{directory}/%{_lib}/tcl
/usr/share/man/mann
/usr/bin/mpksc
