#SPEC by Julien Catalano

Summary:	Free (Libre) clone of Worms from Team17
Name:		wormux
Version:	0.8.1
Release:	%mkrel 1
License:	GPLv2+
Group:		Games/Arcade
Url:		http://www.wormux.org/
Source0:	http://download.gna.org/wormux/%{name}-%{version}.tar.bz2
BuildRequires:	fribidi-devel
Buildrequires:	libSDL_gfx-devel
Buildrequires:	libxml++-devel
Buildrequires:	SDL_image-devel
Buildrequires:	SDL_ttf-devel
Buildrequires:	SDL_mixer-devel
Buildrequires:	SDL_net-devel
BuildRequires:	imagemagick
BuildRequires:	libpng-devel
BuildRequires:	libcurl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
%setup -q -n %{name}-%{version}

%build
#(tpg) get rid of -Werror
sed -i -e 's/-Werror//' src/Makefile.am

%configure2_5x	\
	--bindir=%{_gamesbindir} \
	--with-datadir-name=%{_gamesdatadir}/%{name} \
	--disable-rpath \
	--enable-fribidi

#(tpg) get rid of -Werror
sed -i -e 's/-Werror//' src/Makefile.in

%make

%install
rm -rf %{buildroot}

# allow this script to be executed
chmod +x install-sh

# drop icon extension
perl -pi -e 's/.png//g' data/wormux.desktop

%makeinstall_std localedir=%{_datadir}/locale

%find_lang %{name}

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_gamesbindir}/%{name}
%{_gamesdatadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}_128x128.png
%{_mandir}/man6/%{name}.*
