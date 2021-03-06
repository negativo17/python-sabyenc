Name:           python-sabyenc
Version:        4.0.2
Release:        1%{?dist}
Summary:        SABYenc 3 - yEnc Decoding for Python 3
License:        LGPLv3

URL:            https://github.com/sabnzbd/sabyenc/
Source0:        https://github.com/sabnzbd/sabyenc/archive/v%{version}.tar.gz#/sabyenc-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  python3-devel

%description
The module was extended to do header parsing and full yEnc decoding from a
Python list of chunks, the way in which data is retrieved from Usenet. This is
particularly beneficial when SSL is enabled, which limits the size of each chunk
to 16K. Parsing these chunks in python is much more costly. Additionally, this
module releases Python's GIL during decoding, greatly increasing performance of
the overall download process.

%package -n     python3-sabyenc
Summary:        SABYenc 3 - yEnc Decoding for Python 3

%description -n python3-sabyenc
The module was extended to do header parsing and full yEnc decoding from a
Python list of chunks, the way in which data is retrieved from Usenet. This is
particularly beneficial when SSL is enabled, which limits the size of each chunk
to 16K. Parsing these chunks in python is much more costly. Additionally, this
module releases Python's GIL during decoding, greatly increasing performance of
the overall download process.

%prep
%autosetup -n sabyenc-%{version}

%build
# Remove CFLAGS=... for noarch packages (unneeded)
CFLAGS="%{optflags}" %{__python3} setup.py build

%install
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}

# Disable tests, they don't run with Python 3.8
#check
#{__python3} setup.py test


%files -n       python3-sabyenc
%license LICENSE.md
%doc README.md
%{python3_sitearch}/*

%changelog
* Tue Jul 14 2020 Simone Caronni <negativo17@gmail.com> - 4.0.2-1
- Update to 4.0.2.

* Tue May 26 2020 Simone Caronni <negativo17@gmail.com> - 4.0.1-1
- Update to 4.0.1.

* Sun Dec 01 2019 Simone Caronni <negativo17@gmail.com> - 3.3.5-1
- First build.
