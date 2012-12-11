%define upstream_name Class-Accessor-Chained
%define upstream_version 0.01

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Class-Accessor-Chained module for perl 
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Class::Accessor)
# README says it needs this, and the automatic perl requirement isn't
# being added, so here it is
Requires:	perl(Class::Accessor)
BuildArch:	noarch

%description
A chained accessor is one that always returns the object when called
with parameters (to set), and the value of the field when called with
no arguments.

This module subclasses Class::Accessor in order to provide the same
mk_accessors interface.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Class/Accessor/Chained.pm
%{perl_vendorlib}/Class/Accessor/Chained
%{_mandir}/*/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.10.0-2mdv2011.0
+ Revision: 680777
- mass rebuild

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.10.0-1mdv2011.0
+ Revision: 402217
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.01-4mdv2009.0
+ Revision: 241170
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.01-2mdv2008.0
+ Revision: 86068
- rebuild


* Wed Sep 13 2006 Oden Eriksson <oeriksson@mandriva.com> 0.01-1mdv2007.0
- rebuild

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 0.01-1mdk
- initial Mandriva package

