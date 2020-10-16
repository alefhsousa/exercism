class Matrix:
    def __init__(self, matrix_string):
        self.raw = matrix_string.split('\n')
        self._rows = list()
        self._columns = list()
        self._to_matrix()

    def row(self, index):
        return self._rows[index - 1]

    def column(self, index):
        return list(self._columns[index - 1])

    def _to_matrix(self):
        self._rows = [[int(number) for number in row.split()] for row in self.raw]
        self._columns = list(zip(*self._rows))
