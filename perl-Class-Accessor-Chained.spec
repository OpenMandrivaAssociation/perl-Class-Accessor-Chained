%define upstream_name Class-Accessor-Chained
%define upstream_version 0.01

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 2

Summary:	Class-Accessor-Chained module for perl 
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-Class-Accessor
# README says it needs this, and the automatic perl requirement isn't
# being added, so here it is
Requires:	perl-Class-Accessor
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
A chained accessor is one that always returns the object when called
with parameters (to set), and the value of the field when called with
no arguments.

This module subclasses Class::Accessor in order to provide the same
mk_accessors interface.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Class/Accessor/Chained.pm
%{perl_vendorlib}/Class/Accessor/Chained
%{_mandir}/*/*
