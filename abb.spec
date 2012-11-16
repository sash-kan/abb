Name:		abb
Version:	0.1
Release:	3
Summary:	Command-line client for abf.rosalinux.ru

Group:		System/Configuration/Packaging
License:	GPLv3+
URL:		git://github.com/sash-kan/%{name}.git
Source0:	%{name}
Source1:	%{name}rc
Source2:	readme
Source3:	gpl-3.0.txt
Requires:	bash
Requires:	git
BuildArch:	noarch

%description
abb is command-line client for <http://abf.rosalinux.ru>

%prep
%setup -qcT
cp %{SOURCE1} .
cp %{SOURCE2} .

%install
install -d %{buildroot}%{_bindir}
install %{SOURCE0} %{buildroot}%{_bindir}/

%files
%doc abbrc readme
%{_bindir}/%{name}
