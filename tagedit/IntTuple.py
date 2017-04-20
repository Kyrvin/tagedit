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

class IntTuple:

    def __init__(self, s: str):
        if s:
            l = s.split('/')
            self.fst = int(l[0]) if len(l) > 0 else None
            self.snd = int(l[1]) if len(l) > 1 else None

        else:
            self.fst = None
            self.snd = None

    def __repr__(self):
        if self.fst:
            if self.snd:
                return "IntTuple('" + str(self.fst) + "/" + str(self.snd) + "')"
            else:
                return "IntTuple('" + str(self.fst) + "')"
        else:
            return "IntTuple(None)"

    def __str__(self):
        if self.fst:
            if self.snd:
                return str(self.fst) + "/" + str(self.snd)
            else:
                return str(self.fst)
        else:
            return ""

    def __bool__(self):
        return bool(self.fst) or bool(self.snd)
