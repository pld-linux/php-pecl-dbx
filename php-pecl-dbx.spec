%define		_modname	dbx
%define		_status		stable

Summary:	%{_modname} - database abstraction functions
Summary(pl):	%{_modname} - funkcje abstrakcji baz danych
Name:		php-pecl-%{_modname}
Version:	1.1.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	82d1091c75e047c4a8f9aea7b279e13b
URL:		http://pecl.php.net/package/dbx/
BuildRequires:	libtool
BuildRequires:	php-devel >= 3:5.0.0
Requires:	php-common >= 3:5.0.0
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/php
%define		extensionsdir	%{_libdir}/php

%description
The dbx module is a database abstraction layer. The dbx functions
allow you to access all supported databases using a single calling
convention. The dbx-functions themselves do not interface directly to
the databases, but interface to the modules that are used to support
these databases.

The currently supported databases are MySQL, ODBC, Oracle (oci8), MS
SQL Server, PostgreSQL, FrontBase, Sybase-CT and SQLite.

In PECL status of this extension is: %{_status}.

%description -l pl
Modu³ dbx to warstwa abstrakcji baz danych. Funkcje dbx pozwalaj± na
dostêp do wspieranych baz danych przy u¿yciu spójnej konwencji.
Funkcje dbx jako takie s± interfejsem bazy danych, ale interfejsem
modu³ów do obs³ugi baz danych.

Aktualnie wspierane bazy danych to MySQL, ODBC, Oracle (oci8), MS SQL
Server, PostgreSQL, FrontBase, Sybase-CT oraz SQLite.

To rozszerzenie ma w PECL status: %{_status}.

%prep
%setup -q -c

%build
cd %{_modname}-%{version}
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{extensionsdir}

install %{_modname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{extensionsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/php-module-install install %{_modname} %{_sysconfdir}/php-cgi.ini

%preun
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove %{_modname} %{_sysconfdir}/php-cgi.ini
fi

%files
%defattr(644,root,root,755)
%doc %{_modname}-%{version}/CREDITS
%attr(755,root,root) %{extensionsdir}/%{_modname}.so
