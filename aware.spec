#	environment variable AWARE_HOME must point at build directory
#	mdns,rrdtool,sqlite,mysql selection at configure
#	unknown BR, missing Summary(pl) and description(pl)
#	project looks interesting but needs time and work :)
Summary:	Asynchronous Event Framework for Responsive Applications, System Control and Monitoring
Summary(pl):	-
Name:		aware
Version:	0.11.1
Release:	0.1
License:	GPL
Group:		Applications/Networking
Source0:	http://www.elegant-software.com/software/aware/archive/%{name}-%{version}.src.tgz
# Source0-md5:	a3f8323cea47c2a2ef22ae2194b21f68
URL:		http://www.elegant-software.com/software/aware/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Aware is a high performance distributed event processing 
framework built for systems management. It comes with probes
for common network services and system resources. 
Additionally, Aware allows the cross-correllation of many 
different streams of information, and includes a Web-based 
reporting interface.

%description -l pl

%prep
%setup -q -n %{name}-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install doc/man/* $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES EXTERNAL_PACKAGES FAQ HOWTO IDEAS MAINTAINERS PACKAGE_INFO README SECURITY TODO
