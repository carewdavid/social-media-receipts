import argparse

def main():
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("-p", "--printer", help="Path to line printer", default="/dev/usb/lp0")
    argument_parser.add_argument("-c", "--config", help="Path to config file", default="receipt.conf")
    args = argument_parser.parse_args()
    print(args)


if __name__ == "__main__":
    main()
