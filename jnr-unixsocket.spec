%{?scl:%scl_package jnr-unixsocket}
%{!?scl:%global pkg_name %{name}}
%{?java_common_find_provides_and_requires}

Name:           %{?scl_prefix}jnr-unixsocket
Version:        0.8
Release:        2.1%{?dist}
Summary:        Unix sockets for Java
Group:          Development/Libraries
License:        ASL 2.0
URL:            http://github.com/jnr/%{pkg_name}/
Source0:        https://github.com/jnr/%{pkg_name}/archive/%{version}.tar.gz
Source1:	MANIFEST.MF
Patch0:		add-manifest.patch
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}jnr-constants
BuildRequires:  %{?scl_prefix}jnr-enxio
BuildRequires:  %{?scl_prefix}jnr-ffi
BuildRequires:  %{?scl_prefix}jnr-posix

BuildRequires:  %{?scl_prefix_java_common}maven-local
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
%setup -q -n %{pkg_name}-%{version}
%patch0
cp %{SOURCE1} .

# remove unnecessary wagon extension
%pom_xpath_remove pom:build/pom:extensions

find ./ -name '*.jar' -delete 
find ./ -name '*.class' -delete

%{?scl:EOF}

%build
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%doc LICENSE
%dir %{_javadir}/%{pkg_name}
%dir %{_mavenpomdir}/%{pkg_name}

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Thu Aug 27 2015 Mat Booth <mat.booth@redhat.com> - 0.8-2.1
- Fix unowned directories

* Tue Jun 30 2015 Jeff Johnston <jjohnstn@redhat.com> 0.8-2
- SCL-ize package.

* Tue Jun 30 2015 Jeff Johnston <jjohnstn@redhat.com> 0.8-1
- Initial import from rawhide.
