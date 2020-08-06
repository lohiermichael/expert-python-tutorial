class File(object):
    def __init__(self, file_name, method):
        self.file = open(file_name, method)

    def __enter__(self):
        print('Enter context manager')

        return self.file

    def __exit__(self, type, value, traceback):
        print(type, value, traceback)
        print('Exit context manager')
        # Handle the error
        if type == AttributeError:
            print('We are handling the AssertionError')
            return True
        self.file.close()


if __name__ == "__main__":
    with File(file_name='text.txt', method='w') as f:
        print('Inside context manager')
        f.write('This is a test')

    print('\n')
    with File(file_name='text.txt', method='r') as f:
        print(f.read())

    print('\n')
    with File(file_name='text.txt', method='w') as f:
        print(f.undefined_function('Hey!'))
