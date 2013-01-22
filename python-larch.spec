Summary:	Python B-tree library
Name:		python-larch
Version:	1.20121216
Release:	1
License:	GPL v3
Group:		Libraries/Python
Source0:	http://code.liw.fi/debian/pool/main/p/python-larch/%{name}_%{version}.orig.tar.gz
# Source0-md5:	d552bfadbdb94837673970b6ea45b9f1
URL:		http://liw.fi/cliapp/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	python-tracing
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
his is an implementation of particular kind of B-tree, based
on research by Ohad Rodeh.

%prep
%setup -qn larch-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fsck-larch
%dir %{py_sitescriptdir}/larch
%{py_sitescriptdir}/larch/*.py[co]

