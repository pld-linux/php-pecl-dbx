%define		php_name	php%{?php_suffix}
%define		modname	dbx
%define		status		stable
Summary:	%{modname} - database abstraction functions
Summary(pl.UTF-8):	%{modname} - funkcje abstrakcji baz danych
Name:		%{php_name}-pecl-%{modname}
Version:	1.1.2
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{modname}-%{version}.tgz
# Source0-md5:	8cac1af119e6afa519853bfd3a911bbb
URL:		http://pecl.php.net/package/dbx/
BuildRequires:	%{php_name}-devel >= 4:5.0.4
BuildRequires:	rpmbuild(macros) >= 1.650
%{?requires_php_extension}
Obsoletes:	php-dbx
Provides:	php(%{modname}) = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The dbx module is a database abstraction layer. The dbx functions
allow you to access all supported databases using a single calling
convention. The dbx-functions themselves do not interface directly to
the databases, but interface to the modules that are used to support
these databases.

The currently supported databases are MySQL, ODBC, Oracle (oci8), MS
SQL Server, PostgreSQL, FrontBase, Sybase-CT and SQLite.

In PECL status of this extension is: %{status}.

%description -l pl.UTF-8
Moduł dbx to warstwa abstrakcji baz danych. Funkcje dbx pozwalają na
dostęp do wspieranych baz danych przy użyciu spójnej konwencji.
Funkcje dbx jako takie nie są bezpośrednim interfejsem do bazy danych,
ale interfejsem do modułów do obsługi baz danych.

Aktualnie wspierane bazy danych to MySQL, ODBC, Oracle (oci8), MS SQL
Server, PostgreSQL, FrontBase, Sybase-CT oraz SQLite.

To rozszerzenie ma w PECL status: %{status}.

%prep
%setup -qc
mv %{modname}-*/* .

%build
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_sysconfdir}/conf.d,%{php_extensiondir}}
install -p modules/%{modname}.so $RPM_BUILD_ROOT%{php_extensiondir}
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{modname}.ini
; Enable %{modname} extension module
extension=%{modname}.so
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
%doc CREDITS
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{modname}.ini
%attr(755,root,root) %{php_extensiondir}/%{modname}.so
