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
import mutagen.id3 as id3

from .FileType import FileType
from .IntTuple import IntTuple

class FileTypeID3(FileType):

    def __init__(self, f: mutagen.FileType):
        super().__init__(f)
        assert isinstance(f.tags, mutagen.id3.ID3Tags)
        self._tags = f.tags

    def _get_tag(self, name: str) -> str:
        try:
            return '/'.join(str(self._tags[name]).split('\x00')) or None
        except KeyError:
            return None

    def get_artist(self) -> str:
        return self._get_tag('TPE1')

    def get_album_artist(self) -> str:
        return self._get_tag('TPE2')

    def get_composer(self) -> str:
        return self._get_tag('TPE3')

    def get_album(self) -> str:
        return self._get_tag('TALB')

    def get_title(self) -> str:
        return self._get_tag('TIT2')

    def get_genre(self) -> str:
        return self._get_tag('TCON')

    def get_label(self) -> str:
        return self._get_tag('TIT1')

    def get_description(self) -> str:
        return self._get_tag('TIT3')

    def get_track(self) -> IntTuple:
        try:
            return IntTuple('/'.join(str(self._tags['TRCK']).split('\x00'))) or None
        except (KeyError, ValueError):
            return None

    def get_disc(self) -> IntTuple:
        try:
            return IntTuple('/'.join(str(self._tags['TPOS']).split('\x00'))) or None
        except (KeyError, ValueError):
            return None

    def get_year(self) -> int:
        try:
            return int(str(self._tags['TDRC']).split('\x00')[0]) or None
        except (KeyError, ValueError, IndexError):
            return None

    def get_bpm(self) -> int:
        try:
            return int(str(self._tags['TBPM']).split('\x00')[0]) or None
        except (KeyError, ValueError, IndexError):
            return None

    def set_artist(self, artist: str):
        self._tags.pop('TPE1', None)
        if artist:
            self._tags['TPE1'] = id3.TPE1(id3.Encoding.UTF8, artist)

    def set_album_artist(self, album_artist: str):
        self._tags.pop('TPE2', None)
        if album_artist:
            self._tags['TPE2'] = id3.TPE2(id3.Encoding.UTF8, album_artist)

    def set_composer(self, composer: str):
        self._tags.pop('TPE3', None)
        if composer:
            self._tags['TPE3'] = id3.TPE3(id3.Encoding.UTF8, composer)

    def set_album(self, album: str):
        self._tags.pop('TALB', None)
        if album:
            self._tags['TALB'] = id3.TALB(id3.Encoding.UTF8, album)

    def set_title(self, title: str):
        self._tags.pop('TIT2', None)
        if title:
            self._tags['TIT2'] = id3.TIT2(id3.Encoding.UTF8, title)

    def set_genre(self, genre: str):
        self._tags.pop('TCON', None)
        if genre:
            self._tags['TCON'] = id3.TCON(id3.Encoding.UTF8, genre)

    def set_label(self, label: str):
        self._tags.pop('TIT1', None)
        if label:
            self._tags['TIT1'] = id3.TIT1(id3.Encoding.UTF8, label)

    def set_description(self, desc: str):
        self._tags.pop('TIT3', None)
        if desc:
            self._tags['TIT3'] = id3.TIT3(id3.Encoding.UTF8, desc)

    def set_track(self, track: IntTuple):
        self._tags.pop('TRCK', None)
        if track:
            self._tags['TRCK'] = id3.TRCK(id3.Encoding.UTF8, str(track))

    def set_disc(self, disc: IntTuple):
        self._tags.pop('TPOS', None)
        if disc:
            self._tags['TPOS'] = id3.TPOS(id3.Encoding.UTF8, str(disc))

    def set_year(self, year: int):
        self._tags.pop('TDRC', None)
        if year:
            self._tags['TDRC'] = id3.TDRC(id3.Encoding.UTF8, str(year))

    def set_bpm(self, bpm: int):
        self._tags.pop('TBPM', None)
        if bpm:
            self._tags['TBPM'] = id3.TBPM(id3.Encoding.UTF8, str(bpm))
