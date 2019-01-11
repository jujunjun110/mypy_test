from scripts.modules.myparser import MyParser


def main() -> None:
    p = MyParser()
    num = p.extract_number("1a2b")

    if num is None:
        return

    print(num * 2)


if __name__ == "__main__":
    main()
