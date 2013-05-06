Summary:	Screen layout editor for xrandr 1.2 (Another XRandR gui)
Name:		arandr
URL:		http://christian.amsuess.com/tools/arandr/
Version:	0.1.7.1
Release:	1
Source0:	http://christian.amsuess.com/tools/arandr/files/%{name}-%{version}.tar.gz
License:	GPLv3
Group:		System/X11
BuildArch:	noarch
BuildRequires:	python-devel
BuildRequires:	python-docutils
Requires:	task-x11
Requires:	pygtk2.0

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
%setup -q

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}

%files
%defattr(-,root,root)
%doc NEWS README TODO
%{py_puresitedir}/screenlayout
%{py_puresitedir}/*.egg-info

%{_bindir}/%{name}
%{_bindir}/unxrandr
%{_datadir}/applications/arandr.desktop
%{_datadir}/locale/
%{_mandir}/man1/*.xz


%changelog
* Wed Jun 20 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.1.6-1
+ Revision: 806304
- version update 0.1.6

* Wed Nov 16 2011 Alexander Khrukin <akhrukin@mandriva.org> 0.1.5-1
+ Revision: 731184
- imported package arandr

