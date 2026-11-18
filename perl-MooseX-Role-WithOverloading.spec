#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	MooseX
%define		pnam	Role-WithOverloading
Summary:	MooseX::Role::WithOverloading - Roles which support overloading
Name:		perl-MooseX-Role-WithOverloading
Version:	0.17
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-authors/id/E/ET/ETHER/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	df0bb5ecaacdcccea121797b9825f612
URL:		http://search.cpan.org/dist/MooseX-Role-WithOverloading/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Moose >= 0.94
BuildRequires:	perl-aliased
BuildRequires:	perl-namespace-autoclean >= 0.16
BuildRequires:	perl-namespace-clean
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MooseX::Role::WithOverloading allows you to write a Moose::Role which
defines overloaded operators and allows those operator overloadings to
be composed into the classes/roles/instances it's compiled to, while
plain Moose::Roles would lose the overloading.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorarch}/MooseX
%dir %{perl_vendorarch}/MooseX/Role
%{perl_vendorarch}/MooseX/Role/WithOverloading
%{perl_vendorarch}/MooseX/Role/WithOverloading.pm
%dir %{perl_vendorarch}/auto/MooseX
%dir %{perl_vendorarch}/auto/MooseX/Role
%dir %{perl_vendorarch}/auto/MooseX/Role/WithOverloading
%attr(755,root,root) %{perl_vendorarch}/auto/MooseX/Role/WithOverloading/*.so
%{_mandir}/man3/*
