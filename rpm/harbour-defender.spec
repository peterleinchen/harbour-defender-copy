# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       harbour-defender

# >> macros
# << macros

%{!?qtc_qmake:%define qtc_qmake %qmake}
%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}
%{?qtc_builddir:%define _builddir %qtc_builddir}
Summary:    Privacy watcher
Version:    0.1
Release:    2
Group:      Qt/Qt
License:    LICENSE
URL:        http://example.org/
Source0:    %{name}-%{version}.tar.bz2
Source100:  harbour-defender.yaml
Requires:   sailfishsilica-qt5 >= 0.10.9
Requires:   pyotherside-qml-plugin-python3-qt5
BuildRequires:  pkgconfig(sailfishapp) >= 1.0.2
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  desktop-file-utils
Conflicts:      sailfishos-hosts-adblock
Conflicts:      noadshosts

%description
Configurable adblocker and privacy tuner


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qtc_qmake5 

%qtc_make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root,-)
%{_bindir}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
# >> files
# << files


%post
cp /usr/share/harbour-defender/qml/python/harbour-defender.service /etc/systemd/system/
cp /usr/share/harbour-defender/qml/python/harbour-defender.timer /etc/systemd/system/
cp /usr/share/harbour-defender/qml/python/harbour-defender.path /etc/systemd/system/
cp /usr/share/harbour-defender/qml/python/defender_default.conf /etc/defender.conf
[ -f /etc/hosts.editable ] && echo "/etc/hosts.editable exists" || cp /etc/hosts /etc/hosts.editable 2>/dev/null || :
[ -f /system/etc/hosts.editable ] && echo "/system/etc/hosts.editable exists" || cp /system/etc/hosts /system/etc/hosts.editable 2>/dev/null || :
[ -f /opt/alien/system/etc/hosts.editable ] && echo "/opt/alien/system/etc/hosts.editable exists" || cp /opt/alien/system/etc/hosts /opt/alien/system/etc/hosts.editable 2>/dev/null || :
systemctl start harbour-defender.timer
systemctl enable harbour-defender.timer
systemctl start harbour-defender.path
systemctl enable harbour-defender.path
# >> install post
# << install post

%postun
systemctl stop harbour-defender.timer
systemctl disable harbour-defender.timer
systemctl stop harbour-defender.path
systemctl disable harbour-defender.path
rm /etc/systemd/system/harbour-defender.timer
rm /etc/systemd/system/harbour-defender.path
rm /etc/systemd/system/harbour-defender.service
[ -f /etc/hosts.editable ] && mv /etc/hosts.editable /etc/hosts 2>/dev/null || echo "/etc/hosts.editable does not exist"
[ -f /system/etc/hosts.editable ] && mv /system/etc/hosts.editable /system/etc/hosts 2>/dev/null || echo "/system/etc/hosts.editable does not exist"
[ -f /opt/alien/system/etc/hosts.editable ] && mv /opt/alien/system/etc/hosts.editable /opt/alien/system/etc/hosts 2>/dev/null || echo "/opt/alien/system/etc/hosts.editable does not exist"