#SPEC by Julien Catalano

%define	name	wormux
%define	version	0.8
%define alpha	alpha1
%define	release	0.alpha1.3

%define	Summary	Free (Libre) clone of Worms from Team17

Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%mkrel %{release}
License:	GPL
Group:		Games/Arcade
Url:		http://www.wormux.org/
Source0:	http://download.gna.org/wormux/%{name}-%{version}%{alpha}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}%{alpha}-%{release}-buildroot

Buildrequires:	libSDL_gfx-devel
Buildrequires:	libxml++-devel
Buildrequires:  SDL_image-devel
Buildrequires:  SDL_ttf-devel
Buildrequires:  SDL_mixer-devel
Buildrequires:  SDL_net-devel
BuildRequires:  ImageMagick
BuildRequires:	desktop-file-utils

%description
Almost everyone has heard of the Worms(R) series of games, developed by Team17.
Worms was created in 1990, the goal of the game consisting of a several teams 
of "worms" fighting to the death on a 2D map. Wormux is heavily influenced by 
all games in this genre, including Scorched Earth and Liero.

Wormux is free software clone of this game concept. Though currently under 
heavy development, it is already very playable, with lots of weapons 
(Dynamite, Baseball Bat, Teleportation, etc.). There are also lots of maps 
available for your battling pleasure! Wormux takes the genre to the next 
level, with great customisation options leading to great gameplay. There 
is a wide selection of teams, from the Aliens to the Chickens. Also, new 
battlefields can be downloaded from the Internet, making strategy an 
important part of each battle.

Though two human players are currently needed to play (unless you have 
a split personality :) the creation of artificial players and network play 
are future goals. So, start downloading today, and fight to become king of 
the garden! 

%prep
%setup -q -n %{name}-%{version}%{alpha}

%build
%configure2_5x	--bindir=%{_gamesbindir} \
		--with-datadir-name=%{_gamesdatadir}/%{name}

%make

%install
rm -rf $RPM_BUILD_ROOT

# allow this script to be executed
chmod +x install-sh

# change the name of the icon
perl -pi -e 's/wormux_128x128/wormux/' data/wormux.desktop

%makeinstall_std localedir=%{_datadir}/locale

mkdir -p $RPM_BUILD_ROOT%{_miconsdir} $RPM_BUILD_ROOT%{_iconsdir} $RPM_BUILD_ROOT%{_liconsdir}
convert -resize 16x16 data/%{name}.svg $RPM_BUILD_ROOT%{_miconsdir}/%{name}.xpm
convert -resize 32x32 data/%{name}.svg $RPM_BUILD_ROOT%{_iconsdir}/%{name}.xpm
convert -resize 48x48 data/%{name}.svg $RPM_BUILD_ROOT%{_liconsdir}/%{name}.xpm

mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat > $RPM_BUILD_ROOT%{_menudir}/%{name} << EOF
?package(%name): \
command="%{_gamesbindir}/%{name}" \
needs="X11" \
icon="%{name}.xpm" \
section="More Applications/Games/Arcade" \
title="Wormux" \
longtitle="%{Summary}" \
xdg="true"
EOF

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="Game" \
  --add-category="ArcadeGame" \
  --add-category="X-MandrivaLinux-MoreApplications-Games-Arcade" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

%find_lang %{name}

%post
%{update_menus}

%postun
%{clean_menus}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING INSTALL
%{_gamesbindir}/%{name}
%{_gamesdatadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_menudir}/%{name}
%{_miconsdir}/%{name}.xpm
%{_iconsdir}/%{name}.xpm
%{_liconsdir}/%{name}.xpm
%{_mandir}/man6/%{name}.6.bz2


