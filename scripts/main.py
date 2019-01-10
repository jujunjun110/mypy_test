from typing import Optional


def main():
    message = get_message()
    print(message)


def get_message() -> str:
    return 'message'


if __name__ == '__main__':
    main()
