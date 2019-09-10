#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-frocksdb
Version  : 5.17.2.artisans.1.0
Release  : 1
URL      : https://github.com/dataArtisans/frocksdb/archive/v5.17.2-artisans-1.0.tar.gz
Source0  : https://github.com/dataArtisans/frocksdb/archive/v5.17.2-artisans-1.0.tar.gz
Source1  : https://repo.maven.apache.org/maven2/com/data-artisans/frocksdbjni/5.17.2-artisans-1.0/frocksdbjni-5.17.2-artisans-1.0.jar
Source2  : https://repo.maven.apache.org/maven2/com/data-artisans/frocksdbjni/5.17.2-artisans-1.0/frocksdbjni-5.17.2-artisans-1.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause CC-BY-4.0 GPL-2.0
Requires: mvn-frocksdb-data = %{version}-%{release}
Requires: mvn-frocksdb-license = %{version}-%{release}
BuildRequires : buildreq-cmake

%description
This folder defines a REDIS-style interface for Rocksdb.
Right now it is written as a simple tag-on in the rocksdb::RedisLists class.
It implements Redis Lists, and supports only the "non-blocking operations".

%package data
Summary: data components for the mvn-frocksdb package.
Group: Data

%description data
data components for the mvn-frocksdb package.


%package license
Summary: license components for the mvn-frocksdb package.
Group: Default

%description license
license components for the mvn-frocksdb package.


%prep
%setup -q -n frocksdb-5.17.2-artisans-1.0

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-frocksdb
cp COPYING %{buildroot}/usr/share/package-licenses/mvn-frocksdb/COPYING
cp LICENSE.Apache %{buildroot}/usr/share/package-licenses/mvn-frocksdb/LICENSE.Apache
cp LICENSE.leveldb %{buildroot}/usr/share/package-licenses/mvn-frocksdb/LICENSE.leveldb
cp docs/LICENSE-DOCUMENTATION %{buildroot}/usr/share/package-licenses/mvn-frocksdb/docs_LICENSE-DOCUMENTATION
mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/data-artisans/frocksdbjni/5.17.2-artisans-1.0
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/com/data-artisans/frocksdbjni/5.17.2-artisans-1.0/frocksdbjni-5.17.2-artisans-1.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/data-artisans/frocksdbjni/5.17.2-artisans-1.0
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/com/data-artisans/frocksdbjni/5.17.2-artisans-1.0/frocksdbjni-5.17.2-artisans-1.0.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/com/data-artisans/frocksdbjni/5.17.2-artisans-1.0/frocksdbjni-5.17.2-artisans-1.0.jar
/usr/share/java/.m2/repository/com/data-artisans/frocksdbjni/5.17.2-artisans-1.0/frocksdbjni-5.17.2-artisans-1.0.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-frocksdb/COPYING
/usr/share/package-licenses/mvn-frocksdb/LICENSE.Apache
/usr/share/package-licenses/mvn-frocksdb/LICENSE.leveldb
/usr/share/package-licenses/mvn-frocksdb/docs_LICENSE-DOCUMENTATION
