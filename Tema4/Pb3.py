class Matrix:

    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.data = []

    def get(self, i, j):
        return self.data[i][j]
    
    def set(self, i, j, val):
        self.data[i][j] = val
    
    def transpose(self):
        transposed = [[self.data[j][i] for j in range(self.n)] for i in range(self.m)]
        return Matrix(self.m, self.n, transposed)
    
    def multiplication(self, m):
        if self.m != m.n:
            return None
        n = []
        for i in range(self.n):
            n.append([])
            for j in range(m.m):
                n[i].append(0)
                for k in range(self.m):
                    n[i][j] += self.n[i][k] * m.n[k][j]
        return Matrix(n, m.m)
    
    def apply(self, func):
        for i in range(self.n):
            for j in range(self.m):
                self.data[i][j] = func(self.data[i][j])

    def __iter__(self):
        for row in self.data:
            for elem in row:
                yield elem

    def __repr__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])
