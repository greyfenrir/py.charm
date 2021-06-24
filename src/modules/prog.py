import selenium


def func():
    file = selenium.__file__
    if 'src' in file:
        print("It's my file!: {file}")
    else:
        raise BaseException(f"Wrong file: {file}")


if __name__ == "__main__":
    func()
