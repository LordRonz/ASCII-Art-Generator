import argparse


def get_args():
    parser = argparse.ArgumentParser(description="ASCII Art Generator")
    parser.add_argument("source_file", type=open, help="image file source")
    parser.add_argument(
        "-o", "--output", metavar="out.png", type=str, help="output filename"
    )
    parser.add_argument("-c", "--color", action="store_true", help="enable coloring")

    return parser.parse_args().__dict__
