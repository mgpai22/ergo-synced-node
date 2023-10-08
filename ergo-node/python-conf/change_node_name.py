import argparse
from Operations import write_node_name


if __name__ == "__main__":
    my_parser = argparse.ArgumentParser(description='Write Node Name')

    my_parser.add_argument('node_name', metavar='node_name', type=str, help='node_name')

    args = my_parser.parse_args()

    write_node_name(args.node_name, 'ergo.conf')
