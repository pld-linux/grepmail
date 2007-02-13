#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Mail
%define		pnam	grepmail
Summary:	grepmail - search mailboxes for a particular email
Summary(pl.UTF-8):	grepmail - wyszukaj konkretną wiadomość w plikach z pocztą
Name:		grepmail
Version:	4.80
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
# Source0-md5:	846558ef1fcca841f0b4fd455cf3ac11
URL:		http://grepmail.sourceforge.net/
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-Date-Manip
BuildRequires:	perl-TimeDate
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Grepmail searches a normal, gzip'd, bzip'd, or tzip'd mailbox for
a given regular expression, and returns those emails that match it.
Piped input is allowed, and date and size restrictions are supported.

%description -l pl.UTF-8
Grepmail przeszukuje zwykłe lub skompresowane przy użyciu gzip, bzip2
lub tzip pliki z pocztą przy użyciu wyrażenia regularnego, oraz zwraca
wiadomości, które do niego pasują. Przekazywanie na standardowe wejście
jest dozwolone, obsługiwane są ograniczenia na datę i rozmiar.

%prep
%setup -q -n %{pnam}-%{version}
%{__perl} -pi -e 's/^(require 5.003)(96;)$/$1_$2/' grepmail

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor \
	FASTREADER=0
%{__make}

%{?with_tests:LC_ALL=C %{__make} test}

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
