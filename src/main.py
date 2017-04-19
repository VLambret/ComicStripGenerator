#! /usr/bin/python3

import argparse
import sys
import Parser
import StripGenerator

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', help="comic file to transform into Makefile",
                        default="strip.comic", type=str, required=False)
    args = parser.parse_args()
    return args.f

def main():
    comic_file_name = get_arguments()
    final_png_name = comic_file_name.replace(".comic", ".png")
    strip = Parser.init_from_file(comic_file_name)
    StripGenerator.create_image_from_strip(strip, final_png_name)

main()
