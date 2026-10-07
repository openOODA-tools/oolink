Name:           oolink
Version:        0.1.0
Release:        1%{?dist}
Summary:        Single-purpose POSIX hard linker with inode verification.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oolink
Source0:        oolink-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oolink is a sovereign, capability-bounded HARD LINKER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oolink
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oolink-uninstall

%files
/usr/bin/oolink
/usr/bin/oolink-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
