#!/usr/bin/tclsh

set arch "x86_64"
set base "mpexpr-1.2"
set fileurl "https://sourceforge.net/projects/mpexpr/files/mpexpr/1.2/mpexpr-1.2.tar.gz/download"

set var [list wget $fileurl -O $base.tar.gz]
exec >@stdout 2>@stderr {*}$var

if {[file exists build]} {
    file delete -force build
}

file mkdir build/BUILD build/RPMS build/SOURCES build/SPECS build/SRPMS
file copy -force $base.tar.gz build/SOURCES
file copy -force makefile.patch build/SOURCES

set buildit [list rpmbuild --target $arch --define "_topdir [pwd]/build" -bb mpexpr.spec]
exec >@stdout 2>@stderr {*}$buildit

# Remove our source code
file delete $base.tar.gz
