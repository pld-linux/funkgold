Summary:	FNK/MOD Editor; Sound file editor
Name:		FunktrackerGOLD
Version:	1.5
Release:	2
License:	GPL
Group:		Applications/Sound
Group(pl):	Aplikacje/D¼wiêk
Source0:	http://www.downunder.net.au/~jsno/rel/unix_projects/funktrackergold-%{version}.tgz
Patch0:		funkgold.patch
Patch1:		funkgold-megaloman.patch
URL:		http://www.downunder.net.au/~jsno/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
ExclusiveArch:	i386 

%description
Mod tracking program. This is the only working MOD tracker available
for Linux at this time.

%description -l pl
Tracker plików MOD. Jest to jedyny obecnie istniej±cy MOD tracker dla
Linuksa.

%prep
%setup -q -n funkgold
%patch0 -p1 -b .asm
%patch1 -p1 -b .megaloman

%build

%{__make} clean
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/funktracker}

install funkgold $RPM_BUILD_ROOT%{_bindir}
install Songs/* $RPM_BUILD_ROOT%{_libdir}/funktracker

gzip -9nf DEVELOPERS.README FORMAT.FunktrackerGOLD FORMAT.Protracker \
	TODO WHATS-NEW

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/funkgold
%{_libdir}/funktracker
