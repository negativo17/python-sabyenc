%global real_name sabyenc

Name:           python-%{real_name}
Version:        5.4.3
Release:        1%{?dist}
Summary:        %{real_name} 3 - yEnc Decoding for Python 3
License:        LGPLv3

URL:            https://github.com/sabnzbd/%{real_name}/
Source0:        https://github.com/sabnzbd/%{real_name}/archive/v%{version}.tar.gz#/%{real_name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
The module was extended to do header parsing and full yEnc decoding from a
Python list of chunks, the way in which data is retrieved from Usenet. This is
particularly beneficial when SSL is enabled, which limits the size of each chunk
to 16K. Parsing these chunks in python is much more costly. Additionally, this
module releases Python's GIL during decoding, greatly increasing performance of
the overall download process.

%package -n     python3-%{real_name}
Summary:        %{real_name} 3 - yEnc Decoding for Python 3

%description -n python3-%{real_name}
The module was extended to do header parsing and full yEnc decoding from a
Python list of chunks, the way in which data is retrieved from Usenet. This is
particularly beneficial when SSL is enabled, which limits the size of each chunk
to 16K. Parsing these chunks in python is much more costly. Additionally, this
module releases Python's GIL during decoding, greatly increasing performance of
the overall download process.

%prep
%autosetup -n %{real_name}-%{version}

%build
# Remove CFLAGS=... for noarch packages (unneeded)
CFLAGS="%{optflags}" %{__python3} setup.py build

%install
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}

# Disable tests, they don't run with Python 3.8
#check
#{__python3} setup.py test

%files -n       python3-%{real_name}
%license LICENSE.md
%doc README.md
%{python3_sitearch}/*

%changelog
* Thu Jun 16 2022 Simone Caronni <negativo17@gmail.com> - 5.4.3-1
- Update to 5.4.3.

* Wed Sep 22 2021 Fabio Valentini <decathorpe@gmail.com> - 4.0.2-2
- Add BR: python3-setuptools to fix build on Fedora 35+.

* Tue Jul 14 2020 Simone Caronni <negativo17@gmail.com> - 4.0.2-1
- Update to 4.0.2.

* Tue May 26 2020 Simone Caronni <negativo17@gmail.com> - 4.0.1-1
- Update to 4.0.1.

* Sun Dec 01 2019 Simone Caronni <negativo17@gmail.com> - 3.3.5-1
- First build.
