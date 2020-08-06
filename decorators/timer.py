import time
import random


def timer(func):
    """Time a function

    Args:
        func ([func]): The function to time
    """
    def wrapper(*args, **kwargs):
        start = time.time()
        _ = func(*args, **kwargs)
        end = time.time()

        print(f'{func.__name__} ran for {end - start} seconds')

        if 'print_list_len' in kwargs and kwargs['print_list_len']:
            L = list(args)[0]
            print(f'for list of length: {len(L)}')

        if 'print_args' in kwargs and kwargs['print_args']:
            print(f'For args: {args}')
        print('\n')

    return wrapper


@timer
def pause_function():
    # Sleep 2 seconds
    time.sleep(2)
    pass


@timer
def sort_long_list(L, print_args=False, print_list_len=True):
    return sorted(L)


if __name__ == "__main__":
    list_lens = [10**i for i in range(1, 6)]
    for list_len in list_lens:
        L = random.sample(range(1, 10*list_len), list_len)
        _ = sort_long_list(L, print_list_len=True)

    _ = pause_function()
