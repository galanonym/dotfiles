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
    
    ln -s ~/dotfiles/alacritty/alacritty.yml ~/.config/alacritty/alacritty.yml

Add soft link to bat config
    
    ln -s ~/dotfiles/bat/config ~/.config/bat/config

To install ranger dependencies follow instrucitons in ranger/ranger.md

Add soft link to ranger configs
    
    ln -s ~/dotfiles/ranger/rifle.conf ~/.config/ranger/rifle.conf
    ln -s ~/dotfiles/ranger/rc.conf ~/.config/ranger/rc.conf
    ln -s ~/dotfiles/ranger/plugins/unicode_icons.py ~/.config/ranger/plugins/unicode_icons.py

Add soft link to i3 config
    
    ln -s ~/dotfiles/i3/config ~/.config/i3/config
