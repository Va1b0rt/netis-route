import argparse
import sys

from NetisRcommandinject import Two


parser = argparse.ArgumentParser(description='##############')
parser.add_argument('host', type=str,
                    help='host ip address <192.168.0.1>')
parser.add_argument('port', type=str,
                    help='port number <8000>')


if __name__ == '__main__':
    args = parser.parse_args()

    host = args.host
    port = args.port

    while True:
        cmd = input('?> ')
        if cmd in ('q', 'quit', 'exit'):
            sys.exit(0)

        Two(host, port, cmd)
