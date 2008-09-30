Name:           kmodtool
Version:        1
Release:        5%{?dist}.1
Summary:        Tool for building kmod packages

Group:          Development/Tools
License:        MIT
URL:            http://rpmfusion.org/Packaging/KernelModules/Kmods2

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

Obsoletes:      kmod-helpers-livna < 17
# no need to provide kmod-helpers-livna as it was only in devel

Source1:        %{name}-kmodtool
Source2:        %{name}-kernel-variants


%description
This package contains tools and list of recent kernels that get used when
building kmod-packages.

%prep
echo nothing to prep


%build
echo nothing to build


%install
rm -rf $RPM_BUILD_ROOT .tmp/
# install
mkdir -p $RPM_BUILD_ROOT/%{_bindir} $RPM_BUILD_ROOT/%{_datadir}/%{name}/
install -p -m 0755 %{SOURCE1}  $RPM_BUILD_ROOT/%{_bindir}/kmodtool
install -p -m 0644 %{SOURCE2} $RPM_BUILD_ROOT/%{_datadir}/%{name}/kernel-variants

# adjust default-path
sed -i 's|^default_prefix=.*|default_prefix=%{_datadir}/%{name}/|'  \
 $RPM_BUILD_ROOT/%{_bindir}/kmodtool


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_datadir}/%{name}/

%changelog
* Tue Sep 30 2008 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 1-5.1
- rebuild for RPM Fusion

* Mon Dec 17 2007 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 1-5
- update kmodtool, so the kmod-foo-<uname -r> package does not require the 
  kmod-foo package when building for kernels that were passed with for-kernels

* Tue Dec 04 2007 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 1-4
- update kmodtool, so the kmod-foo metapackage requires the proper version 
  of the kmod-foo-<uname -r> package

* Tue Dec 04 2007 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 1-3
- update kmodtool, so the kmod-foo metapackage provides foo-kmod (which it only
  indirectly does); that should fix #1742, as kmod-foo has a shorter name now
  then kmod-foo-<uname -r>

* Sat Dec 01 2007 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 1-2
- update kmodtool, so the kmod-foo-<uname -r> package tracks in kmod-foo

* Sun Oct 28 2007 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 1-1
- split buildsys stuff out into a seperate package
- rename kmod-helpers-livna to kmodtool
- add proper obsoletes
- make package noarch

* Sat Oct 27 2007 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 16-2
- Update to latest kernels 2.6.23.1-35.fc8 2.6.21-2950.fc8xen

* Sat Oct 27 2007 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 16-1
- Update to latest kernels 2.6.23.1-35.fc8 2.6.21-2949.fc8xen

* Thu Oct 18 2007 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 15-1
- rebuilt for latest kernels

* Thu Oct 18 2007 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 14-1
- rebuilt for latest kernels

* Thu Oct 18 2007 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 13-1
- rebuilt for latest kernels

* Thu Oct 18 2007 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 12-1
- rebuilt for latest kernels

* Fri Oct 12 2007 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 11-1
- rebuilt for latest kernels

* Thu Oct 11 2007 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 10-1
- rebuilt for latest kernels

* Wed Oct 10 2007 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 9-2
- fix typo

* Wed Oct 10 2007 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 9-1
- rebuilt for latest kernels

* Sun Oct 07 2007 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 8-1
- update for 2.6.23-0.224.rc9.git6.fc8

* Sun Oct 07 2007 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 7-1
- update for 2.6.23-0.222.rc9.git1.fc8

* Wed Oct 03 2007 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 6-1
- update for 2.6.23-0.217.rc9.git1.fc8 and 2.6.21-2947.fc8xen

* Wed Oct 03 2007 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 5-1
- disable --all-but-latest stuff -- does not work as expected
- rename up2date list of kernels from "latest" to "current" as latest 
  and newest are to similar in wording; asjust script as well
- kmodtool: don't provide kernel-modules, not needed anymore with
  the new stayle and hurts

* Sun Sep 09 2007 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 4-2
- fix typos in spec file and list-kernels script
- interdependencies between the two buildsys-build packages needs to be
  arch specific as well

* Sun Sep 09 2007 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 4-1
- s/latests/latest/
- update kernel lists for rawhide and test2 kernels
- make kmod-helpers-livna-list-kernels print BuildRequires for all kernels
  as well; this is not needed and will slow build a bit as it will track 
  all the kernel-devel packages in, but that way we make sure they are really
  available in the buildsys

* Fri Sep 07 2007 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 3-4
- implement proper arch deps 

* Fri Sep 07 2007 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 3-3
- proper list of todays rawhide-kernels

* Fri Sep 07 2007 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 3-2
- fix typo in kmod-helpers-livna-latests-kernels

* Fri Sep 07 2007 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 3-1
- adjust for devel

* Sat Sep 01 2007 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 2-1
- initial package
