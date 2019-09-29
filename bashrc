# my c00l aliases

alias ..="cd .."
alias ...="cd ../.."
alias ls="LC_COLLATE=C ls -lahF --color=auto --quoting-style=literal" #show hidden, detailed, colored, without quotes
alias grep="grep --color" 
alias rg="rg --context 2 --smart-case"

# colemak keyboard layout in command line
# fixes keypassx autotype bug
# setxkbmap us -variant colemak

export EDITOR=vim

# add node export path so -g flag works without sudo
export PATH="$PATH:$HOME/npm/bin"

# add dotfiles export path for my own bash scripts
export PATH="$PATH:$HOME/dotfiles/bin"

# remove duplicates from history
export HISTCONTROL=ignoreboth:erasedups
