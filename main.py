from logger import init
from logging import DEBUG

from udpipe import process


INPUT = "Karla žere seno."


def main():
    token_lists = process(INPUT)
    for token_list in token_lists:
        for token in token_list:
            print(repr(token))


if __name__ == "__main__":
    init(__name__, DEBUG)
    main()
