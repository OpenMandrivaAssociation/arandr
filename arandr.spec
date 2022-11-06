Summary:	Screen layout editor for xrandr 1.2 (Another XRandR gui)
Name:		arandr
URL:		http://christian.amsuess.com/tools/arandr/
Version:	0.1.10
Release:	3
Source0:	http://christian.amsuess.com/tools/arandr/files/%{name}-%{version}.tar.gz
License:	GPLv3
Group:		System/X11
BuildArch:	noarch
BuildRequires:	python-devel
BuildRequires:	python-docutils
Requires:	task-x11
Requires:	pygtk2.0

%files
%defattr(-,root,root)
%doc NEWS README TODO
%{py_puresitedir}/screenlayout
%{py_puresitedir}/*.egg-info

%{_bindir}/%{name}
%{_bindir}/unxrandr
%{_datadir}/applications/arandr.desktop
%{_datadir}/locale/
%{_mandir}/man1/*

#--------------------------------------------------------------------

%description
Provide a simple visual front end for XRandR 1.2, client
side X only (no xorg.conf involved, no pre-1.2 options).

Features

* Full controll over positioning (instead of plain "left of") with
  edge snapping

* Saving configurations as executable shell scripts (configurations
  can be loaded without using this program)

* Configuration files can be edited to include additional payload
  (like xsetwacom commands tablet PC users need when rotating), which
  is preserved when editing

* Metacity keybinding integration:

* Saved configurations can be bound to arbitrary keys via metacity
  custom commands.

* Several layouts can be bound to one key; they are cycled
  through. (Useful for "rotate" buttons on tablet PCs.)

* Main widget separated from packaged application (to facilitate
  integration with existing solutions)


%prep
%autosetup -p0

%build
%py_build

%install
%py_install

