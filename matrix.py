"""
Matrix mathematical object
Object: use the magic functions in python

"""


class Matrix:
    def __init__(self, size):
        self.size = size
        self.coordinates = {(i, j) for i in range(1, self.size+1)
                            for j in range(1, self.size+1)}
        self.values = {coord: 0 for coord in self.coordinates}
        self._max_index_len = len(str(self.size))

    def __repr__(self):

        self._max_val_len = max([len(str(value))
                                 for _, value in self.values.items()])
        self._max_len_char = max(self._max_index_len, self._max_val_len)

        row_indices = (self._max_index_len + 2) * ' '
        for i in range(1, self.size+1):
            row_indices += ' ' + \
                str(i) + (2 * self._max_len_char - len(str(i)) - 1) * ' ' + ' '

        content = ''

        for i in range(1, self.size+1):
            content += '\n'
            new_row = f'{i} ' + (self._max_index_len - len(str(i))) * ' ' + '|'
            for j in range(1, self.size+1):
                val_str = str(self.values[(i, j)])
                n_add_spaces = self._max_len_char - len(val_str)
                new_row += ' ' + val_str + n_add_spaces * ' ' + ' |'
            l_row = len(new_row)
            content += new_row

        sep_row = self._make_horizontal_separation(l_row)
        output = row_indices + sep_row + content + sep_row

        return output

    def _make_horizontal_separation(self, l_row):
        return '\n' + (self._max_index_len+1) * ' ' + (l_row -
                                                       (self._max_index_len+1)) * '-'

    def __len__(self):
        return (self.size, self.size)

    def __getitem__(self, coord):
        return self.values[coord]

    def __setitem__(self, coord, new_value):
        self.values[coord] = new_value

    def __add__(self, mat):
        assert len(mat) == len(self), "The sizes don't match"
        sum_mat = Matrix(size=self.size)
        for i in range(1, self.size+1):
            for j in range(1, self.size+1):
                sum_mat[i, j] = self[i, j] + mat[i, j]
        return sum_mat

    def __sub__(self, mat):
        assert len(mat) == len(self), "The sizes don't match"
        sub_mat = Matrix(size=self.size)
        for i in range(1, self.size+1):
            for j in range(1, self.size+1):
                sub_mat[i, j] = self[i, j] - mat[i, j]
        return sub_mat

    def __mul__(self, mat):
        assert len(mat) == len(self), "The sizes don't match"
        mul_mat = Matrix(size=self.size)
        for i in range(1, self.size+1):
            for j in range(1, self.size+1):
                mul_mat[i, j] = sum(self[i, k] * mat[k, j]
                                    for k in range(1, self.size+1))
        return mul_mat

    def __pow__(self, power):
        if power == 1:
            return self
        else:
            return self * self.__pow__(power-1)

    def __rmul__(self, number):
        assert type(number) in [float, int]
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


if __name__ == "__main__":
    Id = make_id(size=1)
    print(5 * Id)
