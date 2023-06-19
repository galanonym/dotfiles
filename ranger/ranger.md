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

    ob - Sort by basename
    oc - Sort by creation time
    ot - Sort by type
    oe - Sort by extension
    os - Sort by size

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
    r - Open file in chosen application

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

Archieve (plugin)

    :extract - Extract marked .zip(s) to here (plugin)
    :extract_dirs - Extract marked .zip(s) to directories (plugin)
    :compress filename - Compress marked to filename.zip

Auto open 3 tabs with bookmarks
    
    You can add startup commands in "r" alias in bashrc in dotfiles

Sort marked first, hidden last
jore file info in main pane
