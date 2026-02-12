import argparse
import sys
import tomllib

def main():
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("-p", "--printer", help="Path to line printer", default="/dev/usb/lp0")
    argument_parser.add_argument("-c", "--config", help="Path to config file", default="receipt.conf")
    args = argument_parser.parse_args()
    try:
        config_file = open(args.config, "rb")
        config = tomllib.load(config_file)
    except FileNotFoundError:
        print("Configuration file not found", file=sys.stderr)
        sys.exit(1)

    feeds = []
    for feed in config['feeds'].items():
        feeds.append(feed)



if __name__ == "__main__":
    main()
