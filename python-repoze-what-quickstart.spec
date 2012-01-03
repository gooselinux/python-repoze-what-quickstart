%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:		python-repoze-what-quickstart
Version:	1.0.1
Release:	1%{?dist}
Summary:	A plugin for a simple authentication system with repoze.who/what
Group:		Development/Languages
License:	BSD
URL:		http://code.gustavonarea.net/repoze.what-pylons/
Source0:	http://pypi.python.org/packages/source/r/repoze.what-quickstart/repoze.what-quickstart-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch
BuildRequires:	python-devel, python-setuptools-devel
BuildRequires:	python-repoze-what >= 1.0.3, python-repoze-who, python-repoze-who-plugins-sa
BuildRequires:	python-repoze-what-plugins-sql, python-nose, python-coverage
Requires:	python-repoze-what >= 1.0.3
Requires:	python-repoze-who, python-repoze-who-plugins-sa, python-repoze-what-plugins-sql
Requires:	python-repoze-who-friendlyform

%description
This plugin allows you to take advantage of a rather simple, and usual, 
authentication and authorization setup, in which the users’ data, the groups 
and the permissions used in the application are all stored in a SQLAlchemy 
or Elixir-managed database.

Put simply, it configures repoze.who and repoze.what in one go so that you 
can have an authentication and authorization system working quickly – hence 
the name.

%prep
%setup -q -n repoze.what-quickstart-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%check
# Tests broken
# PYTHONPATH=$(pwd) nosetests

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.txt
# Need to own this dir, nothing else in our dep chain does
%{python_sitelib}/repoze/what/plugins/
%{python_sitelib}/repoze.what_quickstart*

%changelog
* Sat Sep 12 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0.1-1
- update to 1.0.1, fix typo causing broken deps

* Wed Jul 29 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0-2
- fix summary, file ownership

* Tue May 19 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0-1
- Initial package for Fedora
