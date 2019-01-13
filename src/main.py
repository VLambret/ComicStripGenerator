#! /usr/bin/python3

import sys
import Parser.StripParser
import StripGenerator

def print_usage(command):
    print("usage : " + command + " input.strip [output.strip]")


def main():
    argc = len(sys.argv)
    if (argc < 2 or 3 < argc):
        exit(1)

    if sys.argv[1] == "--help":
        print_usage(sys.argv[0])
        exit(0)

    comic_file_name = sys.argv[1]
    if argc == 3:
        output_image_file = sys.argv[2]
    else:
        output_image_file = comic_file_name + ".png"

    strip = Parser.StripParser.init_from_file(comic_file_name)
    StripGenerator.create_image_from_strip(strip, output_image_file)
    exit(0)

main()
