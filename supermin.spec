Name:           supermin
Version:        5.1.19
Release:        9
Summary:        A tool for building supermin appliances, required by libguestfs
License:        GPLv2+
URL:            http://libguestfs.org/
Source0:        http://libguestfs.org/download/supermin/%{name}-%{version}.tar.gz
Patch0001:      0001-Fix-Bytes-String-for-OCaml-4.06.patch
Patch9000:      9000-fix-cannot-detect-package-manager-on-openeuler.patch
BuildRequires:  augeas dietlibc-devel dnf dnf-plugins-core e2fsprogs-devel
BuildRequires:  findutils gnupg2 grubby hivex kernel ocaml ocaml-findlib-devel
BuildRequires:  rpm rpm-devel systemd-udev tar
BuildRequires:  /usr/bin/pod2man /usr/bin/pod2html /usr/sbin/mke2fs
Requires:       cpio dnf dnf-plugins-core e2fsprogs-libs >= 1.42 findutils
Requires:       rpm tar util-linux-ng /usr/sbin/mke2fs

%description
Supermin is a tool for building supermin appliances.  These are tiny
appliances (similar to virtual machines), usually around 100KB in
size, which get fully instantiated on-the-fly in a fraction of a
second when you need to boot one of them.

%package        help
Summary:        Man files for supermin
Requires:       man
BuildArch:      noarch

%description help
This contains man files for the using of supermin.

%prep
%autosetup -p1

%build
%configure --disable-network-tests
make -C init CC="diet gcc"
%make_build

%install
%make_install

%check
#%ifarch aarch64
#export SKIP_TEST_EXECSTACK=1
#%endif

#make check || {
#    cat tests/test-suite.log
#    exit 1
#}

%files
%doc examples/build-basic-vm.sh README
%license COPYING
%{_bindir}/*

%files help
%{_mandir}/man1/*

%changelog
* Fri Feb 14 2020 Ling Yang <lingyang2@huawei.com> - 5.1.19-9
- Package Initialization
