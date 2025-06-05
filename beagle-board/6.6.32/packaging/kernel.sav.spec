# We have to override the new %%install behavior because, well... the kernel is special.
%global __spec_install_pre %{___build_pre}

# What parts do we want to build?  We must build at least one kernel.
# These are the kernels that are built IF the architecture allows it.
# All should default to 1 (enabled) and be flipped to 0 (disabled)
# by later arch-specific checks.

# The following build options are enabled by default.
# Use either --without <opt> in your rpmbuild command or force values
# to 0 in here to disable them.
#

# kernel-doc
%define with_doc       %{?_without_doc:       0} %{?!_without_doc:       1}
# kernel-headers
%define with_headers   %{?_without_headers:   0} %{?!_without_headers:   1}
%define with_cross_headers   %{?_without_cross_headers:   1} %{?!_without_cross_headers:   0}
# perf
%define with_perf   0
# tools
%define with_tools     %{?_without_tools:     1} %{?!_without_tools:     0}
# bpf tool
%define with_bpftool   %{?_without_bpftool:   0} %{?!_without_bpftool:   1}
# kernel-debuginfo
%define with_debuginfo %{?_without_debuginfo: 1} %{?!_without_debuginfo: 0}


#
# Additional options for user-friendly one-off kernel building:
#
# Only build the base kernel (--with baseonly):
%define with_baseonly   %{?_with_baseonly:    1} %{?!_with_baseonly:     0}
#
# Cross compile requested? Enabled by default
%define with_cross      %{?_without_cross:    0} %{?!_without_cross:     0}
#
# build a release kernel on rawhide
%define with_release    %{?_with_release:     1} %{?!_with_release:      0}

# Want to build a vanilla kernel build without any non-upstream patches?
%define with_vanilla    %{?_with_vanilla:     1} %{?!_with_vanilla:      0}

# Enable Large Physical Address Extension support
%define with_lpae       %{?_with_lpae:        1} %{?!_with_lpae:         0}

# verbose build, i.e. no silent rules and V=1
%define with_verbose %{?_with_verbose:        1} %{?!_with_verbose:      0}

# For a stable, released kernel, released_kernel should be 1. For rawhide
# and/or a kernel built from an rc or git snapshot, released_kernel should
# be 0.
%global released_kernel 1

# baserelease defines which build revision of this kernel version we're
# building.  We used to call this fedora_build, but the magical name
# baserelease is matched by the rpmdev-bumpspec tool, which you should use.
#
# We used to have some extra magic weirdness to bump this automatically,
# but now we don't.  Just use: rpmdev-bumpspec -c 'comment for changelog'
# When changing base_sublevel below or going from rc to a final kernel,
# reset this by hand to 1 (or to 0 and then use rpmdev-bumpspec).
# scripts/rebase.sh should be made to do that for you, actually.
#
# NOTE: baserelease must be > 0 or bad things will happen if you switch
#       to a released kernel (released version will be < rc version)
#
# For non-released -rc kernels, this will be appended after the rcX and
# gitX tags, so a 3 here would become part of release "0.rcX.gitX.3"
#
%global baserelease 1
%global cfg_release 1
%global cfg_tested 0
%global fedora_build %{baserelease}.%{cfg_release}.%{cfg_tested}

%global zipmodules 1

%if %{zipmodules}
%global zipsed -e 's/\.ko$/\.ko.xz/'
%endif

%if %{with_lpae}
%global variant -lpae
%global fedora_build %{baserelease}.lpae
%global with_tools 0
%global with_perf 0
%endif

%if %{with_verbose}
%define make_opts V=1
%else
%define make_opts -s
%endif

# base_sublevel is the kernel version we're starting with and patching
# on top of -- for example, 3.1-rc7-git1 starts with a 3.0 base,
# which yields a base_sublevel of 0.
%define kernel_release  6
%define base_sublevel   6

## If this is a released kernel ##
%if 0%{?released_kernel}

# Do we have a -stable update to apply?
%define stable_update 321

# Set rpm version accordingly
%if 0%{?stable_update}
%define stablerev   %{stable_update}
%define stable_base %{stable_update}
%endif

%define rpmversion  %{kernel_release}.%{base_sublevel}.%{stable_update}

## The not-released-kernel case ##
%else
# The next upstream release sublevel (base_sublevel+1)
%define upstream_sublevel %(echo $((%{base_sublevel} + 1)))
# The rc snapshot level
%define rcrev 0
# The git snapshot level
%define gitrev 0
# Set rpm version accordingly
%define rpmversion %{kernel_release}.%{upstream_sublevel}.0
%endif
# Nb: The above rcrev and gitrev values automagically define Source1 and Source2 below. #TODO: unneeded for Redpesk ?

# The kernel tarball/base version
%define kversion  %{kernel_release}.%{base_sublevel}
%define release_short %(echo %release | sed "s/redpesk\.//g")
%define KVERREL   %{version}-%{release_short}.%{_target_cpu}

%if 0%{!?nopatches:1}
%define nopatches 0
%endif

%if %{with_vanilla}
%define nopatches 1
%endif

%if %{nopatches}
%define variant -vanilla
%endif

%if !%{with_debuginfo}
%define _enable_debug_packages 0
%define debuginfodir /usr/lib/debug
# Needed because we override almost everything involving build-ids
# and debuginfo generation. Currently we rely on the old alldebug setting.
%global _build_id_links alldebug
%endif

# Kernel configuration
%define Flavour             AM62x
%define kernel_config       bb.org_defconfig
%define board_dtb           ti/k3-am625-beagleplay.dtb
%define asmarch             arm64
%define hdrarch             arm64
%define make_target         Image
%define kernel_image_name   Image
%define image_install_path  boot
%define kernel_mflags       KALLSYMS_EXTRA_PASS=1 # http://lists.infradead.org/pipermail/linux-arm-kernel/2012-March/091404.html

%define kernel_image        arch/%{asmarch}/boot/%{kernel_image_name}
%define buildid             .%{Flavour}
# pkg_release is what we'll fill in for the rpm Release: field
%define pkg_release         %{fedora_build}%{?dist}


# Overrides for generic default options

# only package docs noarch
%ifnarch noarch
%define with_doc 0
%define doc_build_fail true
%endif

# don't build noarch kernels or headers (duh)
%ifarch noarch
%define with_up 0
%define with_headers 0
%define with_cross_headers 0
%define with_tools 0
%define with_perf 0
%define with_bpftool 0
%define with_selftests 0
%define with_debug 0
%define all_arch_configs %{name}-%{version}-*.config
%endif


# Should make listnewconfig fail if there's config options
# printed out?
%if %{nopatches}
%define listnewconfig_fail 0
%else
%define listnewconfig_fail 1
%endif

%ifarch %nobuildarches
%define with_up 0
%define with_debug 0
%define with_debuginfo 0
%define with_perf 0
%define with_tools 0
%define with_bpftool 0
%define with_selftests 0
%define _enable_debug_packages 0
%endif

# Architectures we build tools/cpupower on
%define cpupowerarchs x86_64 aarch64


#
# Packages that need to be installed before the kernel is, because the %%post
# scripts use them.
#
%define kernel_prereq  coreutils, systemd
%define initrd_prereq  dracut


Name: kernel
Group: System Environment/Kernel
License: GPLv2 and Redistributable, no modification permitted
Summary: Kernel tree for generic ARM64 platforms adapted for Beagleplay
URL: https://github.com/beagleboard/linux.git
# https://docs.beagleboard.org/latest/boards/beagleplay/demos-and-tutorials/play-kernel-development.html
#Hexsha: ac0ddc64cced3bdaa8ba5aa56a9a3cdc01825744
Version: 6.6.32
Release: %{pkg_release}
Source0: %{name}-%{version}.tar.gz
ExclusiveArch: aarch64
Requires: kernel-core-uname-r = %{KVERREL}
Requires: kernel-modules-uname-r = %{KVERREL}

#
# List the packages used during the kernel build
#
BuildRequires: kmod, patch, bash, coreutils, tar, git, which
BuildRequires: bzip2, xz, findutils, gzip, m4, perl-interpreter, perl-Carp, perl-devel, perl-generators, make, diffutils, gawk
BuildRequires: gcc, binutils, redhat-rpm-config, hmaccalc, python3-devel
BuildRequires: net-tools, hostname, bc, bison, flex, elfutils-devel, dwarves
BuildRequires: openssl-devel
%if %{with_doc}
BuildRequires: xmlto, asciidoc, python3-sphinx
%endif
BuildRequires: redpesk-kernel-config > 0.2
%if %{with_headers}
BuildRequires: rsync
%endif
%if %{with_perf}
BuildRequires: zlib-devel binutils-devel newt-devel perl(ExtUtils::Embed) bison flex xz-devel
BuildRequires: audit-libs-devel
BuildRequires: java-devel
BuildRequires: libbpf-devel
BuildRequires: libbabeltrace-devel
BuildRequires: numactl-devel
%endif
%if %{with_tools}
BuildRequires: gettext ncurses-devel
BuildRequires: pciutils-devel
%endif
%if %{with_debuginfo}
BuildRequires: rpm-build, elfutils
BuildConflicts: rpm < 4.13.0.1-19
BuildConflicts: dwarves < 1.13
# Most of these should be enabled after more investigation
%undefine _include_minidebuginfo
%undefine _find_debuginfo_dwz_opts
%undefine _unique_build_ids
%undefine _unique_debug_names
%undefine _unique_debug_srcs
%undefine _debugsource_packages
%undefine _debuginfo_subpackages
%global _find_debuginfo_opts -r
%global _missing_build_ids_terminate_build 1
%global _no_recompute_build_ids 1
%endif

%if %{with_cross}
%define cross_opts CROSS_COMPILE=%{_build_arch}-linux-gnu-
%endif

# These below are required to build man pages
%if %{with_perf}
BuildRequires: xmlto
%endif
%if %{with_perf} || %{with_tools}
BuildRequires: asciidoc
%endif

BuildRequires: libpfm-devel
BuildRequires: libtraceevent-devel

# Kernel modules modifications
Source16: mod-extra.list
Source17: mod-extra.sh
Source90: filter-x86_64.sh
Source93: filter-aarch64.sh
Source94: filter-armv7hl.sh
Source99: filter-modules.sh
Source100: filter-ti-AM62x.sh

# Kernel config modifications
Source1000: config-custom.cfg

%define with_optimization  1
%if 0%{with_optimization}
Source1001: 01-unnecessary-protocols.cfg
Source1002: 02-wireless.cfg
Source1003: 03-bluetooth.cfg
Source1004: 04-filesystems.cfg
Source1005: 05-graphics.cfg
Source1006: 06-multimedia.cfg
Source1007: 07-input-devices.cfg
Source1008: 08-storage.cfg
Source1009: 09-sound.cfg
Source1010: 10-power-management.cfg
Source1011: 11-power-supply-and-battery.cfg
Source1012: 12-legacy-hardware.cfg
Source1013: 13-LED-and-GPIO-drivers.cfg
Source1014: 14-Real-Time-Clock.cfg
Source1015: 15-sensors-and-monitoring.cfg
Source1016: 16-debugging-features.cfg
Source1017: 17-special-hardware-devices.cfg
Source1018: 18-virtualization-and-emulation.cfg
Source1019: 19-cryptographic-and-security-features.cfg
Source1020: 20-special-subsystems.cfg
Source1021: 21-USB-devices.cfg
Source1022: 22-kernel-subsystems.cfg
Source1023: 23-miscellaneous.cfg
Source1024: 24-general-setup.cfg
Source1025: 25-Processor-type-and-features.cfg
Source1026: 26-Power-management-and-ACPI-options.cfg
Source1027: 27-other-stuff.cfg
Source1028: 30-File-systems.cfg
Source1029: 33-posix-mqueue.cfg
Source1030: 34-remove-EFI.cfg
Source1031: 130-not-to-remove-cryptographic.cfg
Source1032: 29-remove-debug-feature.cfg
Source1033: 132-not-to-remove-Device-Drivers.cfg

Source1101: 132-not-to-remove-Device-Drivers-1.cfg
Source1102: 132-not-to-remove-Device-Drivers-2.cfg
Source1103: 132-not-to-remove-Device-Drivers-3.cfg
Source1104: 132-not-to-remove-Device-Drivers-4.cfg
Source1105: 132-not-to-remove-Device-Drivers-5.cfg
Source1106: 132-not-to-remove-Device-Drivers-6.cfg
Source1107: 132-not-to-remove-Device-Drivers-7.cfg
Source1108: 132-not-to-remove-Device-Drivers-8.cfg
Source1109: 129-not-to-remove-debug-feature.cfg
Source1110: 129-not-to-remove-debug-feature-0.cfg
Source1111: 129-not-to-remove-debug-feature-1.cfg
Source1112: 129-not-to-remove-debug-feature-2.cfg
Source1113: 129-not-to-remove-debug-feature-3.cfg
Source1114: 129-not-to-remove-debug-feature-4.cfg
#Source1108: 28-totest.cfg
Source1115: 28.0-totest.cfg
Source1116: 28.1-totest.cfg
Source1117: 28.2-totest.cfg
Source1118: 28.3-totest.cfg
Source1119: 28.4-totest.cfg
Source1120: 28.5-totest.cfg

%endif


# Sources for kernel-tools
Source2000: cpupower.service
Source2001: cpupower.config

# Patches
Patch1:    0001-dts-beagleplay-enable-m4f-support.patch
Patch2:    0002-Add-phandle-for-cortex-M4F-init.patch

BuildRoot: %{_tmppath}/%{name}-%{KVERREL}-root

%description
The kernel meta package

#
# This macro does requires, provides, conflicts, obsoletes for a kernel package.
#	%%kernel_reqprovconf <subpackage>
# It uses any kernel_<subpackage>_conflicts and kernel_<subpackage>_obsoletes
# macros defined above.
#
%define kernel_reqprovconf \
Provides: %{name} = %{rpmversion}-%{pkg_release}\
Provides: %{name}-%{_target_cpu} = %{rpmversion}-%{pkg_release}%{?1:+%{1}}\
Provides: kernel-drm-nouveau = 16\
Provides: %{name}-uname-r = %{KVERREL}%{?variant}%{?1:+%{1}}\
Requires(pre): %{kernel_prereq}\
Requires(pre): linux-firmware >= 20200619-99.git3890db36\
Requires(preun): systemd >= 200\
Conflicts: xfsprogs < 4.3.0-1\
Conflicts: xorg-x11-drv-vmmouse < 13.0.99\
Conflicts: kexec-tools < 2.0.20-8\
%{expand:%%{?kernel%{?1:_%{1}}_conflicts:Conflicts: %%{kernel%{?1:_%{1}}_conflicts}}}\
%{expand:%%{?kernel%{?1:_%{1}}_obsoletes:Obsoletes: %%{kernel%{?1:_%{1}}_obsoletes}}}\
%{expand:%%{?kernel%{?1:_%{1}}_provides:Provides: %%{kernel%{?1:_%{1}}_provides}}}\
# We can't let RPM do the dependencies automatic because it'll then pick up\
# a correct but undesirable perl dependency from the module headers which\
# isn't required for the kernel proper to function\
AutoReq: no\
AutoProv: yes\
%{nil}


%package doc
Summary: Various documentation bits found in the kernel source
Group: Documentation
%description doc
This package contains documentation files from the kernel
source. Various bits of information about the Linux kernel and the
device drivers shipped with it are documented in these files.

You'll want to install this package if you need a reference to the
options that can be passed to Linux kernel modules at load time.


%package headers
Summary: Header files for the Linux kernel for use by glibc
Group: Development/System
Obsoletes: glibc-kernheaders < 3.0-46
Provides: glibc-kernheaders = 3.0-46
%if "0%{?variant}"
Obsoletes: kernel-headers < %{rpmversion}-%{pkg_release}
Provides: kernel-headers = %{rpmversion}-%{pkg_release}
%endif
%description headers
Kernel-headers includes the C header files that specify the interface
between the Linux kernel and userspace libraries and programs.  The
header files define structures and constants that are needed for
building most standard programs and are also needed for rebuilding the
glibc package.

%package cross-headers
Summary: Header files for the Linux kernel for use by cross-glibc
Group: Development/System
%description cross-headers
Kernel-cross-headers includes the C header files that specify the interface
between the Linux kernel and userspace libraries and programs.  The
header files define structures and constants that are needed for
building most standard programs and are also needed for rebuilding the
cross-glibc package.


%package debuginfo-common-%{_target_cpu}
Summary: Kernel source files used by %{name}-debuginfo packages
Group: Development/Debug
Provides: installonlypkg(kernel)
%description debuginfo-common-%{_target_cpu}
This package is required by %{name}-debuginfo subpackages.
It provides the kernel source files common to all builds.

%if %{with_perf}
%package -n perf
Summary: Performance monitoring for the Linux kernel
Group: Development/System
Requires: bzip2
License: GPLv2
%description -n perf
This package contains the perf tool, which enables performance monitoring
of the Linux kernel.

%package -n perf-debuginfo
Summary: Debug information for package perf
Group: Development/Debug
Requires: %{name}-debuginfo-common-%{_target_cpu} = %{version}-%{release}
AutoReqProv: no
%description -n perf-debuginfo
This package provides debug information for the perf package.

# Note that this pattern only works right to match the .build-id
# symlinks because of the trailing nonmatching alternation and
# the leading .*, because of find-debuginfo.sh's buggy handling
# of matching the pattern against the symlinks file.
%{expand:%%global _find_debuginfo_opts %{?_find_debuginfo_opts} -p '.*%%{_bindir}/perf(\.debug)?|.*%%{_libexecdir}/perf-core/.*|.*%%{_libdir}/traceevent/plugins/.*|.*%%{_libdir}/libperf-jvmti.so(\.debug)?|XXX' -o perf-debuginfo.list}

%package -n python3-perf
Summary: Python bindings for apps which will manipulate perf events
Group: Development/Libraries
%description -n python3-perf
The python3-perf package contains a module that permits applications
written in the Python programming language to use the interface
to manipulate perf events.

%package -n python3-perf-debuginfo
Summary: Debug information for package perf python bindings
Group: Development/Debug
Requires: %{name}-debuginfo-common-%{_target_cpu} = %{version}-%{release}
AutoReqProv: no
%description -n python3-perf-debuginfo
This package provides debug information for the perf python bindings.

# the python_sitearch macro should already be defined from above
%{expand:%%global _find_debuginfo_opts %{?_find_debuginfo_opts} -p '.*%%{python3_sitearch}/perf.*so(\.debug)?|XXX' -o python3-perf-debuginfo.list}

# with_perf
%endif

%if %{with_tools}
%package -n %{name}-tools
Summary: Assortment of tools for the Linux kernel
Group: Development/System
License: GPLv2
%ifarch %{cpupowerarchs}
Provides:  cpupowerutils = 1:009-0.6.p1
Obsoletes: cpupowerutils < 1:009-0.6.p1
Provides:  cpufreq-utils = 1:009-0.6.p1
Provides:  cpufrequtils = 1:009-0.6.p1
Obsoletes: cpufreq-utils < 1:009-0.6.p1
Obsoletes: cpufrequtils < 1:009-0.6.p1
Obsoletes: cpuspeed < 1:1.5-16
Requires: %{name}-tools-libs = %{version}-%{release}
%endif
%define __requires_exclude ^%{_bindir}/python
%description -n %{name}-tools
This package contains the tools/ directory from the kernel source
and the supporting documentation.

%package -n %{name}-tools-libs
Summary: Libraries for the %{name}-tools
Group: Development/System
License: GPLv2
%description -n %{name}-tools-libs
This package contains the libraries built from the tools/ directory
from the kernel source.

%package -n %{name}-tools-libs-devel
Summary: Assortment of tools for the Linux kernel
Group: Development/System
License: GPLv2
Requires: %{name}-tools = %{version}-%{release}
%ifarch %{cpupowerarchs}
Provides:  cpupowerutils-devel = 1:009-0.6.p1
Obsoletes: cpupowerutils-devel < 1:009-0.6.p1
%endif
Requires: %{name}-tools-libs = %{version}-%{release}
Provides: %{name}-tools-devel
%description -n %{name}-tools-libs-devel
This package contains the development files for the tools/ directory from
the kernel source.

%package -n %{name}-tools-debuginfo
Summary: Debug information for package %{name}-tools
Group: Development/Debug
Requires: %{name}-debuginfo-common-%{_target_cpu} = %{version}-%{release}
AutoReqProv: no
%description -n %{name}-tools-debuginfo
This package provides debug information for package %{name}-tools.

# Note that this pattern only works right to match the .build-id
# symlinks because of the trailing nonmatching alternation and
# the leading .*, because of find-debuginfo.sh's buggy handling
# of matching the pattern against the symlinks file.
%{expand:%%global _find_debuginfo_opts %{?_find_debuginfo_opts} -p '.*%%{_bindir}/cpupower(\.debug)?|.*%%{_libdir}/libcpupower.*|.*%%{_bindir}/turbostat(\.debug)?|.*%%{_bindir}/tmon(\.debug)?|.*%%{_bindir}/lsgpio(\.debug)?|.*%%{_bindir}/gpio-hammer(\.debug)?|.*%%{_bindir}/gpio-event-mon(\.debug)?|.*%%{_bindir}/iio_event_monitor(\.debug)?|.*%%{_bindir}/iio_generic_buffer(\.debug)?|.*%%{_bindir}/lsiio(\.debug)?|XXX' -o kernel-tools-debuginfo.list}
%endif

#
# This macro creates a kernel-<subpackage>-debuginfo package.
#	%%kernel_debuginfo_package <subpackage>
#
%define kernel_debuginfo_package() \
%package %{?1:%{1}-}debuginfo\
Summary: Debug information for package %{name}%{?1:-%{1}}\
Group: Development/Debug\
Requires: %{name}-debuginfo-common-%{_target_cpu} = %{version}-%{release}\
Provides: %{name}%{?1:-%{1}}-debuginfo-%{_target_cpu} = %{version}-%{release}\
Provides: installonlypkg(kernel)\
AutoReqProv: no\
%description %{?1:%{1}-}debuginfo\
This package provides debug information for package %{name}%{?1:-%{1}}.\
This is required to use SystemTap with %{name}%{?1:-%{1}}-%{KVERREL}.\
%{expand:%%global _find_debuginfo_opts %{?_find_debuginfo_opts} -p '/.*/%%{KVERREL}%{?1:[+]%{1}}/.*|/.*%%{KVERREL}%{?1:\+%{1}}(\.debug)?' -o debuginfo%{?1}.list}\
%{nil}

#
# This macro creates a kernel-<subpackage>-devel package.
#	%%kernel_devel_package <subpackage> <pretty-name>
#
%define kernel_devel_package() \
%package %{?1:%{1}-}devel\
Summary: Development package for building kernel modules to match the %{?2:%{2} }kernel\
Group: System Environment/Kernel\
Provides: %{name}%{?1:-%{1}}-devel-%{_target_cpu} = %{version}-%{release}\
Provides: %{name}-devel-%{_target_cpu} = %{version}-%{release}%{?1:+%{1}}\
Provides: %{name}-devel-uname-r = %{KVERREL}%{?variant}%{?1:+%{1}}\
Provides: installonlypkg(kernel)\
AutoReqProv: no\
Requires(pre): findutils\
Requires: findutils\
Requires: perl-interpreter\
%description %{?1:%{1}-}devel\
This package provides kernel headers and makefiles sufficient to build modules\
against the %{?2:%{2} }kernel package.\
%{nil}

#
# This macro creates a kernel-<subpackage>-modules-extra package.
#	%%kernel_modules_extra_package <subpackage> <pretty-name>
#
%define kernel_modules_extra_package() \
%package %{?1:%{1}-}modules-extra\
Summary: Extra kernel modules to match the %{?2:%{2} }kernel\
Group: System Environment/Kernel\
Provides: %{name}%{?1:-%{1}}-modules-extra-%{_target_cpu} = %{version}-%{release}\
Provides: %{name}%{?1:-%{1}}-modules-extra-%{_target_cpu} = %{version}-%{release}%{?1:+%{1}}\
Provides: %{name}%{?1:-%{1}}-modules-extra = %{version}-%{release}%{?1:+%{1}}\
Provides: installonlypkg(kernel-module)\
Provides: %{name}%{?1:-%{1}}-modules-extra-uname-r = %{KVERREL}%{?variant}%{?1:+%{1}}\
Requires: %{name}-uname-r = %{KVERREL}%{?variant}%{?1:+%{1}}\
Requires: %{name}%{?1:-%{1}}-modules-uname-r = %{KVERREL}%{?variant}%{?1:+%{1}}\
AutoReq: no\
AutoProv: yes\
%description %{?1:%{1}-}modules-extra\
This package provides less commonly used kernel modules for the %{?2:%{2} }kernel package.\
%{nil}

#
# This macro creates a kernel-<subpackage>-modules package.
#	%%kernel_modules_package <subpackage> <pretty-name>
#
%define kernel_modules_package() \
%package %{?1:%{1}-}modules\
Summary: kernel modules to match the %{?2:%{2}-}core kernel\
Group: System Environment/Kernel\
Provides: %{name}%{?1:-%{1}}-modules-%{_target_cpu} = %{version}-%{release}\
Provides: %{name}-modules-%{_target_cpu} = %{version}-%{release}%{?1:+%{1}}\
Provides: %{name}-modules = %{version}-%{release}%{?1:+%{1}}\
Provides: installonlypkg(kernel-module)\
Provides: %{name}%{?1:-%{1}}-modules-uname-r = %{KVERREL}%{?variant}%{?1:+%{1}}\
Requires: %{name}-uname-r = %{KVERREL}%{?variant}%{?1:+%{1}}\
AutoReq: no\
AutoProv: yes\
%description %{?1:%{1}-}modules\
This package provides commonly used kernel modules for the %{?2:%{2}-}core kernel package.\
%{nil}

#
# this macro creates a kernel-<subpackage> meta package.
#	%%kernel_meta_package <subpackage>
#
%define kernel_meta_package() \
%package %{1}\
summary: kernel meta-package for the %{1} kernel\
group: system environment/kernel\
Requires: %{name}-%{1}-core-uname-r = %{KVERREL}%{?variant}+%{1}\
Requires: %{name}-%{1}-modules-uname-r = %{KVERREL}%{?variant}+%{1}\
Provides: installonlypkg(kernel)\
%description %{1}\
The meta-package for the %{1} kernel\
%{nil}

#
# This macro creates a %%{name}-<subpackage> and its -devel and -debuginfo too.
#	%%define variant_summary The Linux kernel compiled for <configuration>
#	%%kernel_variant_package [-n <pretty-name>] <subpackage>
#
%define kernel_variant_package(n:) \
%package %{?1:%{1}-}core\
Summary: %{variant_summary}\
Group: System Environment/Kernel\
Provides: %{name}-%{?1:%{1}-}core-uname-r = %{KVERREL}%{?variant}%{?1:+%{1}}\
Provides: installonlypkg(kernel)\
%{expand:%%kernel_reqprovconf}\
%if %{?1:1} %{!?1:0} \
%{expand:%%kernel_meta_package %{?1:%{1}}}\
%endif\
%{expand:%%kernel_devel_package %{?1:%{1}} %{!?-n:%{?1:%{1}}}%{?-n:%{-n*}}}\
%{expand:%%kernel_modules_package %{?1:%{1}} %{!?-n:%{?1:%{1}}}%{?-n:%{-n*}}}\
%{expand:%%kernel_modules_extra_package %{?1:%{1}} %{!?-n:%{?1:%{1}}}%{?-n:%{-n*}}}\
%{expand:%%kernel_debuginfo_package %{?1:%{1}}}\
%{nil}

%define variant_summary The Linux kernel compiled with extra debugging enabled
%kernel_variant_package debug
%description debug-core
The kernel package contains the Linux kernel (vmlinuz), the core of any
Linux operating system.  The kernel handles the basic functions
of the operating system:  memory allocation, process allocation, device
input and output, etc.

This variant of the kernel has numerous debugging options enabled.
It should only be installed when trying to gather additional information
on kernel bugs, as some of these options impact performance noticably.

# And finally the main -core package

%define variant_summary The Linux kernel
%kernel_variant_package
%description core
The kernel package contains
the Linux kernel (%{kernel_image_name}), the core of any Linux operating
system.  The kernel handles the basic functions of the operating system:
memory allocation, process allocation, device input and output, etc.


###
### prep
###

%prep
# do a few sanity-checks for --with *only builds
%if %{with_baseonly}
%if !%{with_up}
echo "Cannot build --with baseonly, up build is disabled"
exit 1
%endif
%endif

# more sanity checking; do it quietly
if [ "%{patches}" != "%%{patches}" ] ; then
  for patch in %{patches} ; do
    if [ ! -f $patch ] ; then
      echo "ERROR: Patch  ${patch##/*/}  listed in specfile but is missing"
      exit 1
    fi
  done
fi 2>/dev/null

patch_command='patch -p1 -F1 -s'
ApplyPatch()
{
  local patch=$1
  shift
  if [ ! -f $patch ]; then
    exit 1
  fi
  case "$patch" in
  *.bz2) bunzip2 < "$patch" | $patch_command ${1+"$@"} ;;
  *.gz)  gunzip  < "$patch" | $patch_command ${1+"$@"} ;;
  *.xz)  unxz    < "$patch" | $patch_command ${1+"$@"} ;;
  *) $patch_command ${1+"$@"} < "$patch" ;;
  esac
}

# don't apply patch if it's empty
ApplyOptionalPatch()
{
  local patch=$1
  shift
  if [ ! -f $patch ]; then
    exit 1
  fi
  local C=$(wc -l $patch | awk '{print $1}')
  if [ "$C" -gt 9 ]; then
    ApplyPatch $patch ${1+"$@"}
  fi
}

# First we unpack the kernel tarball.
# If this isn't the first make prep, we use links to the existing clean tarball
# which speeds things up quite a bit.

# Update to latest upstream.
%if 0%{?released_kernel}
%define vanillaversion %{kernel_release}.%{base_sublevel}
# non-released_kernel case
%else
%if 0%{?rcrev}
%define vanillaversion %{kernel_release}.%{upstream_sublevel}-rc%{rcrev}
%if 0%{?gitrev}
%define vanillaversion %{kernel_release}.%{upstream_sublevel}-rc%{rcrev}-git%{gitrev}
%endif
%else
# pre-{base_sublevel+1}-rc1 case
%if 0%{?gitrev}
%define vanillaversion %{kernel_release}.%{base_sublevel}-git%{gitrev}
%else
%define vanillaversion %{kernel_release}.%{base_sublevel}
%endif
%endif
%endif

# %%{vanillaversion} : the full version name, e.g. 2.6.35-rc6-git3
# %%{kversion}       : the base version, e.g. 2.6.34

# Use kernel-%%{kversion}%%{?dist} as the top-level directory name
# so we can prep different trees within a single git directory.

# Build a list of the other top-level kernel tree directories.
# This will be used to hardlink identical vanilla subdirs.
sharedirs=$(find "$PWD" -maxdepth 1 -type d -name 'kernel-%{kernel_release}.*' \
            | grep -x -v "$PWD"/kernel-%{kversion}%{?dist}) ||:

# Delete all old stale trees.
if [ -d kernel-%{kversion}%{?dist} ]; then
  cd kernel-%{kversion}%{?dist}
  for i in %{name}-*
  do
     if [ -d $i ]; then
       # Just in case we ctrl-c'd a prep already
       rm -rf deleteme.%{_target_cpu}
       # Move away the stale away, and delete in background.
       mv $i deleteme-$i
       rm -rf deleteme* &
     fi
  done
  cd ..
fi

# Generate new tree
if [ ! -d kernel-%{kversion}%{?dist}/vanilla-%{vanillaversion} ]; then

  if [ -d kernel-%{kversion}%{?dist}/vanilla-%{kversion} ]; then

    # The base vanilla version already exists.
    cd kernel-%{kversion}%{?dist}

    # Any vanilla-* directories other than the base one are stale.
    for dir in vanilla-*; do
      [ "$dir" = vanilla-%{kversion} ] || rm -rf $dir &
    done

  else

    rm -f pax_global_header
    # Look for an identical base vanilla dir that can be hardlinked.
    for sharedir in $sharedirs ; do
      if [[ ! -z $sharedir  &&  -d $sharedir/vanilla-%{kversion} ]] ; then
        break
      fi
    done
    if [[ ! -z $sharedir  &&  -d $sharedir/vanilla-%{kversion} ]] ; then
%setup -q -n %{name}-%{kversion}%{?dist} -c -T
      cp -al $sharedir/vanilla-%{kversion} .
    else
%setup -q -n %{name}-%{kversion}%{?dist} -c
      mv %{name}-%{version} vanilla-%{kversion}
    fi

  fi
else
  # We already have all vanilla dirs, just change to the top-level directory.
  cd kernel-%{kversion}%{?dist}
fi

# Now build the fedora kernel tree.
cp -al vanilla-%{vanillaversion} %{name}-%{KVERREL}
cd %{name}-%{KVERREL}

#
# misc small stuff to make things compile
#
#ApplyOptionalPatch compile-fixes.patch

%if !%{nopatches}

for i in %{patches}; do
  if [ ! $(echo $i |grep "/imx") ]; then
      ApplyPatch $i
  fi
done

# END OF PATCH APPLICATIONS
%endif

# Any further pre-build tree manipulations happen here.
chmod +x scripts/checkpatch.pl
mv COPYING COPYING-%{version}

# This Prevents scripts/setlocalversion from mucking with our version numbers.
touch .scmversion

# Do not use "ambiguous" python shebangs. RHEL 8 now has a new script
# (/usr/lib/rpm/redhat/brp-mangle-shebangs), which forces us to specify a
# "non-ambiguous" python shebang for scripts we ship in buildroot. This
# script throws an error like below:
# *** ERROR: ambiguous python shebang in /usr/bin/kvm_stat: #!/usr/bin/python. Change it to python3 (or python2) explicitly.
# We patch all sources below for which we got a report/error.
pathfix.py -i %{__python3} -p -n \
	scripts/show_delta \
	scripts/diffconfig \
	scripts/bloat-o-meter \
	scripts/tracing/draw_functrace.py \
	scripts/spdxcheck.py \
	tools/perf/tests/attr.py \
	tools/perf/scripts/python/stat-cpi.py \
	tools/perf/scripts/python/sched-migration.py \
	Documentation \
	scripts/clang-tools/gen_compile_commands.py

%define make make ARCH=$Arch %{?cross_opts} %{?make_opts}

# get rid of unwanted files resulting from patch fuzz
find . \( -name "*.orig" -o -name "*~" \) -exec rm -f {} \; >/dev/null

# remove unnecessary SCM files
find . -name .gitignore -exec rm -f {} \; >/dev/null

# Ensure all python shebangs in 'tools' & 'scripts' directory are using python3
find scripts tools -type f -exec sed -i '1s=^#! */usr/bin/\(python\|env python\)[23]\?=#!%{__python3}=' '{}' ';'

cd ..

###
### build
###
%build
#RLM WARNING DUE TO TEST BUILD:
mkdir  ~/bin
export PATH="${PATH}:/builddir/bin/"

ln -s /usr/aarch64-linux-gnu/sys-root/usr/bin/aarch64-redhat-linux-gnu-pkg-config /builddir/bin/aarch64-linux-gnu-pkg-config


%ifnarch %{arm} aarch64
echo "This build is for arm archiecture only"
exit 1
%endif

cp_vmlinux()
{
  eu-strip --remove-comment -o "$2" "$1"
}

BuildKernel() {
    MakeTarget=$1
    KernelImage=$2
    Flavour=$3
    Arch=%{asmarch}
    Flav=${Flavour:++${Flavour}}
    InstallName=$4
    DevelDir=/usr/src/kernels/%{KVERREL}

    # When the bootable image is just the ELF kernel, strip it.
    # We already copy the unstripped file into the debuginfo package.
    if [ "$KernelImage" = vmlinux ]; then
      CopyKernel=cp_vmlinux
    else
      CopyKernel=cp
    fi

    #KernelVer=%{version}-%{release}.%{_target_cpu}${Flav}
    KernelVer=%{KVERREL}

    echo BUILDING A KERNEL FOR ${Flavour} %{_target_cpu}...

    %if 0%{?stable_update}
    # make sure SUBLEVEL is incremented on a stable release.
    perl -p -i -e "s/^SUBLEVEL.*/SUBLEVEL = %{?stablerev}/" Makefile
    %endif

    # make sure EXTRAVERSION says what we want it to say
 	#IOTBZH: BE CAREFUL EXTRAVERSION needs to be less than 64 chars
    perl -p -i -e "s/^EXTRAVERSION.*/EXTRAVERSION = -%{release_short}.%{_target_cpu}/" Makefile

    # if pre-rc1 devel kernel, must fix up PATCHLEVEL for our versioning scheme
    %if !0%{?rcrev}
    %if 0%{?gitrev}
    perl -p -i -e 's/^PATCHLEVEL.*/PATCHLEVEL = %{upstream_sublevel}/' Makefile
    %endif
    %endif

    # and now to start the build process
    %{make} -s mrproper
    %{make} %{kernel_config}

    # merge custom kernel config fragments
    scripts/kconfig/merge_config.sh -m -r .config %{SOURCE1000}

    # merge base OS kernel config fragments
    scripts/kconfig/merge_config.sh -m -r .config %{?__rp_kernel_config_path}%{?__rp_baseos_config_name}

    # merge redpesk kernel config fragments
    scripts/kconfig/merge_config.sh -m -r .config %{?__rp_kernel_config_path}%{?__rp_kernel_config_name}

%if 0%{with_optimization}

%global get_sources_path_for_cfg() %{lua:
    local astart = 1001
    local astop = 1001+tonumber(rpm.expand("%{cfg_release}"))-1
    for i = astart, astop do
        print(rpm.expand(string.format("%%{SOURCE%d}", i)))
        print(" ")
    end
}

%global get_source_path_for_tested_cfg() %{lua:
    local cfg_nb = 1100+tonumber(rpm.expand("%{cfg_tested}"))
    print(rpm.expand(string.format("%%{SOURCE%d}", cfg_nb)))
}

    for CFG in %get_sources_path_for_cfg; do
      scripts/kconfig/merge_config.sh -m -r .config ${CFG}
    done

%if 0%{?cfg_tested}
  scripts/kconfig/merge_config.sh -m -r .config %get_source_path_for_tested_cfg
%endif

%endif

    echo "Building kernel with ARCH=$Arch"
    %{make} olddefconfig
    %{make} %{?_smp_mflags} $MakeTarget %{?sparse_mflags} %{?kernel_mflags}
    %{make} %{?_smp_mflags} modules %{?sparse_mflags} || exit 1

    # Device Tree / Overlay
    %{make} %{board_dtb}

    # Start installing the results
    mkdir -p %{buildroot}/%{image_install_path}
    mkdir -p %{buildroot}/lib/modules/$KernelVer/dtb
    %if %{with_debuginfo}
    mkdir -p %{buildroot}%{debuginfodir}/%{image_install_path}
    %endif

    install -m 644 .config %{buildroot}/%{image_install_path}/config-$KernelVer
    install -m 644 .config %{buildroot}/lib/modules/$KernelVer/config
    install -m 644 System.map %{buildroot}/%{image_install_path}/System.map-$KernelVer
    install -m 644 System.map %{buildroot}/lib/modules/$KernelVer/System.map

    # We estimate the size of the initramfs because rpm needs to take this size
    # into consideration when performing disk space calculations. (See bz #530778)
    dd if=/dev/zero of=%{buildroot}/%{image_install_path}/initramfs-$KernelVer.img bs=1M count=20

    # Install kernel binary
    install -m 755 $KernelImage %{buildroot}/%{image_install_path}/$InstallName-$KernelVer
    cp --sparse=always %{buildroot}/%{image_install_path}/$InstallName-$KernelVer %{buildroot}/lib/modules/$KernelVer/$InstallName

    # Install board device tree binaries
    # dtb symb link doesn't work that's why another copy of dtb is needed by U-Boot bootloader & extlinux
    for dtb in %{board_dtb}; do
        dtb_ver="`basename -s .dtb ${dtb}`-$KernelVer.dtb"
        install -m 644 arch/$Arch/boot/dts/${dtb} %{buildroot}/lib/modules/$KernelVer/dtb/
        install -m 644 arch/$Arch/boot/dts/${dtb} %{buildroot}/%{image_install_path}/${dtb_ver}
        #install -m 644 arch/$Arch/boot/dts/${dtb} %{buildroot}/%{image_install_path}/k3-am625-beagleplay.dtb
    done

    # hmac sign the kernel for FIPS
    echo "Creating hmac file: %{buildroot}/%{image_install_path}/.%{kernel_image_name}-$KernelVer.hmac"
    ls -l %{buildroot}/%{image_install_path}/$InstallName-$KernelVer
    sha512hmac %{buildroot}/%{image_install_path}/$InstallName-$KernelVer | sed -e "s,%{buildroot},," > %{buildroot}/%{image_install_path}/.%{kernel_image_name}-$KernelVer.hmac;
    cp %{buildroot}/%{image_install_path}/.%{kernel_image_name}-$KernelVer.hmac %{buildroot}/lib/modules/$KernelVer/.%{kernel_image_name}.hmac

    mkdir -p %{buildroot}/lib/modules/$KernelVer
    # Override $(mod-fw) because we don't want it to install any firmware
    # we'll get it from the linux-firmware package and we don't want conflicts
    %{make} -s %{?_smp_mflags} INSTALL_MOD_PATH=%{buildroot} modules_install KERNELRELEASE=$KernelVer mod-fw=

%if %{with_cross}
    # Build scripts for target before moving them into devel package
    compiler=%{_build_arch}-linux-gnu-
    %{make} HOSTCC=${compiler}gcc HOSTLD=${compiler}ld scripts %{?sparse_mflags} %{?kernel_mflags} %{?_smp_mflags}
    %{make} HOSTCC=${compiler}gcc HOSTLD=${compiler}ld modules_prepare %{?sparse_mflags} %{?kernel_mflags} %{?_smp_mflags}
%endif

    # And save the headers/makefiles etc for building modules against
    #
    # This all looks scary, but the end result is supposed to be:
    # * all arch relevant include/ files
    # * all Makefile/Kconfig files
    # * all script/ files

    rm -f %{buildroot}/lib/modules/$KernelVer/build
    rm -f %{buildroot}/lib/modules/$KernelVer/source
    mkdir -p %{buildroot}/lib/modules/$KernelVer/build
    (cd %{buildroot}/lib/modules/$KernelVer ; ln -s build source)
    # dirs for additional modules per module-init-tools, kbuild/modules.txt
    mkdir -p %{buildroot}/lib/modules/$KernelVer/extra
    mkdir -p %{buildroot}/lib/modules/$KernelVer/updates
    # first copy everything
    cp --parents `find  -type f -name "Makefile*" -o -name "Kconfig*"` %{buildroot}/lib/modules/$KernelVer/build
    cp Module.symvers %{buildroot}/lib/modules/$KernelVer/build
    cp System.map %{buildroot}/lib/modules/$KernelVer/build
    if [ -s Module.markers ]; then
      cp Module.markers %{buildroot}/lib/modules/$KernelVer/build
    fi
    # then drop all but the needed Makefiles/Kconfig files
    rm -rf %{buildroot}/lib/modules/$KernelVer/build/Documentation
    rm -rf %{buildroot}/lib/modules/$KernelVer/build/scripts
    rm -rf %{buildroot}/lib/modules/$KernelVer/build/include
    cp .config %{buildroot}/lib/modules/$KernelVer/build
    cp -a scripts %{buildroot}/lib/modules/$KernelVer/build
    if [ -d arch/$Arch/scripts ]; then
      cp -a arch/$Arch/scripts %{buildroot}/lib/modules/$KernelVer/build/arch/%{_arch} || :
    fi
    if [ -f arch/$Arch/*lds ]; then
      cp -a arch/$Arch/*lds %{buildroot}/lib/modules/$KernelVer/build/arch/%{_arch}/ || :
    fi
    rm -f %{buildroot}/lib/modules/$KernelVer/build/scripts/*.o
    rm -f %{buildroot}/lib/modules/$KernelVer/build/scripts/*/*.o
    if [ -d arch/%{asmarch}/include ]; then
      cp -a --parents arch/%{asmarch}/include %{buildroot}/lib/modules/$KernelVer/build/
    fi

    # We need module.lds to compile out-of-tree modules
    cp -a --parents scripts/module.lds %{buildroot}/lib/modules/$KernelVer/build/

    # include the machine specific headers
    if [ -d arch/%{asmarch}/mach-${Flavour}/include ]; then
      cp -a --parents arch/%{asmarch}/mach-${Flavour}/include %{buildroot}/lib/modules/$KernelVer/build/
    fi

    # include a few files for 'make prepare'
    cp -a --parents arch/arm/tools/gen-mach-types %{buildroot}/lib/modules/$KernelVer/build/
    cp -a --parents arch/arm/tools/mach-types %{buildroot}/lib/modules/$KernelVer/build/

    cp -a include %{buildroot}/lib/modules/$KernelVer/build/include

    # Make sure the Makefile and version.h have a matching timestamp so that
    # external modules can be built
    touch -r %{buildroot}/lib/modules/$KernelVer/build/Makefile %{buildroot}/lib/modules/$KernelVer/build/include/generated/uapi/linux/version.h

    # Copy .config to include/config/auto.conf so "make prepare" is unnecessary.
    cp %{buildroot}/lib/modules/$KernelVer/build/.config %{buildroot}/lib/modules/$KernelVer/build/include/config/auto.conf

%if %{with_debuginfo}
    eu-readelf -n vmlinux | grep "Build ID" | awk '{print $NF}' > vmlinux.id
    cp vmlinux.id %{buildroot}/lib/modules/$KernelVer/build/vmlinux.id

    #
    # save the vmlinux file for kernel debugging into the kernel-debuginfo rpm
    #
    mkdir -p %{buildroot}%{debuginfodir}/lib/modules/$KernelVer
    cp --sparse=always vmlinux %{buildroot}%{debuginfodir}/lib/modules/$KernelVer
%endif

    find %{buildroot}/lib/modules/$KernelVer -name "*.ko*" -type f >modnames

    # mark modules executable so that strip-to-file can strip them
    xargs --no-run-if-empty chmod u+x < modnames

    # Generate a list of modules for block and networking.

    grep -F /drivers/ modnames | xargs --no-run-if-empty nm -upA |
    sed -n 's,^.*/\([^/]*\.ko*\):  *U \(.*\)$,\1 \2,p' > drivers.undef

    collect_modules_list()
    {
      sed -r -n -e "s/^([^ ]+) \\.?($2)\$/\\1/p" drivers.undef |
        LC_ALL=C sort -u > %{buildroot}/lib/modules/$KernelVer/modules.$1
      if [ ! -z "$3" ]; then
        sed -r -e "/^($3)\$/d" -i %{buildroot}/lib/modules/$KernelVer/modules.$1
      fi
    }

    collect_modules_list networking \
      'register_netdev|ieee80211_register_hw|usbnet_probe|phy_driver_register|rt(l_|2x00)(pci|usb)_probe|register_netdevice'
    collect_modules_list block \
      'ata_scsi_ioctl|scsi_add_host|scsi_add_host_with_dma|blk_alloc_queue|blk_init_queue|register_mtd_blktrans|scsi_esp_register|scsi_register_device_handler|blk_queue_physical_block_size' 'pktcdvd.ko|dm-mod.ko'
    collect_modules_list drm \
      'drm_open|drm_init'
    collect_modules_list modesetting \
      'drm_crtc_init'

    # detect missing or incorrect license tags
    ( find %{buildroot}/lib/modules/$KernelVer -name '*.ko' | xargs /sbin/modinfo -l | \
        grep -E -v 'GPL( v2)?$|Dual BSD/GPL$|Dual MPL/GPL$|GPL and additional rights$' ) && exit 1

    # remove files that will be auto generated by depmod at rpm -i time
    pushd %{buildroot}/lib/modules/$KernelVer/
        rm -f modules.{alias*,builtin.bin,dep*,*map,symbols*,devname,softdep}
    popd

    cp %{SOURCE100} %{buildroot}/filter-AM62x.sh

    # Call the modules-extra script to move things around
    sh %{SOURCE17} %{buildroot}/lib/modules/$KernelVer %{SOURCE16}

    #
    # Generate the kernel-core and kernel-modules files lists
    #

    # Copy the System.map file for depmod to use, and create a backup of the
    # full module tree so we can restore it after we're done filtering
    cp System.map %{buildroot}/.
    pushd %{buildroot}
    mkdir restore
    cp -r lib/modules/$KernelVer/* restore/.

    # don't include anything going into k-m-e in the file lists
    rm -rf lib/modules/$KernelVer/extra

    # Find all the module files and filter them out into the core and modules
    # lists.  This actually removes anything going into -modules from the dir.
    find lib/modules/$KernelVer/kernel -name *.ko* | sort -n > modules.list
	cp $RPM_SOURCE_DIR/filter-*.sh .
    sh %{SOURCE99} modules.list %{_target_cpu} %{Flavour}
	rm filter-*.sh

    # Run depmod on the resulting module tree and make sure it isn't broken
    ln -s lib/modules/$KernelVer $KernelVer
    depmod -b . -aeF ./System.map $KernelVer &> depmod.out
    if [ -s depmod.out ]; then
        echo "Depmod failure"
        cat depmod.out
        exit 1
    else
        rm depmod.out
    fi
    unlink $KernelVer

    # remove files that will be auto generated by depmod at rpm -i time
    pushd %{buildroot}/lib/modules/$KernelVer/
        rm -f modules.{alias*,builtin.bin,dep*,*map,symbols*,devname,softdep}
    popd

    # Go back and find all of the various directories in the tree.  We use this
    # for the dir lists in kernel-core
    find lib/modules/$KernelVer/kernel -mindepth 1 -type d | sort -n > module-dirs.list

    # Cleanup
    rm System.map
    cp -r restore/* lib/modules/$KernelVer/.
    rm -rf restore
    popd

    # Make sure the files lists start with absolute paths or rpmbuild fails.
    # Also add in the dir entries
    sed -e 's/^lib*/\/lib/' %{?zipsed} %{buildroot}/k-d.list > ../kernel-modules.list
    sed -e 's/^lib*/%dir \/lib/' %{?zipsed} %{buildroot}/module-dirs.list > ../kernel-core.list
    sed -e 's/^lib*/\/lib/' %{?zipsed} %{buildroot}/modules.list >> ../kernel-core.list

    # Cleanup
    rm -f %{buildroot}/k-d.list
    rm -f %{buildroot}/modules.list
    rm -f %{buildroot}/module-dirs.list

    # Move the devel headers out of the root file system
    mkdir -p %{buildroot}/usr/src/kernels
    mv %{buildroot}/lib/modules/$KernelVer/build %{buildroot}/$DevelDir

    # This is going to create a broken link during the build, but we don't use
    # it after this point.  We need the link to actually point to something
    # when kernel-devel is installed, and a relative link doesn't work across
    # the F17 UsrMove feature.
    ln -sf $DevelDir %{buildroot}/lib/modules/$KernelVer/build

    # prune junk from kernel-devel
    find %{buildroot}/usr/src/kernels -name ".*.cmd" -exec rm -f {} \;
}


###
# DO it...
###

# prepare directories
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{image_install_path}
mkdir -p %{buildroot}%{_libexecdir}

cd %{name}-%{KVERREL}

BuildKernel %make_target %kernel_image %{?Flavour} %{kernel_image_name}

%global perf_make \
  make EXTRA_CFLAGS="${RPM_OPT_FLAGS}" LDFLAGS="%{__global_ldflags}" CROSS_COMPILE=aarch64-linux-gnu- -C tools/perf NO_PERF_READ_VDSO32=1 NO_PERF_READ_VDSOX32=1 WERROR=0 NO_LIBUNWIND=1 HAVE_CPLUS_DEMANGLE=1 NO_GTK2=1 NO_STRLCPY=1 NO_BIONIC=1 prefix=%{_prefix} PYTHON=%{__python3}
%if %{with_perf}
# perf
# make sure check-headers.sh is executable
chmod +x tools/perf/check-headers.sh
%{perf_make} DESTDIR=%{buildroot} all
%endif

%global tools_make \
  %{make} CFLAGS="${RPM_OPT_FLAGS}" LDFLAGS="%{__global_ldflags}" V=1

%if %{with_tools}
%ifarch %{cpupowerarchs}
# cpupower
# make sure version-gen.sh is executable.
chmod +x tools/power/cpupower/utils/version-gen.sh
%{tools_make} -C tools/power/cpupower CPUFREQ_BENCH=false DEBUG=false
%endif
pushd tools/thermal/tmon/
%{tools_make}
popd
pushd tools/iio/
%{tools_make}
popd
pushd tools/gpio/
%{tools_make}
popd
# build VM tools
pushd tools/vm/
%{tools_make} slabinfo page_owner_sort
popd
%endif


if [ "%{zipmodules}" -eq "1" ]; then \
    RPM_BUILD_ROOT=%{buildroot}/lib/modules/ /usr/lib/rpm/brp-strip %{_build_arch}-linux-gnu-strip; \
    find %{buildroot}/lib/modules/ -type f -name '*.ko' | xargs xz; \
fi



###
### Special hacks for debuginfo subpackages.
###

# This macro is used by %%install, so we must redefine it before that.
%define debug_package %{nil}

%if %{with_debuginfo}

%ifnarch noarch
%global __debug_package 1
%files -f debugfiles.list debuginfo-common-%{_target_cpu}
%defattr(-,root,root)
%endif

%endif

# We don't want to package debuginfo for self-tests and samples but
# we have to delete them to avoid an error messages about unpackaged
# files.
%define __remove_unwanted_dbginfo_install_post \
  if [ "%{with_selftests}" -ne "0" ]; then \
    rm -rf $RPM_BUILD_ROOT/usr/lib/debug/usr/libexec/ksamples; \
    rm -rf $RPM_BUILD_ROOT/usr/lib/debug/usr/libexec/kselftests; \
  fi \
%{nil}

#
# Disgusting hack alert! We need to ensure we sign modules *after* all
# invocations of strip occur, which is in __debug_install_post if
# find-debuginfo.sh runs, and __os_install_post if not.
#
%define __spec_install_post \
  %{?__debug_package:%{__debug_install_post}}\
  %{__arch_install_post}\
  %{__os_install_post}\
  %{__remove_unwanted_dbginfo_install_post}

###
### install
###

%install
#RLM WARNING DUE TO TEST BUILD:
export PATH="${PATH}:/builddir/bin/"
cd %{name}-%{KVERREL}

%if %{with_doc}
docdir=%{buildroot}%{_datadir}/doc/kernel-doc-%{rpmversion}

# copy the source over
mkdir -p $docdir
tar -h -f - --exclude=man --exclude='.*' -c Documentation | tar xf - -C $docdir

# with_doc
%endif

# We have to do the headers install before the tools install because the
# kernel headers_install will remove any header files in /usr/include that
# it doesn't install itself.

%if %{with_headers}
# Install kernel headers
%{make} ARCH=%{hdrarch} INSTALL_HDR_PATH=%{buildroot}/usr headers_install

find %{buildroot}/usr/include \
     \( -name .install -o -name .check -o \
        -name ..install.cmd -o -name ..check.cmd \) | xargs rm -f

%endif
#RLM WARNING DUE TO TEST BUILD: Remove install-traceevent-plugins
%if %{with_perf}
# perf tool binary and supporting scripts/binaries
%{perf_make} DESTDIR=%{buildroot} lib=%{_lib} install-bin 
# remove the 'trace' symlink.
rm -f %{buildroot}%{_bindir}/trace

# For both of the below, yes, this should be using a macro but right now
# it's hard coded and we don't actually want it anyway right now.
# Whoever wants examples can fix it up!

# remove examples
rm -rf %{buildroot}/usr/lib/examples/perf
# remove the stray header file that somehow got packaged in examples
rm -rf %{buildroot}/usr/lib/include/perf/bpf/bpf.h

# remove perf-bpf examples
rm -rf %{buildroot}/usr/lib/perf/examples
rm -rf %{buildroot}/usr/lib/perf/include

#RLM WARNING DUE TO TEST BUILD:
# python-perf extension
#%%{perf_make} DESTDIR=%{buildroot} install-python_ext

# perf man pages (note: implicit rpm magic compresses them later)
mkdir -p %{buildroot}/%{_mandir}/man1
%{perf_make} DESTDIR=%{buildroot} install-man
%endif

%if %{with_tools}
%{make} -C tools/power/cpupower DESTDIR=%{buildroot} libdir=%{_libdir} mandir=%{_mandir} CPUFREQ_BENCH=false install
rm -f %{buildroot}%{_libdir}/*.{a,la}
%find_lang cpupower
mv cpupower.lang ../
chmod 0755 %{buildroot}%{_libdir}/libcpupower.so*
mkdir -p %{buildroot}%{_unitdir} %{buildroot}%{_sysconfdir}/sysconfig
install -m644 %{SOURCE2000} %{buildroot}%{_unitdir}/cpupower.service
install -m644 %{SOURCE2001} %{buildroot}%{_sysconfdir}/sysconfig/cpupower
pushd tools/thermal/tmon
%{tools_make} INSTALL_ROOT=%{buildroot} install
popd
pushd tools/iio
%{tools_make} DESTDIR=%{buildroot} install
popd
pushd tools/gpio
%{tools_make} DESTDIR=%{buildroot} install
popd
pushd tools/kvm/kvm_stat
make INSTALL_ROOT=%{buildroot} install-tools
make INSTALL_ROOT=%{buildroot} install-man
popd
# install VM tools
pushd tools/vm/
install -m755 slabinfo %{buildroot}%{_bindir}/slabinfo
install -m755 page_owner_sort %{buildroot}%{_bindir}/page_owner_sort
popd
%endif


###
### clean
###

%clean
rm -rf $RPM_BUILD_ROOT

###
### scripts
###

%if %{with_tools}
%post -n %{name}-tools-libs
/sbin/ldconfig

%postun -n %{name}-tools-libs
/sbin/ldconfig
%endif

#
# This macro defines a %%post script for a kernel*-devel package.
#	%%kernel_devel_post [<subpackage>]
#
%define kernel_devel_post() \
%{expand:%%post %{?1:%{1}-}devel}\
if [ -f /etc/sysconfig/kernel ]\
then\
    . /etc/sysconfig/kernel || exit $?\
fi\
if [ "$HARDLINK" != "no" -a -x /usr/sbin/hardlink ]\
then\
    (cd /usr/src/kernels/%{KVERREL}%{?1:+%{1}} &&\
     /usr/bin/find . -type f | while read f; do\
       hardlink -c /usr/src/kernels/*%{?dist}.*/$f $f\
     done)\
fi\
%{nil}

#
# This macro defines a %%post script for a kernel*-modules-extra package.
# It also defines a %%postun script that does the same thing.
#	%%kernel_modules_extra_post [<subpackage>]
#
%define kernel_modules_extra_post() \
%{expand:%%post %{?1:%{1}-}modules-extra}\
/sbin/depmod -a %{KVERREL}%{?1:+%{1}}\
%{nil}\
%{expand:%%postun %{?1:%{1}-}modules-extra}\
/sbin/depmod -a %{KVERREL}%{?1:+%{1}}\
%{nil}

#
# This macro defines a %%post script for a kernel*-modules package.
# It also defines a %%postun script that does the same thing.
#	%%kernel_modules_post [<subpackage>]
#
%define kernel_modules_post() \
%{expand:%%post %{?1:%{1}-}modules}\
/sbin/depmod -a %{KVERREL}%{?1:+%{1}}\
%{nil}\
%{expand:%%postun %{?1:%{1}-}modules}\
/sbin/depmod -a %{KVERREL}%{?1:+%{1}}\
%{nil}

# This macro defines a %%posttrans script for a kernel package.
#	%%kernel_variant_posttrans [<subpackage>]
# More text can follow to go at the end of this variant's %%post.
#
%define kernel_variant_posttrans() \
%{expand:%%posttrans %{?1:%{1}-}core}\
/sbin/depmod -a %{KVERREL}%{?1:+%{1}}\
cp --sparse=always -f /lib/modules/%{KVERREL}%{?1:+%{1}}/%{kernel_image_name} /%{image_install_path}/%{kernel_image_name}-%{KVERREL}%{?1:+%{1}}\
if [[ `df /%{image_install_path} --output=fstype | sed -n 2p` = "ext4" ]]; then\
    ln -sf %{kernel_image_name}-%{KVERREL}%{?1:+%{1}} /%{image_install_path}/%{kernel_image_name}\
else\
    cp --sparse=always -f /lib/modules/%{KVERREL}%{?1:+%{1}}/%{kernel_image_name} /%{image_install_path}/%{kernel_image_name}\
fi\
cd /lib/modules/%{KVERREL}%{?1:+%{1}}/dtb/\
for dtb in `ls *.dtb`; do\
    dtb_ver="`basename -s .dtb ${dtb}`-%{KVERREL}%{?1:+%{1}}.dtb"\
    cp -f ${dtb} /%{image_install_path}/${dtb_ver} \
    cp -f ${dtb} /%{image_install_path}/ \
done\
cd -\
cp -f /lib/modules/%{KVERREL}%{?1:+%{1}}/config /%{image_install_path}/config-%{KVERREL}%{?1:+%{1}}\
cp -f /lib/modules/%{KVERREL}%{?1:+%{1}}/System.map /%{image_install_path}/System.map-%{KVERREL}%{?1:+%{1}}\
cp -f /lib/modules/%{KVERREL}%{?1:+%{1}}/.%{kernel_image_name}.hmac /%{image_install_path}/.%{kernel_image_name}.hmac-%{KVERREL}%{?1:+%{1}}\
%{nil}

#
# This macro defines a %%post script for a kernel package and its devel package.
#	%%kernel_variant_post [-v <subpackage>] [-r <replace>]
# More text can follow to go at the end of this variant's %%post.
#
%define kernel_variant_post(v:r:) \
%{expand:%%kernel_devel_post %{?-v*}}\
%{expand:%%kernel_modules_post %{?-v*}}\
%{expand:%%kernel_modules_extra_post %{?-v*}}\
%{expand:%%kernel_variant_posttrans %{?-v*}}\
%{expand:%%post %{?-v*:%{-v*}-}core}\
%{nil}

#
# This macro defines a %%preun script for a kernel package.
#	%%kernel_variant_preun <subpackage>
#
%define kernel_variant_preun() \
%{expand:%%preun %{?1:%{1}-}core}\
/bin/kernel-install remove %{KVERREL}%{?1:+%{1}} /%{image_install_path}/%{kernel_image_name}-%{KVERREL}%{?1:+%{1}} || exit $?\
unlink /%{image_install_path}/%{kernel_image_name}\
cd /lib/modules/%{KVERREL}%{?1:+%{1}}/dtb/\
for dtb in `ls *.dtb`; do\
    dtb_ver="`basename -s .dtb ${dtb}`-%{KVERREL}%{?1:+%{1}}.dtb"\
    unlink /%{image_install_path}/${dtb_ver} \
done\
cd -\
rm -f /%{image_install_path}/config-%{KVERREL}%{?1:+%{1}}\
rm -f /%{image_install_path}/System.map-%{KVERREL}%{?1:+%{1}}\
rm -f /%{image_install_path}/.%{kernel_image_name}.hmac-%{KVERREL}%{?1:+%{1}}\
%{nil}

%kernel_variant_preun
%kernel_variant_post -r kernel

if [ -x /sbin/ldconfig ]
then
    /sbin/ldconfig -X || exit $?
fi

###
### file lists
###

%if %{with_headers}
%files headers
%defattr(-,root,root)
/usr/include/*
%endif

%if %{with_cross_headers}
%files cross-headers
%defattr(-,root,root)
/usr/*-linux-gnu/include/*
%endif

# only some architecture builds need kernel-doc
%if %{with_doc}
%files doc
%defattr(-,root,root)
%{_datadir}/doc/kernel-doc-%{rpmversion}/Documentation/*
%dir %{_datadir}/doc/kernel-doc-%{rpmversion}/Documentation
%dir %{_datadir}/doc/kernel-doc-%{rpmversion}
%endif

%if %{with_perf}
%files -n perf
%defattr(-,root,root)
%{_bindir}/perf
%{_libdir}/libperf-jvmti.so
#RLM WARNING DUE TO TEST BUILD: Remove install-traceevent-plugins
#%%dir %%{_libdir}/traceevent/plugins
#%%{_libdir}/traceevent/plugins/*
%dir %{_libexecdir}/perf-core
%{_libexecdir}/perf-core/*
%{_datadir}/perf-core/*
%{_mandir}/man[1-8]/perf*
%{_sysconfdir}/bash_completion.d/perf
%doc %{name}-%{KVERREL}/tools/perf/Documentation/examples.txt
%{_docdir}/perf-tip/tips.txt

#RLM WARNING DUE TO TEST BUILD:
#%%files -n python3-perf
#%defattr(-,root,root)
#%%{python3_sitearch}/*

%if %{with_debuginfo}
%files -f perf-debuginfo.list -n perf-debuginfo
%defattr(-,root,root)

%files -f python3-perf-debuginfo.list -n python3-perf-debuginfo
%defattr(-,root,root)
%endif
# with_perf
%endif

%if %{with_tools}
%ifarch %{cpupowerarchs}
%defattr(-,root,root)
%files -n %{name}-tools -f cpupower.lang
%{_bindir}/cpupower
%{_datadir}/bash-completion/completions/cpupower
%{_unitdir}/cpupower.service
%{_mandir}/man[1-8]/cpupower*
%config(noreplace) %{_sysconfdir}/sysconfig/cpupower
# !cpupowerarchs
%else
%files -n %{name}-tools
%defattr(-,root,root)
# cpupowerarchs
%endif
%{_bindir}/tmon
%{_bindir}/iio_event_monitor
%{_bindir}/iio_generic_buffer
%{_bindir}/lsiio
%{_bindir}/lsgpio
%{_bindir}/gpio-hammer
%{_bindir}/gpio-event-mon
%{_mandir}/man1/kvm_stat*
%{_bindir}/kvm_stat
%{_bindir}/page_owner_sort
%{_bindir}/slabinfo

%if %{with_debuginfo}
%files -f %{name}-tools-debuginfo.list -n %{name}-tools-debuginfo
%defattr(-,root,root)
%endif

%ifarch %{cpupowerarchs}
%files -n %{name}-tools-libs
%{_libdir}/libcpupower.so.0
%{_libdir}/libcpupower.so.0.0.1

%files -n %{name}-tools-libs-devel
%{_libdir}/libcpupower.so
%{_includedir}/cpufreq.h
%endif
# with_tools
%endif


# empty meta-package
%files
%defattr(-,root,root)

# This is %%{image_install_path} on an arch where that includes ELF files,
# or empty otherwise.
%define elf_image_install_path %{?kernel_image_elf:%{image_install_path}}

#
# This macro defines the %%files sections for a kernel package
# and its devel and debuginfo packages.
#	%%kernel_variant_files [-k vmlinux] <condition> <subpackage> <without_modules>
#
%define kernel_variant_files(k:) \
%{expand:%%files -f kernel-%{?2:%{2}-}core.list %{?2:%{2}-}core}\
%defattr(-,root,root)\
%{!?_licensedir:%global license %%doc}\
%license %{name}-%{KVERREL}/COPYING-%{version}\
%ghost /%{image_install_path}/%{?-k:%{-k*}}%{!?-k:%{kernel_image_name}}-%{KVERREL}%{?2:+%{2}}\
%ghost /%{image_install_path}/*-%{KVERREL}%{?2:+%{2}}.dtb\
%ghost /%{image_install_path}/%{kernel_image_name}\
%ghost /%{image_install_path}/.%{kernel_image_name}-%{KVERREL}%{?2:+%{2}}.hmac\
%ghost /%{image_install_path}/System.map-%{KVERREL}%{?2:+%{2}}\
%ghost /%{image_install_path}/config-%{KVERREL}%{?2:+%{2}}\
%ghost /%{image_install_path}/initramfs-%{KVERREL}%{?2:+%{2}}.img\
%ghost /%{image_install_path}/kernel*.img\
%dir /lib/modules\
%dir /lib/modules/%{KVERREL}%{?2:+%{2}}\
%dir /lib/modules/%{KVERREL}%{?2:+%{2}}/kernel\
%attr(600,root,root) /lib/modules/%{KVERREL}%{?2:+%{2}}/System.map\
/lib/modules/%{KVERREL}%{?2:+%{2}}/.%{kernel_image_name}.hmac\
/lib/modules/%{KVERREL}%{?2:+%{2}}/dtb\
/lib/modules/%{KVERREL}%{?2:+%{2}}/%{?-k:%{-k*}}%{!?-k:%{kernel_image_name}}\
/lib/modules/%{KVERREL}%{?2:+%{2}}/config\
/lib/modules/%{KVERREL}%{?2:+%{2}}/build\
/lib/modules/%{KVERREL}%{?2:+%{2}}/source\
/lib/modules/%{KVERREL}%{?2:+%{2}}/updates\
/lib/modules/%{KVERREL}%{?2:+%{2}}/modules.*\
%{expand:%%files -f kernel-%{?2:%{2}-}modules.list %{?2:%{2}-}modules}\
%defattr(-,root,root)\
%{expand:%%files %{?2:%{2}-}devel}\
%defattr(-,root,root)\
/usr/src/kernels/%{KVERREL}%{?2:+%{2}}\
%{expand:%%files %{?2:%{2}-}modules-extra}\
%defattr(-,root,root)\
/lib/modules/%{KVERREL}%{?2:+%{2}}/extra\
%if %{with_debuginfo}\
%ifnarch noarch\
%{expand:%%files -f debuginfo%{?2}.list %{?2:%{2}-}debuginfo}\
%defattr(-,root,root)\
%endif\
%endif\
%if %{?2:1} %{!?2:0}\
%{expand:%%files %{2}}\
%defattr(-,root,root)\
%endif\
%{nil}

%kernel_variant_files


%changelog

###
# The following Emacs magic makes C-c C-e use UTC dates.
# Local Variables:
# rpm-change-log-uses-utc: t
# End:
###
