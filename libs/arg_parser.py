from argparse import ArgumentParser


def parse_args():
    """
    Parse CLI arguments
    :return: parser object with arguments
    """
    parser = ArgumentParser(description="Config file")
    parser.add_argument(
        "-c",
        "--config",
        dest="config_path",
        required=True,
        help="path to config file",
        metavar="FILE",
    )
    return parser.parse_args()
