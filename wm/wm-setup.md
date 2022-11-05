# Simple WM Gnome setup

## Install
    > sudo apt install xdotool

## Settings > Keyboard Shortcuts

### Remove following keybindings: 
    Move to workspace below
    Switch applications
    Switch windows of an application
    Lock screen
    Hide window
    View split on left
    View split on right

### Add following rebindings:
    Switch windows | Alt+Tab
    Switch windows directly | Alt+\`

### Add following custom bindings:
    100% full | Super+F | xdotool getactivewindow windowsize 100% 100% windowmove 0% 0%
    50% right | Super+Right | xdotool getactivewindow windowsize 50% 100% windowmove 50% 0%
    50% left | Super+Left | xdotool getactivewindow windowsize 50% 100% windowmove 0% 0% 
    34% right | Super+. | xdotool getactivewindow windowsize 34% 100% windowmove 66% 0%
    66% left | Super+, | xdotool getactivewindow windowsize 66% 100% windowmove 0% 0%
