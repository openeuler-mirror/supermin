Name:           supermin
Version:        5.1.19
Release:        13
Summary:        A tool for building supermin appliances, required by libguestfs
License:        GPLv2+
URL:            http://libguestfs.org/
Source0:        http://libguestfs.org/download/supermin/%{name}-%{version}.tar.gz
Source1:        supermin.attr
Source2:        supermin-find-requires
Patch0001:      0001-Fix-Bytes-String-for-OCaml-4.06.patch
Patch0002:      0002-use-installed-packages-instead-of-dnf-downloading.patch
Patch9000:      9000-fix-cannot-detect-package-manager-on-openeuler.patch
Patch9001:      add-pie-and-bind_now-flags.patch
Patch9002:      9002-fix-cannot-detect-package-manager-on-UnionTech.patch

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

%package        devel
Summary:        Development tools for supermin
Requires:       supermin = %{version}-%{release}
Requires:       rpm-build

%description    devel
supermin-devel contains development tools for supermin.

%package        help
Summary:        Man files for supermin
Requires:       man
BuildArch:      noarch

%description    help
This contains man files for the using of supermin.

%prep
%autosetup -p1

%build
%configure --disable-network-tests
make -C init CC="diet gcc"
%make_build

%install
%make_install

mkdir -p $RPM_BUILD_ROOT%{_rpmconfigdir}/fileattrs/
install -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_rpmconfigdir}/fileattrs/
install -m 0755 %{SOURCE2} $RPM_BUILD_ROOT%{_rpmconfigdir}/

%files
%doc examples/build-basic-vm.sh README
%license COPYING
%{_bindir}/*

%files devel
%{_rpmconfigdir}/fileattrs/supermin.attr
%{_rpmconfigdir}/supermin-find-requires

%files help
%{_mandir}/man1/*

%changelog
* Fri Oct 08 2021 wangqing <wangqing@uniontech.com> - 5.1.19-13
- fix cannot detect package manager on UnionTech

* Wed Sep 08 2021 wangyue <wangyue92@huawei.com> - 5.1.19-12
- Add pie and bind_now flags

* Wed Dec 16 2020 maminjie <maminjie1@huawei.com> - 5.1.19-11
- Use installed packages instead of dnf downloading

* Mon Mar 2 2020 Ling Yang <lingyang2@huawei.com> - 5.1.19-10
- Add devel package

* Fri Feb 14 2020 Ling Yang <lingyang2@huawei.com> - 5.1.19-9
- Package Initialization
