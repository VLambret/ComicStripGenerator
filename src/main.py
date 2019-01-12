#! /usr/bin/python3

import sys

import argparse
import Parser.StripParser
import StripGenerator

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', help="comic file to transform into Makefile",
                        default="strip.comic", type=str, required=False)
    args = parser.parse_args()
    return args.f

def print_usage(command):
    print("usage : " + command + " input.strip [output.strip]")

def main():
    argc = len(sys.argv)
    if (argc < 2 or 3 < argc):
        exit(1)

    if sys.argv[1] == "--help":
        print_usage(sys.argv[0])
        exit(0)

    inputFile = sys.argv[1]
    if argc == 3:
        outputFile = sys.argv[2]
    else:
        outputFile = inputFile.replace(".strip", ".png")

    inputStrip = open(inputFile,'r')

    exit(0)


    #comic_file_name = get_arguments()
    #final_png_name = comic_file_name.replace(".comic", ".png")
    #strip = Parser.StripParser.init_from_file(comic_file_name)
    #StripGenerator.create_image_from_strip(strip, final_png_name)

main()
