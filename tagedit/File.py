#! /bin/python3
# TagEdit - A command line metadata tag editor.
# Copyright (C) 2017 Patrick Keating <kyrvin3@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import mutagen

from .FileType       import FileType
from .FileTypeID3    import FileTypeID3
from .FileTypeMP4    import FileTypeMP4
from .FileTypeVorbis import FileTypeVorbis

def File(path: str) -> FileType:
    try:
        f = mutagen.File(path)

        if isinstance(f.tags, mutagen.id3.ID3Tags):
            return FileTypeID3(f)

        elif isinstance(f.tags, mutagen.mp4.MP4Tags):
            return FileTypeMP4(f)

        elif isinstance(f.tags, mutagen._vorbis.VCommentDict):
            return FileTypeVorbis(f)

        else:
            return None

    except mutagen.MutagenError:
        return None
