#
# Conditional build:
#
%define         qtver           6.6.0

Summary:	A simple & lightweight desktop-agnostic Qt file archiver
Summary(pl.UTF-8):	Prosty i lekki archiwizator plików niezależny od środowiska graficznego
Name:		lxqt-archiver
Version:	1.4.0
Release:	1
License:	GPL-2.0-or-later
URL:		https://lxqt.github.io/
Source0:	https://github.com/lxqt/lxqt-archiver/releases/download/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	8be174a519f9fe5512a4809671b040ce
Source1:	%{name}.appdata.xml
BuildRequires:	Qt6Widgets-devel >= %{qtver}
BuildRequires:	appstream-glib
BuildRequires:	cmake >= 3.18.0
BuildRequires:	glib2-devel >= 1:2.50.0
BuildRequires:	json-glib-devel
BuildRequires:	libfm-qt-devel >= 2.4.0
BuildRequires:	lxqt-build-tools >= 2.4.0
BuildRequires:	perl-base
BuildRequires:	qt6-linguist >= %{qtver}
BuildRequires:	xz-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A simple & lightweight desktop-agnostic Qt file archiver.

%description -l pl.UTF-8
Oparty o bibliotekę Qt, prosty i lekki archiwizator plików niezależny
od środowiska graficznego.

%prep
%setup -q

%build
%cmake -B build

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
        DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_metainfodir}/
cp %{SOURCE1} $RPM_BUILD_ROOT%{_metainfodir}/
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/*.appdata.xml

%find_lang %{name} --with-qm

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc CHANGELOG AUTHORS README.md
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/hicolor/scalable/apps/%{name}.svg
%{_metainfodir}/%{name}.appdata.xml
%dir %{_datadir}/%{name}
# required for the lang files
%dir %{_datadir}/%{name}/translations

%clean
rm -rf $RPM_BUILD_ROOT
