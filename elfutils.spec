#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x8370665B57816A6A (mjw@gnu.org)
#
Name     : elfutils
Version  : 0.170
Release  : 42
URL      : https://sourceware.org/elfutils/ftp/0.170/elfutils-0.170.tar.bz2
Source0  : https://sourceware.org/elfutils/ftp/0.170/elfutils-0.170.tar.bz2
Source99 : https://sourceware.org/elfutils/ftp/0.170/elfutils-0.170.tar.bz2.sig
Summary  : A collection of utilities and DSOs to handle ELF files and DWARF data
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+ GPL-3.0 GPL-3.0+ LGPL-3.0 LGPL-3.0+
Requires: elfutils-bin
Requires: elfutils-lib
Requires: elfutils-locales
BuildRequires : bison
BuildRequires : bzip2-dev
BuildRequires : flex
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : xz-dev
BuildRequires : xz-dev32
BuildRequires : zlib-dev
BuildRequires : zlib-dev32

%description
Elfutils is a collection of utilities, including stack (to show
backtraces), nm (for listing symbols from object files), size
(for listing the section sizes of an object or archive file),
strip (for discarding symbols), readelf (to see the raw ELF file
structures), elflint (to check for well-formed ELF files) and
elfcompress (to compress or decompress ELF sections).
Also included are helper libraries which implement DWARF, ELF,
and machine-specific ELF handling and process introspection.

%package bin
Summary: bin components for the elfutils package.
Group: Binaries

%description bin
bin components for the elfutils package.


%package dev
Summary: dev components for the elfutils package.
Group: Development
Requires: elfutils-lib
Requires: elfutils-bin
Provides: elfutils-devel

%description dev
dev components for the elfutils package.


%package dev32
Summary: dev32 components for the elfutils package.
Group: Default
Requires: elfutils-lib32
Requires: elfutils-bin
Requires: elfutils-dev

%description dev32
dev32 components for the elfutils package.


%package lib
Summary: lib components for the elfutils package.
Group: Libraries

%description lib
lib components for the elfutils package.


%package lib32
Summary: lib32 components for the elfutils package.
Group: Default

%description lib32
lib32 components for the elfutils package.


%package locales
Summary: locales components for the elfutils package.
Group: Default

%description locales
locales components for the elfutils package.


%prep
%setup -q -n elfutils-0.170
pushd ..
cp -a elfutils-0.170 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1502066455
export CFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition -fstack-protector-strong "
export FCFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition -fstack-protector-strong "
export FFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition -fstack-protector-strong "
export CXXFLAGS="$CXXFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition -fstack-protector-strong "
%configure --disable-static --program-prefix=eu- --with-lzma
make V=1  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure --disable-static --program-prefix=eu- --with-lzma   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make V=1  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1502066455
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install
%find_lang elfutils

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/eu-addr2line
/usr/bin/eu-ar
/usr/bin/eu-elfcmp
/usr/bin/eu-elfcompress
/usr/bin/eu-elflint
/usr/bin/eu-findtextrel
/usr/bin/eu-make-debug-archive
/usr/bin/eu-nm
/usr/bin/eu-objdump
/usr/bin/eu-ranlib
/usr/bin/eu-readelf
/usr/bin/eu-size
/usr/bin/eu-stack
/usr/bin/eu-strings
/usr/bin/eu-strip
/usr/bin/eu-unstrip

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/include/elfutils/elf-knowledge.h
/usr/include/elfutils/known-dwarf.h
/usr/include/elfutils/libasm.h
/usr/include/elfutils/libdw.h
/usr/include/elfutils/libdwelf.h
/usr/include/elfutils/libdwfl.h
/usr/include/elfutils/libebl.h
/usr/include/elfutils/version.h
/usr/lib64/libasm.so
/usr/lib64/libdw.so
/usr/lib64/libelf.so
/usr/lib64/pkgconfig/libdw.pc
/usr/lib64/pkgconfig/libelf.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libasm.so
/usr/lib32/libdw.so
/usr/lib32/libelf.so
/usr/lib32/pkgconfig/32libdw.pc
/usr/lib32/pkgconfig/32libelf.pc
/usr/lib32/pkgconfig/libdw.pc
/usr/lib32/pkgconfig/libelf.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/elfutils/libebl_aarch64-0.170.so
/usr/lib64/elfutils/libebl_aarch64.so
/usr/lib64/elfutils/libebl_alpha-0.170.so
/usr/lib64/elfutils/libebl_alpha.so
/usr/lib64/elfutils/libebl_arm-0.170.so
/usr/lib64/elfutils/libebl_arm.so
/usr/lib64/elfutils/libebl_bpf-0.170.so
/usr/lib64/elfutils/libebl_bpf.so
/usr/lib64/elfutils/libebl_i386-0.170.so
/usr/lib64/elfutils/libebl_i386.so
/usr/lib64/elfutils/libebl_ia64-0.170.so
/usr/lib64/elfutils/libebl_ia64.so
/usr/lib64/elfutils/libebl_m68k-0.170.so
/usr/lib64/elfutils/libebl_m68k.so
/usr/lib64/elfutils/libebl_ppc-0.170.so
/usr/lib64/elfutils/libebl_ppc.so
/usr/lib64/elfutils/libebl_ppc64-0.170.so
/usr/lib64/elfutils/libebl_ppc64.so
/usr/lib64/elfutils/libebl_s390-0.170.so
/usr/lib64/elfutils/libebl_s390.so
/usr/lib64/elfutils/libebl_sh-0.170.so
/usr/lib64/elfutils/libebl_sh.so
/usr/lib64/elfutils/libebl_sparc-0.170.so
/usr/lib64/elfutils/libebl_sparc.so
/usr/lib64/elfutils/libebl_tilegx-0.170.so
/usr/lib64/elfutils/libebl_tilegx.so
/usr/lib64/elfutils/libebl_x86_64-0.170.so
/usr/lib64/elfutils/libebl_x86_64.so
/usr/lib64/libasm-0.170.so
/usr/lib64/libasm.so.1
/usr/lib64/libdw-0.170.so
/usr/lib64/libdw.so.1
/usr/lib64/libelf-0.170.so
/usr/lib64/libelf.so.1

%files lib32
%defattr(-,root,root,-)
/usr/lib32/elfutils/libebl_aarch64-0.170.so
/usr/lib32/elfutils/libebl_aarch64.so
/usr/lib32/elfutils/libebl_alpha-0.170.so
/usr/lib32/elfutils/libebl_alpha.so
/usr/lib32/elfutils/libebl_arm-0.170.so
/usr/lib32/elfutils/libebl_arm.so
/usr/lib32/elfutils/libebl_bpf-0.170.so
/usr/lib32/elfutils/libebl_bpf.so
/usr/lib32/elfutils/libebl_i386-0.170.so
/usr/lib32/elfutils/libebl_i386.so
/usr/lib32/elfutils/libebl_ia64-0.170.so
/usr/lib32/elfutils/libebl_ia64.so
/usr/lib32/elfutils/libebl_m68k-0.170.so
/usr/lib32/elfutils/libebl_m68k.so
/usr/lib32/elfutils/libebl_ppc-0.170.so
/usr/lib32/elfutils/libebl_ppc.so
/usr/lib32/elfutils/libebl_ppc64-0.170.so
/usr/lib32/elfutils/libebl_ppc64.so
/usr/lib32/elfutils/libebl_s390-0.170.so
/usr/lib32/elfutils/libebl_s390.so
/usr/lib32/elfutils/libebl_sh-0.170.so
/usr/lib32/elfutils/libebl_sh.so
/usr/lib32/elfutils/libebl_sparc-0.170.so
/usr/lib32/elfutils/libebl_sparc.so
/usr/lib32/elfutils/libebl_tilegx-0.170.so
/usr/lib32/elfutils/libebl_tilegx.so
/usr/lib32/elfutils/libebl_x86_64-0.170.so
/usr/lib32/elfutils/libebl_x86_64.so
/usr/lib32/libasm-0.170.so
/usr/lib32/libasm.so.1
/usr/lib32/libdw-0.170.so
/usr/lib32/libdw.so.1
/usr/lib32/libelf-0.170.so
/usr/lib32/libelf.so.1

%files locales -f elfutils.lang
%defattr(-,root,root,-)

