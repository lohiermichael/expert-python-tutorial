from contextlib import contextmanager


@contextmanager
def open_file(file_name, method):
    f = open(file_name, method)
    try:
        yield f
    finally:
        # If uncommented the error is handled
        # return True
        f.close()


if __name__ == "__main__":
    with open_file('text.txt', 'w') as f:
        # f.undefined_function()
        f.write('Message in file')
