Summary:	Fast image viewer/indexer/montager
Summary(pl):	Szybki program do przegl�dania/indeksowania/montowania obraz�w
Name:		feh
Version:	1.2.0
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://www.linuxbrit.co.uk/downloads/%{name}-%{version}.tar.gz
URL:		http://www.linuxbrit.co.uk/
BuildRequires:	imlib2-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	giblib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
feh is a fast, lightweight image viewer which uses imlib2. It is
commandline-driven and supports multiple images through slideshows,
thumbnail browsing or multiple windows, and montages or index prints
(using truetype fonts to display file info). Advanced features include
fast dynamic zooming, progressive loading, loading via HTTP (with
reload support for watching webcams), recursive file opening
(slideshow of a directory hierarchy), and mousewheel/keyboard control.

%description -l pl
feh jest szybk�, lekk� przegl�rk� obraz�w kt�ra wykorzystuje
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
aclocal
%{__autoconf}
%{__automake}
%configure

%{__make}

gzip -9nf AUTHORS TODO ChangeLog

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/feh
%{_mandir}/man1/*
