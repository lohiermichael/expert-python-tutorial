"""
Matrix mathematical object
Object: use the magic functions in python

"""

from random import randint


class Matrix:
    def __init__(self, n, m=None):
        self.n = n
        # Square matrix case
        self.m = m if m is not None else n

        self.size = (n, m)

        self.coordinates = {(i, j) for i in range(1, self.n+1)
                            for j in range(1, self.m+1)}
        self.values = {coord: 0 for coord in self.coordinates}
        self._max_index_len = max(len(str(self.n)), len(str(self.m)))

    def __repr__(self):

        self._max_val_len = max([len(str(value))
                                 for _, value in self.values.items()])
        self._max_len_char = max(self._max_index_len, self._max_val_len)

        # Build row indices
        row_indices = (self._max_index_len + 2) * ' '
        for j in range(1, self.m+1):
            row_indices += ' ' + \
                str(j) + (self._max_len_char - len(str(j)) + 2) * ' '

        # Build the content of the matrix
        content = ''

        for i in range(1, self.n+1):
            content += '\n'
            new_row = f'{i} ' + (self._max_index_len - len(str(i))) * ' ' + '|'
            for j in range(1, self.m+1):
                val_str = str(self.values[(i, j)])
                n_add_spaces = self._max_len_char - len(val_str)
                new_row += ' ' + val_str + n_add_spaces * ' ' + ' |'
            l_row = len(new_row)
            content += new_row

        # Build the separation rows
        sep_row = self._make_horizontal_separation(l_row)

        # String everything together
        output = row_indices + sep_row + content + sep_row

        return output

    def _make_horizontal_separation(self, l_row):
        return '\n' + (self._max_index_len+1) * ' ' + (l_row -
                                                       (self._max_index_len+1)) * '-'

    def __getitem__(self, coord):
        return self.values[coord]

    def __setitem__(self, coord, new_value):
        self.values[coord] = new_value

    def __add__(self, mat):
        assert len(mat) == len(self), "The sizes don't match"
        sum_mat = Matrix(n=self.n, m=self.m)
        for i in range(1, self.n+1):
            for j in range(1, self.m+1):
                sum_mat[i, j] = self[i, j] + mat[i, j]
        return sum_mat

    def __sub__(self, mat):
        assert len(mat) == len(self), "The sizes don't match"
        sum_mat = Matrix(n=self.n, m=self.m)
        for i in range(1, self.n+1):
            for j in range(1, self.m+1):
                sub_mat[i, j] = self[i, j] - mat[i, j]
        return sub_mat

    def __mul__(self, mat):
        assert self.m == mat.n, "The sizes don't match"
        mul_mat = Matrix(n=self.n, m=mat.m)
        for i in range(1, self.n+1):
            for j in range(1, mat.m+1):
                mul_mat[i, j] = sum(self[i, k] * mat[k, j]
                                    for k in range(1, self.m+1))
        return mul_mat

    def __pow__(self, power):
        if power == 1:
            return self
        else:
            return self * self.__pow__(power-1)

    def __rmul__(self, number):
        if type(number) not in [float, int]:
            raise TypeError()
        assert self.n == self.m, 'The matrix must be squared'
        mul_mat = Matrix(size=self.size)
        for i in range(1, self.size+1):
            mul_mat[i, i] = number * self[i, i]
        return mul_mat


def make_id(size):
    Id = Matrix(size)
    for i in range(1, size+1):
        Id[i, i] = 1
    return Id


def all_same(size, number):
    mat_same = Matrix(size)
    for i in range(1, size+1):
        for j in range(1, size+2):
            mat_same[i, j] = number
    return mat_same


def make_random(n, m=None, rand_low=1, rand_high=100):
    rand_mat = Matrix(n=n, m=m)
    for i in range(1, n+1):
        for j in range(1, m+1):
            rand_mat[i, j] = randint(rand_low, rand_high)
    return rand_mat


if __name__ == "__main__":
    m = make_random(3, 7)
    n = make_random(7, 10)
    p = make_random(10, 3)
    print(m)
    print(n)
    print(m*n*p)
