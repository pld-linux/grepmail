#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Mail
%define	pnam	grepmail
Summary:	grepmail - search mailboxes for a particular email
Summary(pl):	grepmail - wyszukaj konkretn± wiadomo¶æ w plikach z poczt±
Name:		grepmail
Version:	4.80
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
URL:		http://grepmail.sourceforge.net/
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-TimeDate
BuildRequires:	perl-Date-Manip
BuildRequires:	perl-Inline >= 0.41
BuildRequires:	perl-Inline-C >= 0.41
%endif
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Grepmail searches a normal, gzip'd, bzip'd, or tzip'd mailbox for
a given regular expression, and returns those emails that match it.
Piped input is allowed, and date and size restrictions are supported.

%description -l pl
Grepmail przeszukuje zwyk³e lub skompresowane przy u¿yciu gzip, bzip2
lub tzip pliki z poczt± przy u¿yciu wyra¿enia regularnego, oraz zwraca
wiadomo¶ci, które do niego pasuj±.  Przekazywanie na standardowe wej¶cie
jest dozwolone, obs³ugiwane s± ograniczenia na datê i rozmiar.

%prep
%setup -q -n %{pnam}-%{version}
perl -pi -e 's/^(require 5.003)(96;)$/$1_$2/' grepmail

%build
#yes | perl Makefile.PL FASTREADER=1
perl -MExtUtils::MakeMaker -e 'WriteMakefile(NAME=>"grepmail", EXE_FILES=>["grepmail"])'
%{__make}

%{!?_without_tests:LC_ALL=C %{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README FastReader/Change*
%attr(755,root,root) %{_bindir}/*
%{perl_sitearch}/Mail/Folder
%attr(755,root,root) %{perl_sitearch}/auto/Mail/Folder
%{_mandir}/man?/*
