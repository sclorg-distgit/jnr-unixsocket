%{?scl:%scl_package jnr-unixsocket}
%{!?scl:%global pkg_name %{name}}
%{?java_common_find_provides_and_requires}

%global baserelease 1

Name:           %{?scl_prefix}jnr-unixsocket
Version:        0.10
Release:        1.%{baserelease}%{?dist}
Summary:        Unix sockets for Java
Group:          Development/Libraries
License:        ASL 2.0
URL:            http://github.com/jnr/%{pkg_name}/
Source0:        https://github.com/jnr/%{pkg_name}/archive/%{pkg_name}-%{version}.tar.gz
Source1:	MANIFEST.MF
Patch0:		add-manifest.patch
BuildArch:      noarch


BuildRequires:  %{?scl_prefix}jnr-constants
BuildRequires:  %{?scl_prefix}jnr-enxio
BuildRequires:  %{?scl_prefix}jnr-ffi
BuildRequires:  %{?scl_prefix}jnr-posix

BuildRequires:  %{?scl_prefix_maven}maven-local
BuildRequires:  %{?scl_prefix_maven}maven-compiler-plugin
BuildRequires:  %{?scl_prefix_maven}maven-install-plugin
BuildRequires:  %{?scl_prefix_maven}maven-jar-plugin
BuildRequires:  %{?scl_prefix_maven}maven-javadoc-plugin
BuildRequires:  %{?scl_prefix_maven}maven-surefire-plugin
BuildRequires:  %{?scl_prefix_maven}maven-surefire-provider-junit

%description
Unix sockets for Java.

%package javadoc
Summary:        Javadocs for %{pkg_name}
Group:          Documentation

%description javadoc
This package contains the API documentation for %{pkg_name}.

%prep
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
set -e -x
%setup -q -n %{pkg_name}-%{pkg_name}-%{version}
%patch0
cp %{SOURCE1} .

# remove unnecessary wagon extension
%pom_xpath_remove pom:build/pom:extensions

find ./ -name '*.jar' -delete 
find ./ -name '*.class' -delete
%{?scl:EOF}


%build
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
set -e -x
%mvn_build
%{?scl:EOF}


%install
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
set -e -x
%mvn_install
%{?scl:EOF}


%files -f .mfiles
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Fri Jul 22 2016 Mat Booth <mat.booth@redhat.com> - 0.10-1.1
- Auto SCL-ise package for rh-eclipse46 collection

* Fri Feb 5 2016 Alexander Kurtakov <akurtako@redhat.com> 0.10-1
- Update to upstream 0.10 release.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Jeff Johnston <jjohnstn@redhat.com> 0.8-3
- Add MANIFEST.MF.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 5 2015 Alexander Kurtakov <akurtako@redhat.com> 0.8-1
- Update to upstream 0.8 release.

* Fri Jun 27 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 0.2-5
- Update junit BRs (#1106960)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 0.2-3
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 11 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 0.2-1
- Initial package.