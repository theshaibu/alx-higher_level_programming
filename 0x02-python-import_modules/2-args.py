#!/usr/bin/python3
import sys

def main():
    arg_length = len(sys.argv)

    if arg_length == 1:
        print("No arguments.")
    elif arg_length == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(arg_length - 1))

    for i, arg in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(i, arg))

if __name__ == "__main__":
    main()

