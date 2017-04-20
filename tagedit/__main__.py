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

import getopt
import sys

from .File     import File
from .FileType import FileType
from .IntTuple import IntTuple

class Getter:

    @staticmethod
    def artist():
        return Getter('get_artist', 'ARTIST')

    @staticmethod
    def albumartist():
        return Getter('get_album_artist', 'ALBUMARTIST')

    @staticmethod
    def composer():
        return Getter('get_composer', 'COMPOSER')

    @staticmethod
    def album():
        return Getter('get_album', 'ALBUM')

    @staticmethod
    def title():
        return Getter('get_title', 'TITLE')

    @staticmethod
    def genre():
        return Getter('get_genre', 'GENRE')

    @staticmethod
    def label():
        return Getter('get_label', 'LABEL')

    @staticmethod
    def description():
        return Getter('get_description', 'DESCRIPTION')

    @staticmethod
    def track():
        return Getter('get_track', 'TRACK')

    @staticmethod
    def disc():
        return Getter('get_disc', 'DISC')

    @staticmethod
    def year():
        return Getter('get_year', 'YEAR')

    @staticmethod
    def bpm():
        return Getter('get_bpm', 'BPM')

    def __init__(self, attr, key):
        self.attr = attr
        self.key = key

    def __call__(self, obj) -> (str, str):
        value = getattr(obj, self.attr)()
        return (self.key, str(value) if value else '')


class Setter:

    @staticmethod
    def artist(value):
        return Setter('set_artist', value)

    @staticmethod
    def albumartist(value):
        return Setter('set_album_artist', value)

    @staticmethod
    def composer(value):
        return Setter('set_composer', value)

    @staticmethod
    def album(value):
        return Setter('set_album', value)

    @staticmethod
    def title(value):
        return Setter('set_title', value)

    @staticmethod
    def genre(value):
        return Setter('set_genre', value)

    @staticmethod
    def label(value):
        return Setter('set_label', value)

    @staticmethod
    def description(value):
        return Setter('set_description', value)

    @staticmethod
    def track(value):
        return Setter('set_track', value)

    @staticmethod
    def disc(value):
        return Setter('set_disc', value)

    @staticmethod
    def year(value):
        return Setter('set_year', value)

    @staticmethod
    def bpm(value):
        return Setter('set_bpm', value)

    def __init__(self, attr: str, value):
        self.attr = attr
        self.value = value

    def __call__(self, obj):
        getattr(obj, self.attr)(self.value)


class TagEdit:

    version = "tagedit v0.1"
    usage = "Usage:\n"\
            "    tagedit (-h|--help)\n"\
            "    tagedit (-v|--version)\n"\
            "    tagedit [option]... <file>...\n"\
            "\n"\
            "Options:\n"\
            "  Get a tag's value.\n"\
            "    -a --artist\n"\
            "    -r --album-artist\n"\
            "    -c --composer\n"\
            "    -l --album\n"\
            "    -t --title\n"\
            "    -g --genre\n"\
            "    -p --label\n"\
            "    -s --description\n"\
            "    -n --track\n"\
            "    -k --disc\n"\
            "    -y --year\n"\
            "    -b --bpm\n"\
            "\n"\
            "  Set a tag's value.\n"\
            "    -A <value>  --set-artist=<value>\n"\
            "    -R <value>  --set-album-artist=<value>\n"\
            "    -C <value>  --set-composer=<value>\n"\
            "    -L <value>  --set-album=<value>\n"\
            "    -T <value>  --set-title=<value>\n"\
            "    -G <value>  --set-genre=<value>\n"\
            "    -P <value>  --set-label=<value>\n"\
            "    -S <value>  --set-description=<value>\n"\
            "    -N <value>  --set-track=<value>\n"\
            "    -K <value>  --set-disc=<value>\n"\
            "    -Y <value>  --set-year=<value>\n"\
            "    -B <value>  --set-bpm=<value>\n"


    shortopts="hvarcltgpsnkybA:R:C:L:T:G:P:S:N:K:Y:B:"
    longopts=["help",
              "version",
              "artist",
              "album-artist",
              "composer",
              "album",
              "title",
              "genre",
              "label",
              "description",
              "track",
              "disc",
              "year",
              "bpm",
              "set-artist=",
              "set-album-artist=",
              "set-composer=",
              "set-album=",
              "set-title=",
              "set-genre=",
              "set-label=",
              "set-description=",
              "set-track=",
              "set-disc=",
              "set-year=",
              "set-bpm="]


    @staticmethod
    def dflt_getters():
        getters = []
        getters.append(Getter.artist())
        getters.append(Getter.albumartist())
        getters.append(Getter.composer())
        getters.append(Getter.album())
        getters.append(Getter.title())
        getters.append(Getter.genre())
        getters.append(Getter.label())
        getters.append(Getter.description())
        getters.append(Getter.track())
        getters.append(Getter.disc())
        getters.append(Getter.year())
        getters.append(Getter.bpm())
        return getters


    @staticmethod
    def parse_args(argv):
        getters = []
        setters = []
        files = None

        try:
            opts, files = getopt.getopt(argv, TagEdit.shortopts, TagEdit.longopts)
        except getopt.GetoptError as err:
            print(err, file=sys.stderr)
            sys.exit(2)

        for opt in opts:
            if opt[0] in ['-h', '--help']:
                print(TagEdit.usage)
                sys.exit(0)

            elif opt[0] in ['-v', '--version']:
                print(TagEdit.version)
                sys.exit(0)

            elif opt[0] in ['-a', '--artist']:
                getters.append(Getter.artist())

            elif opt[0] in ['-r', '--album-artist']:
                getters.append(Getter.albumartist())

            elif opt[0] in ['-c', '--composer']:
                getters.append(Getter.composer())

            elif opt[0] in ['-l', '--album']:
                getters.append(Getter.album())

            elif opt[0] in ['-t', '--title']:
                getters.append(Getter.title())

            elif opt[0] in ['-g', '--genre']:
                getters.append(Getter.genre())

            elif opt[0] in ['-p', '--label']:
                getters.append(Getter.label())

            elif opt[0] in ['-s', '--description']:
                getters.append(Getter.description())

            elif opt[0] in ['-n', '--track']:
                getters.append(Getter.track())

            elif opt[0] in ['-k', '--disc']:
                getters.append(Getter.disc())

            elif opt[0] in ['-y', '--year']:
                getters.append(Getter.year())

            elif opt[0] in ['-b', '--bpm']:
                getters.append(Getter.bpm())

            elif opt[0] in ['-A', '--set-artist']:
                setters.append(Setter.artist(opt[1]))

            elif opt[0] in ['-R', '--set-album-artist']:
                setters.append(Setter.albumartist(opt[1]))

            elif opt[0] in ['-C', '--set-composer']:
                setters.append(Setter.composer(opt[1]))

            elif opt[0] in ['-L', '--set-album']:
                setters.append(Setter.album(opt[1]))

            elif opt[0] in ['-T', '--set-title']:
                setters.append(Setter.title(opt[1]))

            elif opt[0] in ['-G', '--set-genre']:
                setters.append(Setter.genre(opt[1]))

            elif opt[0] in ['-P', '--set-label']:
                setters.append(Setter.label(opt[1]))

            elif opt[0] in ['-S', '--set-description']:
                setters.append(Setter.description(opt[1]))

            elif opt[0] in ['-N', '--set-track']:
                try:
                    setters.append(Setter.track(IntTuple(opt[1])))
                except ValueError:
                    print("Invalid track '" + opt[1] + "'", file=sys.stderr)
                    sys.exit(2)

            elif opt[0] in ['-K', '--set-disc']:
                try:
                    setters.append(Setter.disc(IntTuple(opt[1])))
                except ValueError:
                    print("Invalid disc '" + opt[1] + "'", file=sys.stderr)
                    sys.exit(2)

            elif opt[0] in ['-Y', '--set-year']:
                try:
                    setters.append(Setter.year(int(opt[1])))
                except ValueError:
                    print("Invalid year '" + opt[1] + "'", file=sys.stderr)
                    sys.exit(2)

            elif opt[0] in ['-B', '--set-bpm']:
                try:
                    setters.append(Setter.bpm(int(opt[1])))
                except ValueError:
                    print("Invalid bpm '" + opt[1] + "'", file=sys.stderr)
                    sys.exit(2)

        if not files:
            print("No files specified.", file=sys.stderr)
            sys.exit(2)

        if not getters and not setters:
            getters = TagEdit.dflt_getters()

        return (getters, setters, files)


    @staticmethod
    def run2(argv) -> int:
        try:
            TagEdit.run(argv)
        except SystemExit as err:
            return err.code


    @staticmethod
    def run(argv):
        (getters, setters, files) = TagEdit.parse_args(argv)

        for path in files:
            tagfile = File(path)

            if tagfile:
                if setters:
                    for callback in setters:
                        callback(tagfile)

                    tagfile.save()

                for callback in getters:
                    (key, value) = callback(tagfile)
                    print(key + "=" + value)

            else:
                print("Unable to open " + path, file=sys.stderr)

        sys.exit(0)


def main():
    result = TagEdit.run(sys.argv[1:])


if __name__ == "__main__":
    main()
