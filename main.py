from libs.context.nasa_context import NasaContext
import argparse


def main() -> None: 
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--command',
                        help='search on nasa images add -i to down')
    parser.add_argument('search', 
                        help='search on nasa images add -i to download images')
    args = parser.parse_args()

    object_ = NasaContext(args.search, True if args.command == 'down' else False)
    object_.extracting_specific_term()


if __name__ == '__main__':
    main()
