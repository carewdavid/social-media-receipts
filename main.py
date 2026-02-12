import argparse
import tomllib

def main():
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("-p", "--printer", help="Path to line printer", default="/dev/usb/lp0")
    argument_parser.add_argument("-c", "--config", help="Path to config file", default="receipt.conf")
    args = argument_parser.parse_args()
    with open(args.config, "rb") as config_file:
        config = tomllib.load(config_file)
        printer = Printer(args.printer, config['printer'])
        feeds = []
        for feed in config['feeds'].items():
            feeds.append(feed)



if __name__ == "__main__":
    main()
