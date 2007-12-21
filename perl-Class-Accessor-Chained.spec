%define real_name Class-Accessor-Chained

Summary:	Class-Accessor-Chained module for perl 
Name:		perl-%{real_name}
Version:	0.01
Release:	%mkrel 2
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel, perl-Class-Accessor
# README says it needs this, and the automatic perl requirement isn't
# being added, so here it is
Requires:	perl-Class-Accessor
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
A chained accessor is one that always returns the object when called
with parameters (to set), and the value of the field when called with
no arguments.

This module subclasses Class::Accessor in order to provide the same
mk_accessors interface.

%prep
%setup -q -n %{real_name}-%{version} 

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


