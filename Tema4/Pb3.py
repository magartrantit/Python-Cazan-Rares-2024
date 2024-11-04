class Matrix:

    def __init__(self, n, m, data=None):
        self.n = n
        self.m = m
        if data:
            self.data = data
        else:
            self.data = [[0] * m for _ in range(n)]  # Initialize with zeros

    def get(self, i, j):
        return self.data[i][j]
    
    def set(self, i, j, val):
        self.data[i][j] = val
    
    def transpose(self):
        transposed = [[self.data[j][i] for j in range(self.n)] for i in range(self.m)]
        return Matrix(self.m, self.n, transposed)
    
    def multiply(self, other):
        if self.m != other.n:
            raise ValueError("Matrices cannot be multiplied")

        result = Matrix(self.n, other.m)
        for i in range(self.n):
            for j in range(other.m):
                result.data[i][j] = sum(self.get(i, k) * other.get(k, j) for k in range(self.m))
        return result
    
    def apply_transformation(self, func):
        for i in range(self.n):
            for j in range(self.m):
                self.data[i][j] = func(self.data[i][j])

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])
