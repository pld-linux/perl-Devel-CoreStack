%include	/usr/lib/rpm/macros.perl
%define	pdir	Devel
%define	pnam	CoreStack
Summary:	Devel::CoreStack perl module
Summary(pl):	Modu³ perla Devel::CoreStack
Name:		perl-Devel-CoreStack
Version:	1.3
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module attempts to generate a stack dump from a core file by
locating the best available debugger (if any) and running it with the
appropriate arguments and command script.

%description -l pl
Ten modu³ próbuje wygenerowaæ zrzut stosu z pliku core poprzez
zlokalizowanie najlepszego dostêpnego debuggera (je¶li w ogóle jest) i
uruchomienie go z odpowiednimi parametrami.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_privlib}/Devel/CoreStack.pm
%{_mandir}/man3/*
