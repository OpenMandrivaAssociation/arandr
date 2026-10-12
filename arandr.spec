Summary:	Screen layout editor for xrandr 1.2 (Another XRandR gui)
Name:		arandr
Version:	0.1.11
Release:	4
License:	GPLv3
Group:		System/X11
URL:		https://christian.amsuess.com/tools/arandr/
Source0:	http://christian.amsuess.com/tools/arandr/files/%{name}-%{version}.tar.gz

BuildRequires:	python%{pyver}dist(docutils)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:  desktop-file-utils
BuildRequires:  gettext

BuildSystem:    python

Requires:       python
Requires:       python%{pyver}dist(pygobject)
Requires:       xrandr

BuildArch:	noarch

%files -f %{name}.lang
%license COPYING
%doc README TODO ChangeLog NEWS
%{_bindir}/%{name}
%{_bindir}/unxrandr
%{python3_sitelib}/screenlayout/
%{python3_sitelib}/arandr-%{version}-py*.egg-info
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man1/unxrandr.1.*

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

%prep -a
# setuptools 84 no longer sets dry_run on Command subclasses.
sed -i 's/def initialize_options(self): pass/def initialize_options(self):\n        self.dry_run = False/' setup.py

%install -a
# locales
%find_lang %{name}

