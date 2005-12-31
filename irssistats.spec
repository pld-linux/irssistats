Summary:	Generates HTML IRC stats based on irssi logs
Summary(pl):	Generuje statystyki kana³u IRC korzystaj±c z logów irssi
Name:		irssistats
Version:	0.70
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://royale.zerezo.com/irssistats/%{name}-%{version}.tar.gz
# Source0-md5:	9fd99eb73166f2e8dad2328a52e884a1
URL:		http://royale.zerezo.com/irssistats/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
irssistats is a tool that make HTML stats from irssi logfiles. The
statistics generated display many useful and funny informations about
the channel.


%description -l pl
irssistats to narzêdzie tworz±ce statystyki w HTML-u korzystaj±ce z
logów irssi. Statystyki zawieraj± du¿o po¿ytecznych i zabawnych
informacji o kanale.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	PRE=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README irssistats.sgml sample.*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/%{name}*
%{_datadir}/%{name}
