#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : elfutils
Version  : 0.186
Release  : 515
URL      : file:///aot/build/clearlinux/packages/elfutils/elfutils-v0.186.tar.gz
Source0  : file:///aot/build/clearlinux/packages/elfutils/elfutils-v0.186.tar.gz
Summary  : elfutils libelf library to read and write ELF files
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+ GPL-3.0 GPL-3.0+ LGPL-3.0+
Requires: elfutils-bin = %{version}-%{release}
Requires: elfutils-lib = %{version}-%{release}
Requires: elfutils-locales = %{version}-%{release}
Requires: elfutils-man = %{version}-%{release}
BuildRequires : binutils-dev
BuildRequires : bison
BuildRequires : buildreq-cmake
BuildRequires : bzip2
BuildRequires : bzip2-bin
BuildRequires : bzip2-dev
BuildRequires : bzip2-staticdev
BuildRequires : curl
BuildRequires : curl-dev
BuildRequires : doxygen
BuildRequires : flex
BuildRequires : flex-dev
BuildRequires : gcc
BuildRequires : gcc-dev
BuildRequires : gcc-dev32
BuildRequires : gcc-doc
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libs-math
BuildRequires : gcc-libstdc++32
BuildRequires : gcc-libubsan
BuildRequires : gcc-locale
BuildRequires : gettext
BuildRequires : glibc-dev
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : glibc-staticdev
BuildRequires : iproute2
BuildRequires : libarchive
BuildRequires : libarchive-dev
BuildRequires : libedit
BuildRequires : libedit-dev
BuildRequires : libffi-dev
BuildRequires : libffi-staticdev
BuildRequires : libgcc1
BuildRequires : libstdc++
BuildRequires : libxml2-dev
BuildRequires : libxml2-staticdev
BuildRequires : lz4-dev
BuildRequires : lz4-staticdev
BuildRequires : lzo-dev
BuildRequires : lzo-staticdev
BuildRequires : pkg-config
BuildRequires : pkgconfig(32libcurl)
BuildRequires : pkgconfig(libcurl)
BuildRequires : procps-ng
BuildRequires : python3-dev
BuildRequires : python3-staticdev
BuildRequires : sqlite-autoconf
BuildRequires : sqlite-autoconf-dev
BuildRequires : util-linux
BuildRequires : util-linux-dev
BuildRequires : xz-dev
BuildRequires : xz-dev32
BuildRequires : xz-devel
BuildRequires : xz-staticdev
BuildRequires : zlib-dev
BuildRequires : zlib-dev32
BuildRequires : zlib-staticdev
BuildRequires : zstd-dev
BuildRequires : zstd-staticdev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
The elfutils project provides libraries and tools for ELF files and DWARF data.
The project home is http://elfutils.org/

%package bin
Summary: bin components for the elfutils package.
Group: Binaries

%description bin
bin components for the elfutils package.


%package dev
Summary: dev components for the elfutils package.
Group: Development
Requires: elfutils-lib = %{version}-%{release}
Requires: elfutils-bin = %{version}-%{release}
Provides: elfutils-devel = %{version}-%{release}
Requires: elfutils = %{version}-%{release}

%description dev
dev components for the elfutils package.


%package dev32
Summary: dev32 components for the elfutils package.
Group: Default
Requires: elfutils-lib32 = %{version}-%{release}
Requires: elfutils-bin = %{version}-%{release}
Requires: elfutils-dev = %{version}-%{release}

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


%package man
Summary: man components for the elfutils package.
Group: Default

%description man
man components for the elfutils package.


%package staticdev
Summary: staticdev components for the elfutils package.
Group: Default
Requires: elfutils-dev = %{version}-%{release}

%description staticdev
staticdev components for the elfutils package.


%package staticdev32
Summary: staticdev32 components for the elfutils package.
Group: Default
Requires: elfutils-dev32 = %{version}-%{release}

%description staticdev32
staticdev32 components for the elfutils package.


%prep
%setup -q -n elfutils
cd %{_builddir}/elfutils
pushd %{_builddir}
cp -a %{_builddir}/elfutils build32
popd

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1639525987
unset LD_AS_NEEDED
export GCC_IGNORE_WERROR=1
## altflags1f content
## altflags1
unset ASFLAGS
export CFLAGS="-fdata-sections -ffunction-sections -g -Ofast -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -fno-lto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
export ASMFLAGS="-fdata-sections -ffunction-sections -g -Ofast -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -fno-lto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
export CXXFLAGS="-fdata-sections -ffunction-sections -g -Ofast -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -fno-lto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
export FCFLAGS="-fdata-sections -ffunction-sections -g -Ofast -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -fno-lto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
export FFLAGS="-fdata-sections -ffunction-sections -g -Ofast -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -fno-lto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
export CFFLAGS="-fdata-sections -ffunction-sections -g -Ofast -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -fno-lto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
export LDFLAGS="-fdata-sections -ffunction-sections -g -Ofast -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -fno-lto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
#
export MAKEFLAGS=%{?_smp_mflags}
#
%global _lto_cflags 1
#global _lto_cflags %{nil}
%global _disable_maintainer_mode 1
#%global _disable_maintainer_mode %{nil}
#
export CCACHE_DISABLE=true
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
#export CCACHE_SLOPPINESS=modules,include_file_mtime,include_file_ctime,time_macros,pch_defines,file_stat_matches,clang_index_store,system_headers,locale
#export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,clang_index_store,file_macro
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
#export CCACHE_LOGFILE=/var/tmp/ccache/cache.debug
#export CCACHE_DEBUG=true
#export CCACHE_NODIRECT=true
#
export PKG_CONFIG_PATH="/usr/lib64/pkgconfig:/usr/share/pkgconfig"
#
export LD_LIBRARY_PATH="/usr/nvidia/lib64:/usr/nvidia/lib64/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/haswell/pulseaudio:/usr/lib64/haswell/alsa-lib:/usr/lib64/haswell/gstreamer-1.0:/usr/lib64/haswell/pipewire-0.3:/usr/lib64/haswell/spa-0.2:/usr/lib64/dri:/usr/lib64/chromium:/usr/lib64:/usr/lib64/pulseaudio:/usr/lib64/alsa-lib:/usr/lib64/gstreamer-1.0:/usr/lib64/pipewire-0.3:/usr/lib64/spa-0.2:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/nvidia/lib32:/usr/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
#
export LIBRARY_PATH="/usr/nvidia/lib64:/usr/nvidia/lib64/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/haswell/pulseaudio:/usr/lib64/haswell/alsa-lib:/usr/lib64/haswell/gstreamer-1.0:/usr/lib64/haswell/pipewire-0.3:/usr/lib64/haswell/spa-0.2:/usr/lib64/dri:/usr/lib64/chromium:/usr/lib64:/usr/lib64/pulseaudio:/usr/lib64/alsa-lib:/usr/lib64/gstreamer-1.0:/usr/lib64/pipewire-0.3:/usr/lib64/spa-0.2:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/nvidia/lib32:/usr/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
#
export PATH="/usr/lib64/ccache/bin:/usr/local/cuda/bin:/usr/nvidia/bin:/usr/bin/haswell:/usr/bin:/usr/sbin"
#
export CPATH="/usr/local/cuda/include"
#
export DISPLAY=:0
export __GL_SYNC_TO_VBLANK=1
export __GL_SYNC_DISPLAY_DEVICE=HDMI-0
export VDPAU_NVIDIA_SYNC_DISPLAY_DEVICE=HDMI-0
export LANG=en_US.UTF-8
export XDG_CONFIG_DIRS=/usr/share/xdg:/etc/xdg
export XDG_SEAT=seat0
export XDG_SESSION_TYPE=tty
export XDG_CURRENT_DESKTOP=KDE
export XDG_SESSION_CLASS=user
export XDG_VTNR=1
export XDG_SESSION_ID=1
export XDG_RUNTIME_DIR=/run/user/1000
export XDG_DATA_DIRS=/usr/local/share:/usr/share
export KDE_SESSION_VERSION=5
export KDE_SESSION_UID=1000
export KDE_FULL_SESSION=true
export KDE_APPLICATIONS_AS_SCOPE=1
export VDPAU_DRIVER=nvidia
export LIBVA_DRIVER_NAME=vdpau
export LIBVA_DRIVERS_PATH=/usr/lib64/dri
export GTK_RC_FILES=/etc/gtk/gtkrc
export FONTCONFIG_PATH=/usr/share/defaults/fonts
## altflags1f end
sd -r '\s--dirty\s' ' ' .
sd -r 'git describe' 'git describe --abbrev=0' .
%reconfigure  --enable-static \
--enable-shared \
--program-prefix=eu- \
--with-zlib \
--with-lzma \
--with-zstd \
--disable-debuginfod \
--disable-libdebuginfod \
--enable-maintainer-mode \
--enable-install-elfh
## make_prepend64 content
# find . -type f -name 'Makefile' -exec sed -i 's:-lbz2\b:-Wl,--whole-archive,/usr/lib64/libbz2.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
# find . -type f -name 'Makefile' -exec sed -i 's:-lz\b:-Wl,--whole-archive,/usr/lib64/libz.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
# find . -type f -name 'Makefile' -exec sed -i 's:-llzma\b:-Wl,--whole-archive,/usr/lib64/liblzma.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
# find . -type f -name 'Makefile' -exec sed -i 's:-lzstd\b:-Wl,--whole-archive,/usr/lib64/libzstd.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
# find . -type f -name 'Makefile' -exec sed -i 's:-lacl\b:-Wl,--whole-archive,/usr/lib64/libacl.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
# find . -type f -name 'Makefile' -exec sed -i 's:-llz4\b:-Wl,--whole-archive,/usr/lib64/liblz4.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
# find . -type f -name 'Makefile' -exec sed -i 's:-llzo2\b:-Wl,--whole-archive,/usr/lib64/liblzo2.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
# find . -type f -name 'Makefile' -exec sed -i 's:-lxml2\b:-Wl,--whole-archive,/usr/lib64/libxml2.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
# find . -type f -name 'Makefile' -exec sed -i 's:-lexpat\b:-Wl,--whole-archive,/usr/lib64/libexpat.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
# find . -type f -name 'Makefile' -exec sed -i 's:-lcrypto\b:-Wl,--whole-archive,/usr/lib64/libcrypto.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
# find . -type f -name 'Makefile' -exec sed -i 's:-lssl\b:-Wl,--whole-archive,/usr/lib64/libssl.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
## make_prepend64 end
## make_macro content
make  %{?_smp_mflags}  V=1 VERBOSE=1  V=1 VERBOSE=1
make check -j1 V=1 VERBOSE=1
## make_macro end

pushd ../build32/
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
unset LD_LIBRARY_PATH
unset LIBRARY_PATH
unset CPATH
unset ASFLAGS
unset CFLAGS
unset CXXFLAGS
unset FCFLAGS
unset FFLAGS
unset CFFLAGS
unset LDFLAGS
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
export ASFLAGS="--32"
export CFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -pipe -fPIC -march=native -mtune=native -m32 -mstackrealign"
export ASMFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -pipe -fPIC -march=native -mtune=native -m32 -mstackrealign"
export CXXFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -fvisibility-inlines-hidden -pipe -fPIC -march=native -mtune=native -m32 -mstackrealign"
export FCFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -fvisibility-inlines-hidden -pipe -fPIC -march=native -mtune=native -m32 -mstackrealign"
export FFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -fvisibility-inlines-hidden -pipe -fPIC -march=native -mtune=native -m32 -mstackrealign"
export CFFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -fvisibility-inlines-hidden -pipe -fPIC -march=native -mtune=native -m32 -mstackrealign"
export LDFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -pipe -fPIC -march=native -mtune=native -m32 -mstackrealign"
%reconfigure  --program-prefix=eu- \
--with-zlib \
--with-lzma \
--without-bzlib \
--disable-debuginfod \
--disable-libdebuginfod \
--libdir=/usr/lib32 \
--build=i686-generic-linux-gnu \
--host=i686-generic-linux-gnu \
--target=i686-clr-linux-gnu \
--enable-maintainer-mode --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}  V=1 VERBOSE=1  V=1 VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1639525987
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
    pushd %{buildroot}/usr/lib32/pkgconfig
    for i in *.pc ; do ln -s $i 32$i ; done
    popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install
%find_lang elfutils
## Remove excluded files
rm -f %{buildroot}*/usr/bin/addr2line
rm -f %{buildroot}*/usr/bin/ar
rm -f %{buildroot}*/usr/bin/ld
rm -f %{buildroot}*/usr/bin/nm
rm -f %{buildroot}*/usr/bin/objdump
rm -f %{buildroot}*/usr/bin/ranlib
rm -f %{buildroot}*/usr/bin/readelf
rm -f %{buildroot}*/usr/bin/size
rm -f %{buildroot}*/usr/bin/stack
rm -f %{buildroot}*/usr/bin/strings
rm -f %{buildroot}*/usr/bin/strip
rm -f %{buildroot}*/usr/lib64/pkgconfig/libdebuginfod.pc
rm -f %{buildroot}*/usr/lib32/pkgconfig/32libdebuginfod.pc
rm -f %{buildroot}*/usr/lib32/pkgconfig/libdebuginfod.pc

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/eu-addr2line
/usr/bin/eu-ar
/usr/bin/eu-elfclassify
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
/usr/include/dwarf.h
/usr/include/elf.h
/usr/include/elfutils/elf-knowledge.h
/usr/include/elfutils/known-dwarf.h
/usr/include/elfutils/libasm.h
/usr/include/elfutils/libdw.h
/usr/include/elfutils/libdwelf.h
/usr/include/elfutils/libdwfl.h
/usr/include/elfutils/version.h
/usr/include/gelf.h
/usr/include/libelf.h
/usr/include/nlist.h
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
/usr/lib64/libasm-0.186.so
/usr/lib64/libasm.so.1
/usr/lib64/libdw-0.186.so
/usr/lib64/libdw.so.1
/usr/lib64/libelf-0.186.so
/usr/lib64/libelf.so.1

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libasm-0.186.so
/usr/lib32/libasm.so.1
/usr/lib32/libdw-0.186.so
/usr/lib32/libdw.so.1
/usr/lib32/libelf-0.186.so
/usr/lib32/libelf.so.1

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/eu-elfclassify.1
/usr/share/man/man1/eu-readelf.1
/usr/share/man/man3/elf_begin.3
/usr/share/man/man3/elf_clone.3
/usr/share/man/man3/elf_getdata.3
/usr/share/man/man3/elf_update.3

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libasm.a
/usr/lib64/libdw.a
/usr/lib64/libelf.a

%files staticdev32
%defattr(-,root,root,-)
/usr/lib32/libasm.a
/usr/lib32/libdw.a
/usr/lib32/libelf.a

%files locales -f elfutils.lang
%defattr(-,root,root,-)
