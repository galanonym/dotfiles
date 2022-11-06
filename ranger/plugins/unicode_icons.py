# Unicode Icons in Ranger File Manager
#
# How to install?
# https://gist.github.com/marcbelmont/c12d2fd2519a372d3b347f665b37e74a#gistcomment-3240106

from __future__ import absolute_import, division, print_function

from itertools import repeat

import ranger.api
from ranger.core.linemode import LinemodeBase

# https://unicode.org/emoji/charts/full-emoji-list.html
EXTENSIONS = {}
for extensions, icon in [
    ('py pyc pyo', '🐍'),
    ('php phtml phps', '🐘'),
    ('lua', '🌙'),
    ('love', '🧡'),
    ('liquid', '🌊'),
    ('mp3 opus ogg m4a m3u pls', '🎧'),
    ('flac wav', '🎼'),
    ('pdf', '📜'),
    ('css', '🎨'),
    ('appimage bash rc sh desktop phar apk', '🎯'),
    ('jpg jge jgeg', '📸'),
    ('png webp ico', '🗺 '),
    ('gif', '🎞️ '),
    ('xcf bmp raw', '🖌 '),
    ('vim', '🧰'),
    ('htm html', '🌎'),
    ('xml xml~ dtd', '📰'),
    ('txt rtf', '📝'),
    ('gpg lock kdbx kdb md5 md5sums keystore', '🔑'),
    ('csv xlsx log json yml', '📓'),
    ('md', '📘'),
    ('nfo info bak backup example', '❔'),
    ('img iso tga', '📀'),
    ('part', '💔'),
    ('torrent', '🔽'),
    ('jar java', '🍵'),
    ('asm pid diff dsc cpp h o s src cc', '💻'),
    ('conf cfg patch ini', '🛠️ '),
    ('deb rpm gz zip tar tgz', '📦'),
    ('sql db so sqlite sqlite3 mdb dat', '💾'),
    ('ttf otf woff woff2 eot gxf', '🔤'),
    ('exe dll', '🚽'),
    ('hs hi', '📟'),
    ('js', '🌐'),
    ('vc', '🗄️ '),
]:
    EXTENSIONS.update(dict(zip(extensions.split(), repeat(icon))))


# https://github.com/ranger/ranger/blob/081e73152a9391211770fab56676d7d974413ae6/ranger/container/fsobject.py
@ranger.api.register_linemode
class MyLinemode(LinemodeBase):
    name = "unicode_icons"

    def filetitle(self, fobj, metadata):
        if fobj.is_directory:
            icon = '📂'
        elif fobj.extension in EXTENSIONS:
            icon = EXTENSIONS[fobj.extension]
        elif fobj.is_link:
            icon = '🔗'
        elif fobj.audio:
            icon = '🎵'
        elif fobj.container:
            icon = '📦'
        elif fobj.document:
            icon = '📝'
        elif fobj.image:
            icon = '📸'
        elif fobj.video:
            icon = '📽 '
        elif 'Dockerfile' in fobj.relative_path:
            icon = '🐋'
        elif 'Makefile' in fobj.relative_path:
            icon = '🛠️ '
        elif '.env' in fobj.relative_path:
            icon = '🛠️ '
        elif '.gitignore' in fobj.relative_path:
            icon = '👓'
        elif '.ignore' in fobj.relative_path:
            icon = '👓'
        elif '.htpasswd' in fobj.relative_path:
            icon = '🔑'
        elif '.htaccess' in fobj.relative_path:
            icon = '🛠️ '
        else:
            icon = '📄'
        return (icon + ' ' if icon else '') + fobj.relative_path

    def infostring(self, fobj, metadata):
        raise NotImplementedError
