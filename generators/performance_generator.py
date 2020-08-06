import sys

from decorators.timer import timer

"""
Space performance
"""


def gen_list(n):
    for i in range(n):
        yield n


def make_list(n):
    return [i ** 2 for i in range(n)]


def compare_space_performance(g, l):
    print(f'The list takes {sys.getsizeof(l)} bytes in memory')
    print(f'The generator takes {sys.getsizeof(g)} bytes in memory')


"""
Time performance
"""


@timer
def gen_list_time(n):
    for i in range(n):
        yield n


@timer
def make_list_time(n):
    return [i ** 2 for i in range(n)]


if __name__ == "__main__":
    n = 10**7
    # Space performance
    compare_space_performance(g=gen_list(n), l=make_list(n))

    # Time performance
    _ = gen_list_time(n)
    _ = make_list_time(n)
