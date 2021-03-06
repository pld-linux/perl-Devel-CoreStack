%define		pdir	Devel
%define		pnam	CoreStack
Summary:	Devel::CoreStack - try to generate a stack dump from a core file
Summary(pl.UTF-8):	Devel::CoreStack - próba wygenerowania zrzutu stosu z pliku core
Name:		perl-Devel-CoreStack
Version:	1.3
Release:	7
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	483183935fcd4743a4903a183722f559
URL:		http://search.cpan.org/dist/Devel-CoreStack/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Devel::CoreStack Perl module attempts to generate a stack dump
from a core file by locating the best available debugger (if any) and
running it with the appropriate arguments and command script.

%description -l pl.UTF-8
Moduł Perla Devel::CoreStack próbuje wygenerować zrzut stosu z pliku
core poprzez zlokalizowanie najlepszego dostępnego debuggera (jeśli w
ogóle jest) i uruchomienie go z odpowiednimi parametrami.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Devel/CoreStack.pm
%{_mandir}/man3/*
