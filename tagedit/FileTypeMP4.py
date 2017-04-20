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
import mutagen.mp4 as mp4

from .FileType import FileType
from .IntTuple import IntTuple

class FileTypeMP4(FileType):

    def __init__(self, f: mutagen.FileType):
        super().__init__(f)
        assert isinstance(f.tags, mutagen.mp4.MP4Tags)
        self._tags = f.tags

    def _get_str(self, name: str) -> str:
        try:
            return '/'.join(self._tags[name]) or None
        except KeyError:
            return None

    def _get_tup(self, name: str) -> IntTuple:
        try:
            val = self._tags[name][0]
            tup = IntTuple(None)
            tup.fst = int(val[0])
            tup.snd = int(val[1])
            return tup

        except (KeyError, IndexError, ValueError):
            return None

    def _get_int(self, name: str) -> int:
        try:
            return int(self._tags[name][0])
        except (KeyError, IndexError, ValueError):
            return None

    def get_artist(self) -> str:
        return self._get_str('\xa9ART')

    def get_album_artist(self) -> str:
        return self._get_str('aART')

    def get_composer(self) -> str:
        return self._get_str('\xa9wrt')

    def get_album(self) -> str:
        return self._get_str('\xa9alb')

    def get_title(self) -> str:
        return self._get_str('\xa9nam')

    def get_genre(self) -> str:
        return self._get_str('\xa9gen')

    def get_label(self) -> str:
        return self._get_str('\xa9grp')

    def get_description(self) -> str:
        return self._get_str('desc')

    def get_track(self) -> IntTuple:
        return self._get_tup('trkn')

    def get_disc(self) -> IntTuple:
        return self._get_tup('disk')

    def get_year(self) -> int:
        try:
            for v in self._tags['\xa9day']:
                try:
                    return int(v) or None
                except ValueError:
                    pass

        except KeyError:
            return None

    def get_bpm(self) -> int:
        return self._get_int('tmpo')

    def _set_str(self, name: str, value: str):
        self._tags.pop(name, None)
        if value:
            self._tags[name] = [value]

    def _set_tup(self, name: str, tup: IntTuple):
        self._tags.pop(name, None)
        if tup:
            self._tags[name] = [(tup.fst or 0, tup.snd or 0)]

    def _set_int(self, name: str, val: int):
        self._tags.pop(name, None)
        if val:
            self._tags[name] = [val]

    def set_artist(self, artist: str):
        self._set_str('\xa9ART', artist)

    def set_album_artist(self, album_artist: str):
        self._set_str('aART', album_artist)

    def set_composer(self, composer: str):
        self._set_str('\xa9wrt', composer)

    def set_album(self, album: str):
        self._set_str('\xa9alb', album)

    def set_title(self, title: str):
        self._set_str('\xa9nam', title)

    def set_genre(self, genre: str):
        self._set_str('\xa9gen', genre)

    def set_label(self, label: str):
        self._set_str('\xa9grp', label)

    def set_description(self, desc: str):
        self._set_str('desc', desc)

    def set_track(self, track: IntTuple):
        self._set_tup('trkn', track)

    def set_disc(self, disc: IntTuple):
        self._set_tup('disk', disc)

    def set_year(self, year: int):
        self._set_str('\xa9day', str(year))

    def set_bpm(self, bpm: int):
        self._set_int('tmpo', bpm)
