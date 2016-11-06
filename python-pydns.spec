%define 	module	pydns
Summary:	Python module for DNS (Domain Name Service)
Name:		python-%{module}
Version:	2.3.6
Release:	1
License:	Python
Group:		Development/Languages
Source0:	http://downloads.sourceforge.net/pydns/%{module}-%{version}.tar.gz
# Source0-md5:	d12ca75251854ab6fcabbaff6909b690
URL:		http://pydns.sourceforge.net/
BuildRequires:	python-devel
BuildRequires:	rpmbuild(macros) >= 1.710
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a another release of the pydns code, as originally written by
Guido van Rossum, and with a hopefully nicer API bolted over the top
of it by Anthony Baxter.

This package contains a module (dnslib) that implements a DNS (Domain
Name Server) client, plus additional modules that define some symbolic
constants used by DNS (dnstype, dnsclass, dnsopcode).

%prep
%setup -q -n %{module}-%{version}

# Some files are latin-1 encoded but are incorrectly labelled as UTF-8 by
# upstream (see rhbz:620265)
#
# Convert them to actually be UTF-8, preserving the (now-correct) encoding
# declaration (preserving timestamps):
for file in DNS/Lib.py DNS/Type.py ; do
	iconv -f ISO-8859-1 -t UTF-8 -o $file.new $file && \
	touch -r $file $file.new && \
	mv $file.new $file
done

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS.txt PKG-INFO README-guido.txt README.txt
%dir %{py_sitescriptdir}/DNS
%{py_sitescriptdir}/DNS/*.py[co]
%{py_sitescriptdir}/pydns-%{version}-py*.egg-info
