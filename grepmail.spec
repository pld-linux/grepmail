#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Mail
%define	pnam	grepmail
Summary:	grepmail - search mailboxes for a particular email
Summary(pl):	grepmail - wyszukaj konkretn� wiadomo�� w plikach z poczt�
Name:		grepmail
Version:	4.80
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
URL:		http://grepmail.sourceforge.net/
BuildRequires:	perl-devel >= 5.6
%if %{!?_without_tests:1}0
BuildRequires:	perl-Date-Manip
BuildRequires:	perl-TimeDate
%endif
BuildRequires:	rpm-perlprov >= 3.0.3-26
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Grepmail searches a normal, gzip'd, bzip'd, or tzip'd mailbox for
a given regular expression, and returns those emails that match it.
Piped input is allowed, and date and size restrictions are supported.

%description -l pl
Grepmail przeszukuje zwyk�e lub skompresowane przy u�yciu gzip, bzip2
lub tzip pliki z poczt� przy u�yciu wyra�enia regularnego, oraz zwraca
wiadomo�ci, kt�re do niego pasuj�.  Przekazywanie na standardowe wej�cie
jest dozwolone, obs�ugiwane s� ograniczenia na dat� i rozmiar.

%prep
%setup -q -n %{pnam}-%{version}
%{__perl} -pi -e 's/^(require 5.003)(96;)$/$1_$2/' grepmail

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor \
	FASTREADER=0
%{__make}

%{!?_without_tests:LC_ALL=C %{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
