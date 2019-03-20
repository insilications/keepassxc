#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xB7A66F03B59076A8 (release@keepassxc.org)
#
Name     : keepassxc
Version  : 2.4.0
Release  : 9
URL      : https://github.com/keepassxreboot/keepassxc/releases/download/2.4.0/keepassxc-2.4.0-src.tar.xz
Source0  : https://github.com/keepassxreboot/keepassxc/releases/download/2.4.0/keepassxc-2.4.0-src.tar.xz
Source99 : https://github.com/keepassxreboot/keepassxc/releases/download/2.4.0/keepassxc-2.4.0-src.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause BSL-1.0 CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.1 LGPL-3.0 MIT
Requires: keepassxc-bin = %{version}-%{release}
Requires: keepassxc-data = %{version}-%{release}
Requires: keepassxc-lib = %{version}-%{release}
Requires: keepassxc-license = %{version}-%{release}
Requires: keepassxc-man = %{version}-%{release}
BuildRequires : argon2-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86misc-dev libXxf86vm-dev
BuildRequires : libgcrypt-dev
BuildRequires : libgpg-error-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(libsodium)
BuildRequires : qrencode-dev
BuildRequires : qtbase-dev mesa-dev
BuildRequires : qttools-dev
BuildRequires : qtx11extras-dev
BuildRequires : quazip-dev
BuildRequires : zlib-dev
Patch1: fix-build.patch

%description
# <img src="https://keepassxc.org/logo.png" width="40" height="40"/> KeePassXC
[![TeamCity Build Status](https://ci.keepassxc.org/app/rest/builds/buildType:\(project:KeepassXC\)/statusIcon)](https://ci.keepassxc.org/?guest=1) [![codecov](https://codecov.io/gh/keepassxreboot/keepassxc/branch/develop/graph/badge.svg)](https://codecov.io/gh/keepassxreboot/keepassxc)

%package bin
Summary: bin components for the keepassxc package.
Group: Binaries
Requires: keepassxc-data = %{version}-%{release}
Requires: keepassxc-license = %{version}-%{release}

%description bin
bin components for the keepassxc package.


%package data
Summary: data components for the keepassxc package.
Group: Data

%description data
data components for the keepassxc package.


%package lib
Summary: lib components for the keepassxc package.
Group: Libraries
Requires: keepassxc-data = %{version}-%{release}
Requires: keepassxc-license = %{version}-%{release}

%description lib
lib components for the keepassxc package.


%package license
Summary: license components for the keepassxc package.
Group: Default

%description license
license components for the keepassxc package.


%package man
Summary: man components for the keepassxc package.
Group: Default

%description man
man components for the keepassxc package.


%prep
%setup -q -n keepassxc-2.4.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1553119921
mkdir -p clr-build
pushd clr-build
export LDFLAGS="${LDFLAGS} -fno-lto"
%cmake .. -DWITH_XC_BROWSER=ON \
-DWITH_XC_NETWORKING=ON \
-DWITH_XC_SSHAGENT=ON \
-DWITH_XC_KEESHARE=ON \
-DWITH_XC_KEESHARE_SECURE=ON
make  %{?_smp_mflags} VERBOSE=1
popd

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
LD_LIBRARY_PATH=/usr/lib64 ctest .

%install
export SOURCE_DATE_EPOCH=1553119921
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/keepassxc
cp LICENSE.BOOST-1.0 %{buildroot}/usr/share/package-licenses/keepassxc/LICENSE.BOOST-1.0
cp LICENSE.BSD %{buildroot}/usr/share/package-licenses/keepassxc/LICENSE.BSD
cp LICENSE.CC0 %{buildroot}/usr/share/package-licenses/keepassxc/LICENSE.CC0
cp LICENSE.GPL-2 %{buildroot}/usr/share/package-licenses/keepassxc/LICENSE.GPL-2
cp LICENSE.GPL-3 %{buildroot}/usr/share/package-licenses/keepassxc/LICENSE.GPL-3
cp LICENSE.LGPL-2.1 %{buildroot}/usr/share/package-licenses/keepassxc/LICENSE.LGPL-2.1
cp LICENSE.LGPL-3 %{buildroot}/usr/share/package-licenses/keepassxc/LICENSE.LGPL-3
cp LICENSE.MIT %{buildroot}/usr/share/package-licenses/keepassxc/LICENSE.MIT
cp LICENSE.NOKIA-LGPL-EXCEPTION %{buildroot}/usr/share/package-licenses/keepassxc/LICENSE.NOKIA-LGPL-EXCEPTION
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/keepassxc
/usr/bin/keepassxc-cli
/usr/bin/keepassxc-proxy

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.keepassxc.KeePassXC.desktop
/usr/share/icons/hicolor/128x128/apps/keepassxc-dark.png
/usr/share/icons/hicolor/128x128/apps/keepassxc-locked.png
/usr/share/icons/hicolor/128x128/apps/keepassxc-unlocked.png
/usr/share/icons/hicolor/128x128/apps/keepassxc.png
/usr/share/icons/hicolor/128x128/mimetypes/application-x-keepassxc.png
/usr/share/icons/hicolor/16x16/apps/keepassxc-dark.png
/usr/share/icons/hicolor/16x16/apps/keepassxc-locked.png
/usr/share/icons/hicolor/16x16/apps/keepassxc-unlocked.png
/usr/share/icons/hicolor/16x16/apps/keepassxc.png
/usr/share/icons/hicolor/16x16/mimetypes/application-x-keepassxc.png
/usr/share/icons/hicolor/22x22/mimetypes/application-x-keepassxc.png
/usr/share/icons/hicolor/24x24/apps/keepassxc-dark.png
/usr/share/icons/hicolor/24x24/apps/keepassxc-locked.png
/usr/share/icons/hicolor/24x24/apps/keepassxc-unlocked.png
/usr/share/icons/hicolor/24x24/apps/keepassxc.png
/usr/share/icons/hicolor/256x256/apps/keepassxc-dark.png
/usr/share/icons/hicolor/256x256/apps/keepassxc-locked.png
/usr/share/icons/hicolor/256x256/apps/keepassxc-unlocked.png
/usr/share/icons/hicolor/256x256/apps/keepassxc.png
/usr/share/icons/hicolor/32x32/apps/keepassxc-dark.png
/usr/share/icons/hicolor/32x32/apps/keepassxc-locked.png
/usr/share/icons/hicolor/32x32/apps/keepassxc-unlocked.png
/usr/share/icons/hicolor/32x32/apps/keepassxc.png
/usr/share/icons/hicolor/32x32/mimetypes/application-x-keepassxc.png
/usr/share/icons/hicolor/48x48/apps/keepassxc-dark.png
/usr/share/icons/hicolor/48x48/apps/keepassxc-locked.png
/usr/share/icons/hicolor/48x48/apps/keepassxc-unlocked.png
/usr/share/icons/hicolor/48x48/apps/keepassxc.png
/usr/share/icons/hicolor/64x64/apps/keepassxc-dark.png
/usr/share/icons/hicolor/64x64/apps/keepassxc-locked.png
/usr/share/icons/hicolor/64x64/apps/keepassxc-unlocked.png
/usr/share/icons/hicolor/64x64/apps/keepassxc.png
/usr/share/icons/hicolor/64x64/mimetypes/application-x-keepassxc.png
/usr/share/icons/hicolor/scalable/apps/keepassxc-dark.svg
/usr/share/icons/hicolor/scalable/apps/keepassxc-locked.svg
/usr/share/icons/hicolor/scalable/apps/keepassxc-unlocked.svg
/usr/share/icons/hicolor/scalable/apps/keepassxc.svg
/usr/share/icons/hicolor/scalable/mimetypes/application-x-keepassxc.svg
/usr/share/keepassxc/icons/application/128x128/apps/keepassxc-dark.png
/usr/share/keepassxc/icons/application/128x128/apps/keepassxc-locked.png
/usr/share/keepassxc/icons/application/128x128/apps/keepassxc-unlocked.png
/usr/share/keepassxc/icons/application/128x128/apps/keepassxc.png
/usr/share/keepassxc/icons/application/128x128/apps/preferences-system-network-sharing.png
/usr/share/keepassxc/icons/application/128x128/mimetypes/application-x-keepassxc.png
/usr/share/keepassxc/icons/application/16x16/actions/application-exit.png
/usr/share/keepassxc/icons/application/16x16/actions/auto-type.png
/usr/share/keepassxc/icons/application/16x16/actions/configure.png
/usr/share/keepassxc/icons/application/16x16/actions/database-change-key.png
/usr/share/keepassxc/icons/application/16x16/actions/document-close.png
/usr/share/keepassxc/icons/application/16x16/actions/document-edit.png
/usr/share/keepassxc/icons/application/16x16/actions/document-encrypt.png
/usr/share/keepassxc/icons/application/16x16/actions/document-new.png
/usr/share/keepassxc/icons/application/16x16/actions/document-open.png
/usr/share/keepassxc/icons/application/16x16/actions/document-save-as.png
/usr/share/keepassxc/icons/application/16x16/actions/document-save.png
/usr/share/keepassxc/icons/application/16x16/actions/edit-clear-locationbar-ltr.png
/usr/share/keepassxc/icons/application/16x16/actions/edit-clear-locationbar-rtl.png
/usr/share/keepassxc/icons/application/16x16/actions/entry-clone.png
/usr/share/keepassxc/icons/application/16x16/actions/entry-delete.png
/usr/share/keepassxc/icons/application/16x16/actions/entry-edit.png
/usr/share/keepassxc/icons/application/16x16/actions/entry-new.png
/usr/share/keepassxc/icons/application/16x16/actions/favicon-download.png
/usr/share/keepassxc/icons/application/16x16/actions/group-delete.png
/usr/share/keepassxc/icons/application/16x16/actions/group-edit.png
/usr/share/keepassxc/icons/application/16x16/actions/group-empty-trash.png
/usr/share/keepassxc/icons/application/16x16/actions/group-new.png
/usr/share/keepassxc/icons/application/16x16/actions/help-about.png
/usr/share/keepassxc/icons/application/16x16/actions/message-close.png
/usr/share/keepassxc/icons/application/16x16/actions/paperclip.png
/usr/share/keepassxc/icons/application/16x16/actions/password-copy.png
/usr/share/keepassxc/icons/application/16x16/actions/password-generate.png
/usr/share/keepassxc/icons/application/16x16/actions/password-generator.png
/usr/share/keepassxc/icons/application/16x16/actions/password-show-off.png
/usr/share/keepassxc/icons/application/16x16/actions/password-show-on.png
/usr/share/keepassxc/icons/application/16x16/actions/system-help.png
/usr/share/keepassxc/icons/application/16x16/actions/system-search.png
/usr/share/keepassxc/icons/application/16x16/actions/url-copy.png
/usr/share/keepassxc/icons/application/16x16/actions/username-copy.png
/usr/share/keepassxc/icons/application/16x16/apps/keepassxc-dark.png
/usr/share/keepassxc/icons/application/16x16/apps/keepassxc-locked.png
/usr/share/keepassxc/icons/application/16x16/apps/keepassxc-unlocked.png
/usr/share/keepassxc/icons/application/16x16/apps/keepassxc.png
/usr/share/keepassxc/icons/application/16x16/mimetypes/application-x-keepassxc.png
/usr/share/keepassxc/icons/application/22x22/actions/auto-type.png
/usr/share/keepassxc/icons/application/22x22/actions/chronometer.png
/usr/share/keepassxc/icons/application/22x22/actions/database-change-key.png
/usr/share/keepassxc/icons/application/22x22/actions/dialog-close.png
/usr/share/keepassxc/icons/application/22x22/actions/dialog-ok.png
/usr/share/keepassxc/icons/application/22x22/actions/document-encrypt.png
/usr/share/keepassxc/icons/application/22x22/actions/document-new.png
/usr/share/keepassxc/icons/application/22x22/actions/document-open.png
/usr/share/keepassxc/icons/application/22x22/actions/document-save.png
/usr/share/keepassxc/icons/application/22x22/actions/entry-clone.png
/usr/share/keepassxc/icons/application/22x22/actions/entry-delete.png
/usr/share/keepassxc/icons/application/22x22/actions/entry-edit.png
/usr/share/keepassxc/icons/application/22x22/actions/entry-new.png
/usr/share/keepassxc/icons/application/22x22/actions/favicon-download.png
/usr/share/keepassxc/icons/application/22x22/actions/group-empty-trash.png
/usr/share/keepassxc/icons/application/22x22/actions/help-about.png
/usr/share/keepassxc/icons/application/22x22/actions/message-close.png
/usr/share/keepassxc/icons/application/22x22/actions/paperclip.png
/usr/share/keepassxc/icons/application/22x22/actions/password-copy.png
/usr/share/keepassxc/icons/application/22x22/actions/password-generate.png
/usr/share/keepassxc/icons/application/22x22/actions/password-generator.png
/usr/share/keepassxc/icons/application/22x22/actions/system-help.png
/usr/share/keepassxc/icons/application/22x22/actions/system-search.png
/usr/share/keepassxc/icons/application/22x22/actions/url-copy.png
/usr/share/keepassxc/icons/application/22x22/actions/username-copy.png
/usr/share/keepassxc/icons/application/22x22/mimetypes/application-x-keepassxc.png
/usr/share/keepassxc/icons/application/22x22/status/dialog-error.png
/usr/share/keepassxc/icons/application/22x22/status/dialog-information.png
/usr/share/keepassxc/icons/application/22x22/status/dialog-warning.png
/usr/share/keepassxc/icons/application/24x24/apps/keepassxc-dark.png
/usr/share/keepassxc/icons/application/24x24/apps/keepassxc-locked.png
/usr/share/keepassxc/icons/application/24x24/apps/keepassxc-unlocked.png
/usr/share/keepassxc/icons/application/24x24/apps/keepassxc.png
/usr/share/keepassxc/icons/application/256x256/apps/keepassxc-dark.png
/usr/share/keepassxc/icons/application/256x256/apps/keepassxc-locked.png
/usr/share/keepassxc/icons/application/256x256/apps/keepassxc-unlocked.png
/usr/share/keepassxc/icons/application/256x256/apps/keepassxc.png
/usr/share/keepassxc/icons/application/32x32/actions/application-exit.png
/usr/share/keepassxc/icons/application/32x32/actions/auto-type.png
/usr/share/keepassxc/icons/application/32x32/actions/chronometer.png
/usr/share/keepassxc/icons/application/32x32/actions/configure.png
/usr/share/keepassxc/icons/application/32x32/actions/database-change-key.png
/usr/share/keepassxc/icons/application/32x32/actions/dialog-close.png
/usr/share/keepassxc/icons/application/32x32/actions/dialog-ok.png
/usr/share/keepassxc/icons/application/32x32/actions/document-close.png
/usr/share/keepassxc/icons/application/32x32/actions/document-edit.png
/usr/share/keepassxc/icons/application/32x32/actions/document-encrypt.png
/usr/share/keepassxc/icons/application/32x32/actions/document-new.png
/usr/share/keepassxc/icons/application/32x32/actions/document-open.png
/usr/share/keepassxc/icons/application/32x32/actions/document-properties.png
/usr/share/keepassxc/icons/application/32x32/actions/document-save.png
/usr/share/keepassxc/icons/application/32x32/actions/edit-clear-locationbar-ltr.png
/usr/share/keepassxc/icons/application/32x32/actions/edit-clear-locationbar-rtl.png
/usr/share/keepassxc/icons/application/32x32/actions/entry-clone.png
/usr/share/keepassxc/icons/application/32x32/actions/entry-delete.png
/usr/share/keepassxc/icons/application/32x32/actions/entry-edit.png
/usr/share/keepassxc/icons/application/32x32/actions/entry-new.png
/usr/share/keepassxc/icons/application/32x32/actions/favicon-download.png
/usr/share/keepassxc/icons/application/32x32/actions/group-empty-trash.png
/usr/share/keepassxc/icons/application/32x32/actions/help-about.png
/usr/share/keepassxc/icons/application/32x32/actions/key-enter.png
/usr/share/keepassxc/icons/application/32x32/actions/paperclip.png
/usr/share/keepassxc/icons/application/32x32/actions/password-copy.png
/usr/share/keepassxc/icons/application/32x32/actions/password-generate.png
/usr/share/keepassxc/icons/application/32x32/actions/password-generator.png
/usr/share/keepassxc/icons/application/32x32/actions/password-show-off.png
/usr/share/keepassxc/icons/application/32x32/actions/password-show-on.png
/usr/share/keepassxc/icons/application/32x32/actions/system-help.png
/usr/share/keepassxc/icons/application/32x32/actions/system-search.png
/usr/share/keepassxc/icons/application/32x32/actions/url-copy.png
/usr/share/keepassxc/icons/application/32x32/actions/username-copy.png
/usr/share/keepassxc/icons/application/32x32/actions/view-history.png
/usr/share/keepassxc/icons/application/32x32/apps/internet-web-browser.png
/usr/share/keepassxc/icons/application/32x32/apps/keepassxc-dark.png
/usr/share/keepassxc/icons/application/32x32/apps/keepassxc-locked.png
/usr/share/keepassxc/icons/application/32x32/apps/keepassxc-unlocked.png
/usr/share/keepassxc/icons/application/32x32/apps/keepassxc.png
/usr/share/keepassxc/icons/application/32x32/apps/preferences-desktop-icons.png
/usr/share/keepassxc/icons/application/32x32/apps/utilities-terminal.png
/usr/share/keepassxc/icons/application/32x32/categories/preferences-other.png
/usr/share/keepassxc/icons/application/32x32/mimetypes/application-x-keepassxc.png
/usr/share/keepassxc/icons/application/32x32/status/security-high.png
/usr/share/keepassxc/icons/application/48x48/apps/keepassxc-dark.png
/usr/share/keepassxc/icons/application/48x48/apps/keepassxc-locked.png
/usr/share/keepassxc/icons/application/48x48/apps/keepassxc-unlocked.png
/usr/share/keepassxc/icons/application/48x48/apps/keepassxc.png
/usr/share/keepassxc/icons/application/64x64/apps/keepassxc-dark.png
/usr/share/keepassxc/icons/application/64x64/apps/keepassxc-locked.png
/usr/share/keepassxc/icons/application/64x64/apps/keepassxc-unlocked.png
/usr/share/keepassxc/icons/application/64x64/apps/keepassxc.png
/usr/share/keepassxc/icons/application/64x64/mimetypes/application-x-keepassxc.png
/usr/share/keepassxc/icons/application/scalable/apps/keepassxc-dark.svg
/usr/share/keepassxc/icons/application/scalable/apps/keepassxc-locked.svg
/usr/share/keepassxc/icons/application/scalable/apps/keepassxc-unlocked.svg
/usr/share/keepassxc/icons/application/scalable/apps/keepassxc.svg
/usr/share/keepassxc/icons/application/scalable/mimetypes/application-x-keepassxc.svg
/usr/share/keepassxc/icons/database/C00_Password.png
/usr/share/keepassxc/icons/database/C01_Package_Network.png
/usr/share/keepassxc/icons/database/C02_MessageBox_Warning.png
/usr/share/keepassxc/icons/database/C03_Server.png
/usr/share/keepassxc/icons/database/C04_Klipper.png
/usr/share/keepassxc/icons/database/C05_Edu_Languages.png
/usr/share/keepassxc/icons/database/C06_KCMDF.png
/usr/share/keepassxc/icons/database/C07_Kate.png
/usr/share/keepassxc/icons/database/C08_Socket.png
/usr/share/keepassxc/icons/database/C09_Identity.png
/usr/share/keepassxc/icons/database/C10_Kontact.png
/usr/share/keepassxc/icons/database/C11_Camera.png
/usr/share/keepassxc/icons/database/C12_IRKickFlash.png
/usr/share/keepassxc/icons/database/C13_KGPG_Key3.png
/usr/share/keepassxc/icons/database/C14_Laptop_Power.png
/usr/share/keepassxc/icons/database/C15_Scanner.png
/usr/share/keepassxc/icons/database/C16_Mozilla_Firebird.png
/usr/share/keepassxc/icons/database/C17_CDROM_Unmount.png
/usr/share/keepassxc/icons/database/C18_Display.png
/usr/share/keepassxc/icons/database/C19_Mail_Generic.png
/usr/share/keepassxc/icons/database/C20_Misc.png
/usr/share/keepassxc/icons/database/C21_KOrganizer.png
/usr/share/keepassxc/icons/database/C22_ASCII.png
/usr/share/keepassxc/icons/database/C23_Icons.png
/usr/share/keepassxc/icons/database/C24_Connect_Established.png
/usr/share/keepassxc/icons/database/C25_Folder_Mail.png
/usr/share/keepassxc/icons/database/C26_FileSave.png
/usr/share/keepassxc/icons/database/C27_NFS_Unmount.png
/usr/share/keepassxc/icons/database/C28_QuickTime.png
/usr/share/keepassxc/icons/database/C29_KGPG_Term.png
/usr/share/keepassxc/icons/database/C30_Konsole.png
/usr/share/keepassxc/icons/database/C31_FilePrint.png
/usr/share/keepassxc/icons/database/C32_FSView.png
/usr/share/keepassxc/icons/database/C33_Run.png
/usr/share/keepassxc/icons/database/C34_Configure.png
/usr/share/keepassxc/icons/database/C35_KRFB.png
/usr/share/keepassxc/icons/database/C36_Ark.png
/usr/share/keepassxc/icons/database/C37_KPercentage.png
/usr/share/keepassxc/icons/database/C38_Samba_Unmount.png
/usr/share/keepassxc/icons/database/C39_History.png
/usr/share/keepassxc/icons/database/C40_Mail_Find.png
/usr/share/keepassxc/icons/database/C41_VectorGfx.png
/usr/share/keepassxc/icons/database/C42_KCMMemory.png
/usr/share/keepassxc/icons/database/C43_EditTrash.png
/usr/share/keepassxc/icons/database/C44_KNotes.png
/usr/share/keepassxc/icons/database/C45_Cancel.png
/usr/share/keepassxc/icons/database/C46_Help.png
/usr/share/keepassxc/icons/database/C47_KPackage.png
/usr/share/keepassxc/icons/database/C48_Folder.png
/usr/share/keepassxc/icons/database/C49_Folder_Blue_Open.png
/usr/share/keepassxc/icons/database/C50_Folder_Tar.png
/usr/share/keepassxc/icons/database/C51_Decrypted.png
/usr/share/keepassxc/icons/database/C52_Encrypted.png
/usr/share/keepassxc/icons/database/C53_Apply.png
/usr/share/keepassxc/icons/database/C54_Signature.png
/usr/share/keepassxc/icons/database/C55_Thumbnail.png
/usr/share/keepassxc/icons/database/C56_KAddressBook.png
/usr/share/keepassxc/icons/database/C57_View_Text.png
/usr/share/keepassxc/icons/database/C58_KGPG.png
/usr/share/keepassxc/icons/database/C59_Package_Development.png
/usr/share/keepassxc/icons/database/C60_KFM_Home.png
/usr/share/keepassxc/icons/database/C61_Services.png
/usr/share/keepassxc/icons/database/C62_Tux.png
/usr/share/keepassxc/icons/database/C63_Feather.png
/usr/share/keepassxc/icons/database/C64_Apple.png
/usr/share/keepassxc/icons/database/C65_W.png
/usr/share/keepassxc/icons/database/C66_Money.png
/usr/share/keepassxc/icons/database/C67_Certificate.png
/usr/share/keepassxc/icons/database/C68_BlackBerry.png
/usr/share/keepassxc/translations/keepassx_ar.qm
/usr/share/keepassxc/translations/keepassx_bn.qm
/usr/share/keepassxc/translations/keepassx_ca.qm
/usr/share/keepassxc/translations/keepassx_cs.qm
/usr/share/keepassxc/translations/keepassx_da.qm
/usr/share/keepassxc/translations/keepassx_de.qm
/usr/share/keepassxc/translations/keepassx_el.qm
/usr/share/keepassxc/translations/keepassx_en_GB.qm
/usr/share/keepassxc/translations/keepassx_en_US.qm
/usr/share/keepassxc/translations/keepassx_es.qm
/usr/share/keepassxc/translations/keepassx_eu.qm
/usr/share/keepassxc/translations/keepassx_fi.qm
/usr/share/keepassxc/translations/keepassx_fr.qm
/usr/share/keepassxc/translations/keepassx_he.qm
/usr/share/keepassxc/translations/keepassx_hr_HR.qm
/usr/share/keepassxc/translations/keepassx_hu.qm
/usr/share/keepassxc/translations/keepassx_id.qm
/usr/share/keepassxc/translations/keepassx_is_IS.qm
/usr/share/keepassxc/translations/keepassx_it.qm
/usr/share/keepassxc/translations/keepassx_ja.qm
/usr/share/keepassxc/translations/keepassx_kk.qm
/usr/share/keepassxc/translations/keepassx_ko.qm
/usr/share/keepassxc/translations/keepassx_la.qm
/usr/share/keepassxc/translations/keepassx_lt.qm
/usr/share/keepassxc/translations/keepassx_lv.qm
/usr/share/keepassxc/translations/keepassx_nb.qm
/usr/share/keepassxc/translations/keepassx_nl_NL.qm
/usr/share/keepassxc/translations/keepassx_pl.qm
/usr/share/keepassxc/translations/keepassx_pt.qm
/usr/share/keepassxc/translations/keepassx_pt_BR.qm
/usr/share/keepassxc/translations/keepassx_pt_PT.qm
/usr/share/keepassxc/translations/keepassx_ro.qm
/usr/share/keepassxc/translations/keepassx_ru.qm
/usr/share/keepassxc/translations/keepassx_sk.qm
/usr/share/keepassxc/translations/keepassx_sl_SI.qm
/usr/share/keepassxc/translations/keepassx_sr.qm
/usr/share/keepassxc/translations/keepassx_sv.qm
/usr/share/keepassxc/translations/keepassx_th.qm
/usr/share/keepassxc/translations/keepassx_tr.qm
/usr/share/keepassxc/translations/keepassx_uk.qm
/usr/share/keepassxc/translations/keepassx_zh_CN.qm
/usr/share/keepassxc/translations/keepassx_zh_TW.qm
/usr/share/keepassxc/wizard/background-pixmap.png
/usr/share/keepassxc/wordlists/eff_large.wordlist
/usr/share/metainfo/org.keepassxc.KeePassXC.appdata.xml
/usr/share/mime-packages/keepassxc.xml

%files lib
%defattr(-,root,root,-)
/usr/lib64/keepassxc/libkeepassx-autotype-xcb.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/keepassxc/LICENSE.BOOST-1.0
/usr/share/package-licenses/keepassxc/LICENSE.BSD
/usr/share/package-licenses/keepassxc/LICENSE.CC0
/usr/share/package-licenses/keepassxc/LICENSE.GPL-2
/usr/share/package-licenses/keepassxc/LICENSE.GPL-3
/usr/share/package-licenses/keepassxc/LICENSE.LGPL-2.1
/usr/share/package-licenses/keepassxc/LICENSE.LGPL-3
/usr/share/package-licenses/keepassxc/LICENSE.MIT
/usr/share/package-licenses/keepassxc/LICENSE.NOKIA-LGPL-EXCEPTION

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/keepassxc-cli.1
