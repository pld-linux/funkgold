Summary:  FNK/MOD Editor; Sound file editor
Name: FunktrackerGOLD
Version: 1.5
Release: 2
Copyright: GPL
Group: Applications/Sound
Source: http://www.downunder.net.au/~jsno/rel/unix_projects/funktrackergold-1.5.tgz 
Patch0: funkgold.patch
Patch1: funkgold-megaloman.patch
URL: http://www.downunder.net.au/~jsno/
BuildRoot: /var/tmp/funkgold-root
ExclusiveArch: i386 

%description
Mod tracking program.  This is the only working MOD tracker available for Linux
at this time.

%prep
%setup -q -n funkgold
%patch0 -p1 -b .asm
%patch1 -p1 -b .megaloman

%build

make clean
make


%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/usr/bin/
mkdir -p $RPM_BUILD_ROOT/usr/lib/funktracker
 
install -m 755 -s funkgold  $RPM_BUILD_ROOT/usr/bin
install -m 644 Songs/* $RPM_BUILD_ROOT/usr/lib/funktracker 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root) 
/usr/lib/funktracker
/usr/bin/funkgold

%doc COPYING DEVELOPERS.README FORMAT.FunktrackerGOLD FORMAT.Protracker INSTALL TODO WHATS-NEW  

%changelog
* Sun May  9 1999 Peter Hanecak <hanecak@megaloman.sk>
- changes to allow non-root users to build too (%install)
- makefile patch

* Mon Aug 17 1998 Michael Maher <mike@redhat.com>
- built package 
