%global real_name sabyenc

Name:           python-%{real_name}
Version:        4.0.2
Release:        3%{?dist}
Summary:        %{real_name} 3 - yEnc Decoding for Python 3
License:        LGPLv3

URL:            https://github.com/sabnzbd/%{real_name}/
Source0:        https://github.com/sabnzbd/%{real_name}/archive/v%{version}.tar.gz#/%{real_name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  python3-devel

%global _description %{expand:
The module was extended to do header parsing and full yEnc decoding from a
Python list of chunks, the way in which data is retrieved from Usenet. This is
particularly beneficial when SSL is enabled, which limits the size of each chunk
to 16K. Parsing these chunks in python is much more costly. Additionally, this
module releases Python's GIL during decoding, greatly increasing performance of
the overall download process.}

%description %_description

%package -n     python3-%{real_name}
Summary:        %{summary}

%description -n python3-%{real_name} %_description

%prep
%autosetup -n %{real_name}-%{version}
%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{real_name}3

%check
%py3_check_import %{real_name}3

%files -n python3-%{real_name} -f %{pyproject_files}
%license LICENSE.md
%doc README.md

%changelog
* Mon Sep 27 2021 Simone Caronni <negativo17@gmail.com> - 4.0.2-3
- Update SPEC file for recent package guidelines.

* Wed Sep 22 2021 Fabio Valentini <decathorpe@gmail.com> - 4.0.2-2
- Add BR: python3-setuptools to fix build on Fedora 35+.

* Tue Jul 14 2020 Simone Caronni <negativo17@gmail.com> - 4.0.2-1
- Update to 4.0.2.

* Tue May 26 2020 Simone Caronni <negativo17@gmail.com> - 4.0.1-1
- Update to 4.0.1.

* Sun Dec 01 2019 Simone Caronni <negativo17@gmail.com> - 3.3.5-1
- First build.
