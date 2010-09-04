
%define name	mimms
%define version	3.2.1
%define rel	1

Summary:	MMS stream downloader
Name:		%{name}
Version:	%{version}
Release:	%mkrel %rel
URL:		http://nongnu.org/mimms/
Source:		http://download.savannah.gnu.org/releases/mimms/%name-%version.tar.bz2
License:	GPLv3+
Group:		Video
BuildRoot:	%{_tmppath}/%{name}-root
# not noarch due to arch-specific requirement on libmms0
# BuildArch:	noarch
Requires:	python-%{name}

%description
mimms is a program designed to allow you to download streams using
the MMS protocol and save them to your computer, as opposed to
watching them live. Similar functionality is available in full media
player suites such as Xine, MPlayer, and VLC, but mimms is quick and
easy to use and, for the time being, remains a useful program.

%package -n python-%{name}
Summary:	MMS stream module for Python
Group:		System/Libraries
%py_requires -d
# used from pure python code, not linked against
Requires:	%{_lib}mms0

%description -n python-%{name}
Python module for handling of MMS streams, based on libmms.

%prep
%setup -q
%apply_patches

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS NEWS README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%files -n python-%{name}
%defattr(-,root,root)
%doc AUTHORS
%{python_sitelib}/lib%{name}
%{python_sitelib}/%{name}-*.egg-info
