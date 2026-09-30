import sys

from parse_map import parse_map


def main():
    if len(sys.argv) != 2:
        print("Usage: fly-in.py map")
        return

    try:
        config = parse_map(sys.argv[1])
    except (FileNotFoundError, ValueError) as error:
        print(f"Error: {error}")
        return

    print(config)


if __name__ == "__main__":
    main()
