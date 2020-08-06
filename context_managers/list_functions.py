class ContextManager():

    def __init__(self):
        self.functions = []

    def func(self, f):
        self.functions.append(f)
        return f

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        for f in self.functions:
            print(f.__name__)


if __name__ == "__main__":

    with ContextManager() as cm:

        @cm.func
        def add(x, y):
            return x + y

        def foo():
            return "foo"

        @cm.func
        def subtract(x, y):
            return x - y
