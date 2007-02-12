Summary:	FNK/MOD sound file (module) editor
Summary(pl.UTF-8):   Edytor plików dźwiękowych (modułów) FNK/MOD
Name:		FunktrackerGOLD
Version:	1.5
Release:	2
License:	GPL
Group:		Applications/Sound
Source0:	http://www.downunder.net.au/~jsno/rel/unix_projects/funktrackergold-%{version}.tgz
Patch0:		funkgold.patch
Patch1:		funkgold-megaloman.patch
URL:		http://www.downunder.net.au/~jsno/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
ExclusiveArch:	i386

%description
Mod tracking program.

%description -l pl.UTF-8
Edytor (tracker) do plików MOD i FNK.

%prep
%setup -q -n funkgold
%patch0 -p1
%patch1 -p1

%build
%{__make} clean
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/funktracker}

install funkgold $RPM_BUILD_ROOT%{_bindir}
install Songs/* $RPM_BUILD_ROOT%{_libdir}/funktracker


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc DEVELOPERS.README FORMAT.FunktrackerGOLD FORMAT.Protracker \
	TODO WHATS-NEW
%attr(755,root,root) %{_bindir}/funkgold
%{_libdir}/funktracker
