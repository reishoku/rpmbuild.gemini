
%{!?_version: %global _version %(jq -r '.[]."@google/gemini-cli"' package.json)}

Name: gemini-cli
Version: 0.17.0
Release: 1%{?dist}
Summary: An open-source AI agent that brings the power of Gemini directly into your terminal

License: Apache-2.0
URL: https://github.com/google-gemini/gemini-cli
Source0: %url/releases/download/v%{version}/gemini.js
Source10: %url/archive/refs/tags/v%{version}.tar.gz
Source20: gemini-wrapper

BuildRequires: jq
BuildRequires: tar
Requires: nodejs

%description
Gemini CLI is an open-source AI agent that brings the power of Gemini directly into your terminal.

%prep

%build

%install
tar zxf %{SOURCE10} --strip-components 1 -C .

%{__mkdir_p} %{buildroot}%{_bindir}

%{__mkdir_p} %{buildroot}%{_libexecdir}/%{name}
%{__install} -m 0755 %{SOURCE0} %{buildroot}%{_libexecdir}/%{name}/gemini.js

%{__install} -m 0755 %{SOURCE20} %{buildroot}%{_bindir}/gemini-cli

%check


%files
%{_bindir}/gemini-cli
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/gemini.js
%license LICENSE


%changelog
* Fri Nov 21 2025 KOSHIKAWA Kenichi <reishoku.misc@pm.me> - 0.17.0-1
- Update to 0.17.0

* Thu Nov 20 2025 KOSHIKAWA Kenichi <reishoku.misc@pm.me> - 0.16.0-1
- Update to 0.16.0

* Thu Nov 20 2025 KOSHIKAWA Kenichi <reishoku.misc@pm.me> - 0.15.4-1
- Update to 0.15.4

* Sun Nov 16 2025 KOSHIKAWA Kenichi <reishoku.misc@pm.me> - 0.15.3-1
- Update to 0.15.3

* Sat Nov 15 2025 KOSHIKAWA Kenichi <reishoku.misc@pm.me> - 0.15.1-1
- Initial RPM packaging for Gemini CLI

