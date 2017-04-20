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

from .IntTuple import IntTuple

class FileType:

    def __init__(self, f: mutagen.FileType):
        assert isinstance(f, mutagen.FileType)
        self._file = f

    def save(self):
        assert isinstance(self._file, mutagen.FileType)
        self._file.save()

    def get_artist(self) -> str:
        raise NotImplementedError

    def get_album_artist(self) -> str:
        raise NotImplementedError

    def get_composer(self) -> str:
        raise NotImplementedError

    def get_album(self) -> str:
        raise NotImplementedError

    def get_title(self) -> str:
        raise NotImplementedError

    def get_genre(self) -> str:
        raise NotImplementedError

    def get_label(self) -> str:
        raise NotImplementedError

    def get_description(self) -> str:
        raise NotImplementedError

    def get_track(self) -> IntTuple:
        raise NotImplementedError

    def get_disc(self) -> IntTuple:
        raise NotImplementedError

    def get_year(self) -> int:
        raise NotImplementedError

    def get_bpm(self) -> int:
        raise NotImplementedError

    def set_artist(self, artist: str):
        raise NotImplementedError

    def set_album_artist(self, album_artist: str):
        raise NotImplementedError

    def set_composer(self, composer: str):
        raise NotImplementedError

    def set_album(self, album: str):
        raise NotImplementedError

    def set_title(self, title: str):
        raise NotImplementedError

    def set_genre(self, genre: str):
        raise NotImplementedError

    def set_label(self, label: str):
        raise NotImplementedError

    def set_description(self, desc: str):
        raise NotImplementedError

    def set_track(self, track: IntTuple):
        raise NotImplementedError

    def set_disc(self, disc: IntTuple):
        raise NotImplementedError

    def set_year(self, year: int):
        raise NotImplementedError

    def set_bpm(self, bpm: int):
        raise NotImplementedError
