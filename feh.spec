Summary:	Fast image viewer/indexer/montager
Summary(hu.UTF-8):	Gyors képnézegető/indexelő/montázsoló
Summary(pl.UTF-8):	Szybki program do przeglądania/indeksowania/montowania obrazów
Name:		feh
Version:	1.8
Release:	0.9
License:	BSD
Group:		X11/Applications/Graphics
Source0:	https://derf.homelinux.org/~derf/projects/feh/%{name}-%{version}.tar.bz2
# Source0-md5:	fe81334805f4da9b5f1e35b45c444a1a
URL:		https://derf.homelinux.org/~derf/projects/feh/
Source1:	%{name}-bash-completion
BuildRequires:	giblib-devel >= 1.2.4
BuildRequires:	imlib2-devel >= 1.0.0
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXt-devel
Provides:	WallpaperChanger
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
feh is a fast, lightweight image viewer which uses imlib2. It is
commandline-driven and supports multiple images through slideshows,
thumbnail browsing or multiple windows, and montages or index prints
(using truetype fonts to display file info). Advanced features include
fast dynamic zooming, progressive loading, loading via HTTP (with
reload support for watching webcams), recursive file opening
(slideshow of a directory hierarchy), and mousewheel/keyboard control.

%description -l hu.UTF-8
feh egy gyors, könnyűsúlyú képnézegető, amely az imlib2-t használja.
Parancssor-orientált és lehetséges több képet is nézni vetítés,
bélyegkép böngészés vagy több ablakban. További lehetőségek (többek
között): gyors dinamikus zoom, progresszív betöltés, HTTP protokoll
(webcam), rekurzív fájl megnyitás (könyvtár-szerkezetben diavetítés)
és egér-götgetés/billentyűzettel irányítás.

%description -l pl.UTF-8
feh jest szybką, lekką przeglądarką obrazów która wykorzystuje
bibliotekę imlib2. Jest kierowana z linii poleceń i obsługuje wiele
obrazów naraz przez "pokazy slajdów", przeglądanie miniatur lub wiele
okienek na raz, oraz montowanie obrazów lub tworzenie indeksów
(wykorzystując fonty TrueType do wyświetlania informacji o plikach).
Zaawansowane opcje zawierają szybie powiększanie, ładowanie stopniowe,
ładowanie przez HTTP (z opcją przeładowania do oglądania webcamów),
rekursywne otwieranie plików (pokaz slajdów z hierarchii katalogów),
oraz sterowanie z klawiatury/myszki (też z kółkiem).

%package bash-completion
Summary:	bash-completion to feh
Summary(pl.UTF-8):	bashowe dopełnianie linii poleceń programu feh
Group:		Applications/Shells
Requires:	bash-completion

%description bash-completion
bash-completion to feh.

%description bash-completion -l pl.UTF-8
bashowe dopełnianie linii poleceń programu feh.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix}

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d/%{name}

rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/feh
%{_mandir}/man1/*

%files bash-completion
%defattr(644,root,root,755)
%{_sysconfdir}/bash_completion.d/%{name}
