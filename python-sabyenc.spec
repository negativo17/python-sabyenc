%global srcname sabyenc

Name:           python-%{srcname}
Version:        3.3.6
Release:        1%{?dist}
Summary:        yEnc Module for Python modified for SABnzbd
License:        LGPLv3
URL:            https://github.com/sabnzbd/sabnzbd-yenc

Source0:        %{pypi_source}

BuildRequires:  python2-setuptools
BuildRequires:  python2-devel
BuildRequires:  gcc

Requires:       python2 >= 2.6

%global _description %{expand:
A modified the original yenc module by Alessandro Duca for use within SABnzbd.

The module was extended to do header parsing and full yEnc decoding from a
Python list of chunks, the way in which data is retrieved from usenet.}

%description %_description

%package -n python2-%{srcname}
Summary:        %{summary}
BuildRequires:  python2-devel
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}

%build
CFLAGS="%{optflags}" %py2_build

%install
%py2_install

%files -n python2-%{srcname}
%doc README.md
%{python2_sitearch}/%{srcname}.so
%{python2_sitearch}/%{srcname}-%{version}-*.egg-info

%changelog
* Sun Dec 01 2019 Simone Caronni <negativo17@gmail.com> - 3.3.5-1
- First build.
