Summary:	Fast image viewer/indexer/montager
Summary(pl.UTF-8):	Szybki program do przeglądania/indeksowania/montowania obrazów
Name:		feh
Version:	1.3.4
Release:	1
License:	BSD
Group:		X11/Applications/Graphics
Source0:	http://www.linuxbrit.co.uk/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	3d35ba3d2f0693b019800787f1103891
URL:		http://www.linuxbrit.co.uk/feh/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	giblib-devel >= 1.2.4
BuildRequires:	imlib2-devel >= 1.0.0
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
feh is a fast, lightweight image viewer which uses imlib2. It is
commandline-driven and supports multiple images through slideshows,
thumbnail browsing or multiple windows, and montages or index prints
(using truetype fonts to display file info). Advanced features include
fast dynamic zooming, progressive loading, loading via HTTP (with
reload support for watching webcams), recursive file opening
(slideshow of a directory hierarchy), and mousewheel/keyboard control.

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

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/feh
%{_mandir}/man1/*
