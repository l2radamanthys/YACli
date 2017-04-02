import sys
import os
import lib.handler


def main():
    if len(sys.argv) > 1:
        argv = sys.argv[1:]
        lib.handler.call_handler(argv)
    else:
        print('Error faltan parametros', sys.argv)


if __name__ == '__main__':
    main()