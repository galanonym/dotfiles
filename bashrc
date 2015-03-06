# my c00l aliases

alias ..='cd ..'
alias ...='cd ../..'
alias ls="ls -lahF --color=auto" #show hidden, detailed, colored

# colemak keyboard layout in command line
# fixes keypassx autotype bug
setxkbmap us -variant colemak

export EDITOR=vim

# add node export path so -g flag works without sudo
export PATH="$PATH:$HOME/npm/bin"

# add dotfiles export path for my own bash scripts
export PATH="$PATH:$HOME/dotfiles/bin"
