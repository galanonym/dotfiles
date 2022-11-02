# Installation

Gnome Nautilus Context Menu

    sudo apt install python-nautilus python3-nautilus
    Use system install from: https://github.com/Stunkymonkey/nautilus-open-any-terminal
    

Text file previews

    Install bat from https://github.com/sharkdp/bat#installation with .deb package
    Change --style="numbers" for bat in scope.sh

Other file previews

    > sudo apt install ffmpegthumbnailer
    > sudo apt install atool

Archieve

    https://github.com/maximtrp/ranger-archives

# Ranger commands

View

    H - History back
    L - History forword

    J - Move down half page
    K - Move up half page

    zh - Toggle hidden files
    <c-h> - Toggle hidden files
    R - Refresh current directory
    i - Inspect file in ranger

File editing

    F7 - New directory
    <insert> - New file
    cw - Rename current file
    a - Append to current file
    yy - Yank / copy
    dd - Cut
    pp - Paste
    dD - Delete
    dT - Trash

Search

    / - Search
    n - Next
    N - Prev

Shell

    ! - Execute shell command
    S - Spawn new terminal in current window
    c-t - Open new terminal in current directory
    c-a-t - Open new terminal (system)

Tabs

    c-n - Create new tab
    c-w - Close current tab
    ]b - Next tab (custom)
    [b - Prev tab (custom)
    
Marking

    v - Mark selected (custom)
    V - Mark all (custom)
    c-l - Unmark all (custom)

Drag & Drop

    c-d - Open in dragon (custom)

Scout Search

    <space> - Run scout search (custom)
    <esc> - Exit scout search

Bookmarks

    m<key> - Bookmark current directory
    `<key> - Go to bookmark
    :edit ~/.local/share/ranger/bookmarks - Edit bookmarks

Archieve

    :extract - Extract marked .zip(s) to here (plugin)
    :extract_dirs - Extract marked .zip(s) to directories (plugin)
    :compress filename - Compress marked to filename.zip

Auto open 3 tabs with bookmarks
    
    You can add startup commands in "r" alias in bashrc in dotfiles

Sort marked first, hidden last
More file info in main pane
