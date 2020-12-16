#
# spec file for package butterback
#
# Copyright (c) 2016-2018 Vladimir Olteanu <vl.olteanu@gmail.com>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           butterback
Version:        9834025c25c180a09e8ad57bcdd1db2c09032734
Release:        0
License:        WTFPLv2
Summary:        Simple backup tool using BtrFS
Url:            https://github.com/vlolteanu/butterback
Source0:        butterback-9834025c25c180a09e8ad57bcdd1db2c09032734.tar.gz

Requires:       bash
Requires:       coreutils
Requires:       btrfsprogs
Requires:       rsync

%description


%prep
%setup -q

%build


%install
ls
install -m 0755 -d $RPM_BUILD_ROOT/etc/butterback
install -m 0744 -D butterback $RPM_BUILD_ROOT/usr/sbin/butterback

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc COPYING
/etc/butterback
/usr/sbin/butterback

%changelog
