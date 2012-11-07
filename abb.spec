name:		abb
version:	0.1
release:	1
summary:	command-line client for abf.rosalinux.ru

group:		System/Configuration/Packaging
license:	GPLv3+
url:		git://github.com/sash-kan/%{name}.git
buildarch:	noarch
source0:	%{name}
source1:	%{name}rc
source2:	readme
source3:	gpl-3.0.txt

requires:	bash

%description
abb is command-line client for <http://abf.rosalinux.ru>

%prep
%setup -qcT

%install
cp %{SOURCE1} .
cp %{SOURCE2} .
install -d %{buildroot}%{_bindir}
install %{SOURCE0} %{buildroot}%{_bindir}/

%files
%defattr(-,root,root,-)
%doc abbrc readme
%{_bindir}/%{name}
