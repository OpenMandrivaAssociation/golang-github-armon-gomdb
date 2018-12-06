# https://github.com/armon/gomdb
%global goipath         github.com/armon/gomdb
%global commit          75f545a47e8956a9f84de7d95fafb003dc916831

%gometa

Name:           %{goname}
Version:        0
Release:        0.16%{?dist}
Summary:        Go wrapper for LMDB - OpenLDAP Lightning Memory-Mapped Database
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.lock
Source2:        glide.yaml
Patch0:         use-system-lmdb.patch

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: lmdb-devel
Requires:      lmdb-devel

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{gobaseipath} prefix.

%prep
%forgesetup
%patch0 -p1
cp %{SOURCE1} %{SOURCE2} .

%install
%goinstall glide.lock glide.yaml

%check
%gochecks -d .

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Mon Nov 12 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.17.20181112git75f545a
- Bump to commit 75f545a47e8956a9f84de7d95fafb003dc916831

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.15.git.git151f2e0
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.git.git151f2e0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 08 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.13.git.git151f2e0
- Update to spec 3.0
  Upload glide.lock and glide.yaml

* Mon Feb 26 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.12.20150106git151f2e0
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.git151f2e0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.git151f2e0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.git151f2e0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.git151f2e0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.git151f2e0
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.git151f2e0
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.git151f2e0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 0-0.4.git151f2e0
- Update to spec-2.1
  related: #1248536

* Thu Jul 30 2015 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.3.git151f2e0
- Update of spec file to spec-2.0
  resolves: #1248536

* Sat Jun 20 2015 jchaloup <jchaloup@redhat.com> - 0-0.2.git151f2e0
- Add missing runtime dependency on lmdb-devel
  related: #1212046

* Wed Apr 15 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.git151f2e0
- First package for Fedora
  resolves: #1212046
