Summary:	Generates HTML IRC stats based on irssi logs
Summary(pl.UTF-8):	Generowanie statystyk kanału IRC w oparciu o logi irssi
Name:		irssistats
Version:	0.75
Release:	2
License:	GPL v2
Group:		Applications
Source0:	http://royale.zerezo.com/irssistats/%{name}-%{version}.tar.gz
# Source0-md5:	f3654fd292220bd9adada7ff6c7f0421
URL:		http://royale.zerezo.com/irssistats/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
irssistats is a tool that make HTML stats from irssi logfiles. The
statistics generated display many useful and funny informations about
the channel.

%description -l pl.UTF-8
irssistats to narzędzie tworzące statystyki w HTML-u z plików logów
irssi. Statystyki zawierają dużo pożytecznych i zabawnych informacji o
kanale.

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
