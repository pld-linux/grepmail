#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	grepmail
Summary:	grepmail - search mailboxes for a particular email
#Summary(pl):	
Name:		grepmail
Version:	4.72
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{version}.tar.gz
URL:		http://grepmail.sourceforge.net/
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-TimeDate
BuildRequires:	perl-Date-Manip
BuildRequires:	perl-Inline >= 0.41
BuildRequires:	perl-Inline-C >= 0.41
BuildRequires:	perl
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Grepmail searches a normal, gzip'd, bzip'd, or tzip'd mailbox for a given
regular expression, and returns those emails that match it.  Piped input
is allowed, and date and size restrictions are supported.

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{version}

%build
yes "" | perl Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README FastReader/Change*
%attr(755,root,root) %{_bindir}/*
%{perl_archlib}/Mail/Folder
%attr(755,root,root) %{perl_archlib}/auto/Mail/Folder
%{_mandir}/man?/*
