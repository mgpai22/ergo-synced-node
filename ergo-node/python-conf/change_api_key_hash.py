import argparse
from Operations import write_api_key_hash


if __name__ == "__main__":
    my_parser = argparse.ArgumentParser(description='Write API Hash')

    my_parser.add_argument('api_hash', metavar='api_hash', type=str, help='api_hash')

    args = my_parser.parse_args()

    write_api_key_hash(args.api_hash, 'ergo.conf')
