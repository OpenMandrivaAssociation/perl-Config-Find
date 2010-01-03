%define upstream_name    Config-Find
%define upstream_version 0.26

%define _requires_exceptions perl(Win32)

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Find configuration files
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Config/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(File::HomeDir)
BuildRequires: perl(File::Spec)
BuildRequires: perl(File::Which)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


