# Automatically generated by perl-Net-Ping.spec.PL
%define class Net
%define subclass Ping
%define version 2.17
%define release 1
%define defperlver 5.6.1

# Derived values
%define real_name %{class}-%{subclass}
%define name perl-%{real_name}
%define perlver %(rpm -q perl --queryformat '%%{version}' 2> /dev/null || echo %{defperlver})

Summary:        Perl module %{class}::%{subclass}
Name:           %{name}
Version:        %{version}
Release:        %{release}
Group:          Development/Perl
License:        See documentation
Source:         http://www.cpan.org/modules/by-module/%{class}/%{real_name}-%{version}.tar.gz
Url:            http://search.cpan.org/search?dist=%{real_name}
Vendor:         Rob Brown <bbb@cpan.org>
Packager:       Michael McLagan <michael.mclagan@linux.org>
BuildRequires:  perl
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-buildroot-%(id -u -n)/
Requires:       perl = %{perlver}
Provides:       %{real_name}

%description
Perl module which implements the %{class}::%{subclass} class.

# Provide perl-specific find-{provides,requires}.
%define __find_provides /usr/lib/rpm/find-provides.perl
%define __find_requires /usr/lib/rpm/find-requires.perl

%prep
%setup -q -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL
make OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall PREFIX=$RPM_BUILD_ROOT%{_prefix}
[ -x /usr/lib/rpm/brp-compress ] && /usr/lib/rpm/brp-compress
find $RPM_BUILD_ROOT%{prefix} -type f -print | perl -ne "print if s@^$RPM_BUILD_ROOT@@g && !/perllocal|packlist|.bs/" > %{name}-filelist

%clean
cd ..
rm -rf $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_DIR/%{real_name}-%{version}

%files -f %{name}-filelist
%defattr(-,root,root)
%doc CHANGES README


%changelog
* Thu May 03 2002 Rob Brown <bbb@cpan.org>
- Compatibility changesto work with older versions of
  perl (5.005/5.6.0/5.6.1) and rpm (3.x/4.x)
* Fri Apr 19 2002 Michael McLagan <michael.mclagan@linux.org>
- Use standard naming (perl-Net-Ping)
- Reimplemented spec with my 'generic' perl module script
* Sat Apr 06 2002 Rob Brown <bbb@cpan.org>
- Hack to let this version override the default
* Thu Nov 15 2001 Rob Brown <bbb@cpan.org>
- initial creation
