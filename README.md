### Installation
Run git clone in ~ folder.

### Usage
Add to ~/.bashrc to use this file

    if [ -f ~/dotfiles/bashrc]; then
       . ~/dotfiles/bashrc
    fi

Add soft link to .gitconfig

    ln -s ~/dotfiles/gitconfig .gitconfig
