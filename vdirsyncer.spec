Summary:	Synchronize calendars and contacts
Name:		vdirsyncer
Version:	0.19.1
Release:	1
License:	BSD
Group:		Applications/System
Source0:	https://github.com/pimutils/vdirsyncer/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	c0f923b6905593a7430e7f0996acb6be
URL:		https://vdirsyncer.pimutils.org/
BuildRequires:	python3
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools_scm
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Vdirsyncer is a command-line tool for synchronizing calendars and
addressbooks between a variety of servers and the local filesystem.
The most popular usecase is to synchronize a server with a local
folder and use a set of other programs to change the local events and
contacts. Vdirsyncer can then synchronize those changes back to the
server.

However, vdirsyncer is not limited to synchronizing between clients
and servers. It can also be used to synchronize calendars and/or
addressbooks between two servers directly.

%prep
%setup -q

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS.rst CHANGELOG.rst CONTRIBUTING.rst LICENSE README.rst config.example
%attr(755,root,root) %{_bindir}/%{name}
%{py3_sitescriptdir}/%{name}
%{py3_sitescriptdir}/%{name}-%{version}-py3*.egg-info
