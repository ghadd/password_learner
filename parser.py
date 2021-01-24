from argparse import ArgumentParser

parser = ArgumentParser(description="Learn passwords!")
parser.add_argument("--new", action="store_true", dest="create_new")
parser.add_argument("--allowed-chars", dest="allowed_chars", default=None)
parser.add_argument("-e", "--exclude-ambigous",
                    dest="exclude_ambigous_chars", action="store_true")
parser.add_argument("-l", "--length", dest="length", default=16)
