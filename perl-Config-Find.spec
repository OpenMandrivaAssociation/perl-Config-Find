%define upstream_name    Config-Find
%define upstream_version 0.26

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Win32\\)'
%else
%define _requires_exceptions perl(Win32)
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Find configuration files
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Config/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(File::HomeDir)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Which)
BuildArch:	noarch

%description
Every OS has different rules for configuration files placement, this module
allows to easily find and create your app configuration files following
those rules.

Config::Find references configuration files by the application name or by
the application name and the configuration file name when the app uses
several application files, i.e 'emacs', 'profile', 'apache/httpd',
'apache/ssl'.

By default the $0 value is used to generate the configuration file name. To
define it explicitly the keywords 'name' or 'names' have to be used:

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.260.0-3mdv2011.0
+ Revision: 654897
- rebuild for updated spec-helper

* Sun Jan 03 2010 Jérôme Quelin <jquelin@mandriva.org> 0.260.0-2mdv2011.0
+ Revision: 485906
- removing bogus requires:

  + Michael Scherer <misc@mandriva.org>
    - do not Requires Win32

* Tue Nov 17 2009 Jérôme Quelin <jquelin@mandriva.org> 0.260.0-1mdv2010.1
+ Revision: 466756
- import perl-Config-Find


* Tue Nov 17 2009 cpan2dist 0.26-1mdv
- initial mdv release, generated with cpan2dist
