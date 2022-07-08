class Size:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return str((self.width, self.height))

    def set(self, width, height):
        self.__init__(width, height)

    def __eq__(self, other):
        return self.width == other.width and self.height == other.height

    def __ne__(self, other):
        return self.width != other.width and self.height != other.height

    def __add__(self, other):
        return Size(self.X + other.X, self.Y + other.Y)

    def __sub__(self, other):
        return Size(self.X - other.X, self.Y - other.Y)

    def __truediv__(self, other):
        return Size(self.X / other.X, self.Y / other.Y)

    def __floordiv__(self, other):
        return Size(self.X // other.X, self.Y // other.Y)

    def __mul__(self, other):
        return Size(self.X * other.X, self.Y * other.Y)

    def __iadd__(self, other):
        self.width += other.width
        self.height += other.height
        return self

    def __isub__(self, other):
        self.width -= other.width
        self.height -= other.height
        return self

    def __itruediv__(self, other):
        self.width /= other.width
        self.height /= other.height
        return self

    def __ifloordiv__(self, other):
        self.width //= other.width
        self.height //= other.height
        return self

    def __imul__(self, other):
        self.width *= other.width
        self.height *= other.height
        return self
