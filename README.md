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

Add soft link to i3 config
    
    ln -s ~/dotfiles/i3config ~/.i3/config
