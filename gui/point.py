class Point:
    _x = 0
    _y = 0

    @property
    def X(self):
        return self._x

    @X.setter
    def X(self, value):
        self._x = value

    @property
    def Y(self):
        return self._y

    @Y.setter
    def Y(self, value):
        self._y = value

    def __init__(self, x=0, y=0):
        self.X = x
        self.Y = y

    def __repr__(self):
        return str((self.X, self.Y))

    def set(self, x, y):
        self.__init__(x, y)

    def __eq__(self, other):
        return self.X == other.X and self.Y == other.Y

    def __ne__(self, other):
        return self.X != other.X and self.Y != other.Y

    def __add__(self, other):
        return Point(self.X + other.X, self.Y + other.Y)

    def __sub__(self, other):
        return Point(self.X - other.X, self.Y - other.Y)

    def __truediv__(self, other):
        return Point(self.X / other.X, self.Y / other.Y)

    def __floordiv__(self, other):
        return Point(self.X // other.X, self.Y // other.Y)

    def __mul__(self, other):
        return Point(self.X * other.X, self.Y * other.Y)

    def __iadd__(self, other):
        self.X += other.X
        self.Y += other.Y
        return self

    def __isub__(self, other):
        self.X -= other.X
        self.Y -= other.Y
        return self

    def __itruediv__(self, other):
        self.X /= other.X
        self.Y /= other.Y
        return self

    def __ifloordiv__(self, other):
        self.X //= other.X
        self.Y //= other.Y
        return self

    def __imul__(self, other):
        self.X *= other.X
        self.Y *= other.Y
        return self
