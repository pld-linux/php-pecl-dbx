%define		_modname	dbx
%define		_status		stable
Summary:	%{_modname} - database abstraction functions
Summary(pl.UTF-8):	%{_modname} - funkcje abstrakcji baz danych
Name:		php-pecl-%{_modname}
Version:	1.1.0
Release:	8
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	82d1091c75e047c4a8f9aea7b279e13b
URL:		http://pecl.php.net/package/dbx/
BuildRequires:	php-devel >= 3:5.0.0
BuildRequires:	rpmbuild(macros) >= 1.344
%{?requires_php_extension}
Requires:	php-common >= 4:5.0.4
Obsoletes:	php-dbx
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The dbx module is a database abstraction layer. The dbx functions
allow you to access all supported databases using a single calling
convention. The dbx-functions themselves do not interface directly to
the databases, but interface to the modules that are used to support
these databases.

The currently supported databases are MySQL, ODBC, Oracle (oci8), MS
SQL Server, PostgreSQL, FrontBase, Sybase-CT and SQLite.

In PECL status of this extension is: %{_status}.

%description -l pl.UTF-8
Moduł dbx to warstwa abstrakcji baz danych. Funkcje dbx pozwalają na
dostęp do wspieranych baz danych przy użyciu spójnej konwencji.
Funkcje dbx jako takie nie są bezpośrednim interfejsem do bazy danych,
ale interfejsem do modułów do obsługi baz danych.

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
install -d $RPM_BUILD_ROOT{%{php_sysconfdir}/conf.d,%{php_extensiondir}}

install %{_modname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{php_extensiondir}
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{_modname}.ini
; Enable %{_modname} extension module
extension=%{_modname}.so
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%php_webserver_restart

%postun
if [ "$1" = 0 ]; then
	%php_webserver_restart
fi

%files
%defattr(644,root,root,755)
%doc %{_modname}-%{version}/CREDITS
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{_modname}.ini
%attr(755,root,root) %{php_extensiondir}/%{_modname}.so
