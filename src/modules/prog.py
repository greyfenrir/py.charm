import selenium


def func():
    file = selenium.__file__
    if 'src' not in file:
        raise BaseException(file)


if __name__ == "main":
    func()
