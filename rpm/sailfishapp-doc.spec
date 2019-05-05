Name: sailfishapp-doc
Version: 1
Release: 1
Summary: Sailfish Application Documentation
Group: Documentation
License: LGPLv2.1
URL: https://github.com/sailfishos/sailfishapp-doc
Source: %{name}-%{version}.tar.bz2

%description
Documentation explaining how to create Sailfish Applications using the
libsafailfishapp support library.

%package doc
Summary: Documentation for %{name}.
BuildRequires: mer-qdoc-template

%description doc
This package contains the documentation for %{name}.

%prep
%setup -q

%build
%qmake5 -r VERSION=%{version}
make

%install
make install INSTALL_ROOT=%{buildroot}
mkdir -p %{buildroot}/%{_docdir}/%{name}
cp -R doc/html/* %{buildroot}/%{_docdir}/%{name}/

%files doc
%defattr(-,root,root,-)
%{_docdir}/%{name}

