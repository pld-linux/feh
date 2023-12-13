Summary:	Fast image viewer/indexer/montager
Summary(hu.UTF-8):	Gyors képnézegető/indexelő/montázsoló
Summary(pl.UTF-8):	Szybki program do przeglądania/indeksowania/montowania obrazów
Name:		feh
Version:	3.10.1
Release:	1
License:	BSD
Group:		X11/Applications/Graphics
Source0:	https://feh.finalrewind.org/%{name}-%{version}.tar.bz2
# Source0-md5:	08446a75833a0bcb09a36e9a4c7e64df
URL:		https://feh.finalrewind.org/
# Bash completion by https://github.com/scop/bash-completion/blob/master/completions/feh
Source1:	%{name}-bash-completion
# zsh completion by https://git.finalrewind.org/zsh/plain/etc/completions/_feh
Source2:	%{name}-zsh-completion
BuildRequires:	curl-devel
BuildRequires:	imlib2-devel >= 1.0.0
BuildRequires:	libexif-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libmagic-devel
BuildRequires:	libpng-devel
BuildRequires:	sed >= 4.0
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXt-devel
Requires:	ImageMagick
Requires:	imlib2_loaders
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

%package -n bash-completion-feh
Summary:	Bash completion for feh
Summary(pl.UTF-8):	Dopełnianie parametrów feh dla powłoki Bash
Group:		Applications/Shells
Requires:	bash-completion >= 1:2.0
Requires:	%{name} = %{version}-%{release}
Obsoletes:	feh-bash-completion
BuildArch:	noarch

%description -n bash-completion-feh
Bash completion for feh.

%description -n bash-completion-feh -l pl.UTF-8
Dopełnianie parametrów feh dla powłoki Bash.

%package -n zsh-completion-feh
Summary:	ZSH completion for feh
Summary(pl.UTF-8):	Dopełnianie parametrów feh dla powłoki ZSH
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description -n zsh-completion-feh
ZSH completion for feh.

%description -n zsh-completion-feh -l pl.UTF-8
Dopełnianie parametrów feh dla powłoki ZSH.

%prep
%setup -q

%build
CFLAGS="%{rpmcflags} %{rpmcppflags}" \
LDFLAGS="%{rpmldflags}" \
%{__make} \
	CC="%{__cc}" \
	PREFIX=%{_prefix} \
	exif=1 \
	help=1 \
	inotify=1 \
	magic=1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d
install -d $RPM_BUILD_ROOT%{zsh_compdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix}

cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d/%{name}
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{zsh_compdir}/_%{name}

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%update_desktop_database

%postun
%update_icon_cache hicolor
%update_desktop_database

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog examples README.md TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/feh
%{_mandir}/man1/*.1*
%{_desktopdir}/feh.desktop
%{_iconsdir}/hicolor/48x48/apps/feh.png
%{_iconsdir}/hicolor/scalable/apps/feh.svg

%files -n bash-completion-feh
%defattr(644,root,root,755)
%{_sysconfdir}/bash_completion.d/%{name}

%files -n zsh-completion-feh
%defattr(644,root,root,755)
%{zsh_compdir}/_feh
