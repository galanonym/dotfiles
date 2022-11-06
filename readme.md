### Installation
Run git clone in ~ folder.
    
    git clone https://github.com/galanonym/dotfiles.git

### Usage
Add to ~/.bashrc to use this file

    if [ -f ~/dotfiles/bashrc ]; then
       . ~/dotfiles/bashrc
    fi

Add soft link to .gitconfig

    ln -s ~/dotfiles/gitconfig ~/.gitconfig

Add soft link to alacritty config
    
    mkdir -p ~/.config/alacritty && ln -s ~/dotfiles/alacritty/alacritty.yml ~/.config/alacritty/alacritty.yml

Add soft link to i3 config
    
    ln -s ~/dotfiles/i3/config ~/.config/i3/config

### Ranger Installation

Ranger

    sudo apt install ranger
    ranger --copy-config=all

Image previews

    sudo apt install ffmpegthumbnailer

Add soft link to ranger configs
    
    cp ~/.config/ranger/rc.conf ~/.config/ranger/rc.conf.backup
    cp ~/.config/ranger/rifle.conf ~/.config/ranger/rifle.conf.backup
    ln -s ~/dotfiles/ranger/rifle.conf ~/.config/ranger/rifle.conf
    ln -s ~/dotfiles/ranger/rc.conf ~/.config/ranger/rc.conf
    mkdir -p ~/.config/ranger/plugins
    ln -s ~/dotfiles/ranger/plugins/unicode_icons.py ~/.config/ranger/plugins/unicode_icons.py

Gnome Nautilus Context Menu

    sudo apt install python-nautilus python3-nautilus
    Use system install from: https://github.com/Stunkymonkey/nautilus-open-any-terminal
    
Text file previews

    Install bat from https://github.com/sharkdp/bat#installation with .deb package
    mkdir -p ~/.config/bat && ln -s ~/dotfiles/bat/config ~/.config/bat/config
    Change --style="numbers" for bat in ~/.config/ranger/scope.sh

Archieve

    sudo apt install atool
    https://github.com/maximtrp/ranger-archives
