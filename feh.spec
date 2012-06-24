Summary:	Fast image viewer/indexer/montager
Summary(pl):	Szybki program do przegl�dania/indeksowania/montowania obraz�w
Name:		feh
Version:	1.3.0
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://www.linuxbrit.co.uk/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	41cbfbd0c1535a7162d199cf2d448f5b
URL:		http://www.linuxbrit.co.uk/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	giblib-devel >= 1.2.4
BuildRequires:	imlib2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
feh is a fast, lightweight image viewer which uses imlib2. It is
commandline-driven and supports multiple images through slideshows,
thumbnail browsing or multiple windows, and montages or index prints
(using truetype fonts to display file info). Advanced features include
fast dynamic zooming, progressive loading, loading via HTTP (with
reload support for watching webcams), recursive file opening
(slideshow of a directory hierarchy), and mousewheel/keyboard control.

%description -l pl
feh jest szybk�, lekk� przegl�dark� obraz�w kt�ra wykorzystuje
bibliotek� imlib2. Jest kierowana z linii polece� i obs�uguje wiele
obraz�w naraz przez "pokazy slajd�w", przegl�danie miniatur lub wiele
okienek na raz, oraz montowanie obraz�w lub tworzenie indeks�w
(wykorzystuj�c fonty TrueType do wy�wietlania informacji o plikach).
Zaawansowane opcje zawieraj� szybie powi�kszanie, �adowanie stopniowe,
�adowanie przez HTTP (z opcj� prze�adowania do ogl�dania webcam�w),
rekursywne otwieranie plik�w (pokaz slajd�w z hierarchii katalog�w),
oraz sterowanie z klawiatury/myszki (te� z k�kiem).

%prep
%setup -q

%build
rm -f missing
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
%doc AUTHORS TODO ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_datadir}/feh
%{_mandir}/man1/*
