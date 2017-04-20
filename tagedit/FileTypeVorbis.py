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

from .FileType import FileType
from .IntTuple import IntTuple

class FileTypeVorbis(FileType):

    def __init__(self, f: mutagen.FileType):
        super().__init__(f)
        assert isinstance(f.tags, mutagen._vorbis.VCommentDict)
        self._tags = f.tags

    def get_artist(self) -> str:
        return '/'.join(self._tags.get('ARTIST', [])) or None

    def get_album_artist(self) -> str:
        return '/'.join(self._tags.get('ALBUMARTIST', [])) or None

    def get_composer(self) -> str:
        return '/'.join(self._tags.get('COMPOSER', [])) or None

    def get_album(self) -> str:
        return '/'.join(self._tags.get('ALBUM', [])) or None

    def get_title(self) -> str:
        return '/'.join(self._tags.get('TITLE', [])) or None

    def get_genre(self) -> str:
        return '/'.join(self._tags.get('GENRE', [])) or None

    def get_label(self) -> str:
        return '/'.join(self._tags.get('LABEL', [])) or None

    def get_description(self) -> str:
        return '/'.join(self._tags.get('DESCRIPTION', [])) or None

    def get_track(self) -> IntTuple:
        for s in self._tags.get('TRACKNUMBER', []):
            try:
                return IntTuple(s) or None
            except ValueError:
                pass

        return None

    def get_disc(self) -> IntTuple:
        for s in self._tags.get('DISCNUMBER', []):
            try:
                return IntTuple(s) or None
            except ValueError:
                pass

        return None

    def get_year(self) -> int:
        for d in self._tags.get('DATE', []):
            try:
                return int(d) or None
            except ValueError:
                pass

        return None

    def get_bpm(self) -> int:
        for b in self._tags.get('BPM', []):
            try:
                return int(b) or None
            except ValueError:
                pass

        return None

    def set_artist(self, artist: str):
        self._tags['ARTIST'] = [artist] if artist else []

    def set_album_artist(self, album_artist: str):
        self._tags['ALBUMARTIST'] = [album_artist] if album_artist else []

    def set_composer(self, composer: str):
        self._tags['COMPOSER'] = [composer] if composer else []

    def set_album(self, album: str):
        self._tags['ALBUM'] = [album] if album else []

    def set_title(self, title: str):
        self._tags['TITLE'] = [title] if title else []

    def set_genre(self, genre: str):
        self._tags['GENRE'] = [genre] if genre else []

    def set_label(self, label: str):
        self._tags['LABEL'] = [label] if label else []

    def set_description(self, desc: str):
        self._tags['DESCRIPTION'] = [desc] if desc else []

    def set_track(self, track: IntTuple):
        self._tags['TRACKNUMBER'] = [str(track)] if track else []

    def set_disc(self, disc: IntTuple):
        self._tags['DISCNUMBER'] = [str(disc)] if disc else []

    def set_year(self, year: int):
        self._tags['DATE'] = [str(year)] if year else []

    def set_bpm(self, bpm: int):
        self._tags['BPM'] = [str(bpm)] if bpm else []
