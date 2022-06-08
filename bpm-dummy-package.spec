%undefine _disable_source_fetch

Name:           bpm-dummy-package
Version:        1.2.3
Release:        1%{?dist}
Summary:        Summary here
URL:            url.to.official.website.org
Source0:        https://link.to/download.tar.gz
License:        https://link.to/terms
Requires:       pkg1, pkg2 >= 3.21, pkg3
Group:          ...
ExclusiveArch:  x86_64
%description
This is a very long description of bpm-dummy-package.

%prep
%autosetup -n bpm-dummy-package


%install
# bash commands

%files
%{_datadir}/files/and/stuff

%changelog
...
