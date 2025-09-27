from abc import ABC, abstractmethod
from math import pi, sqrt, isclose

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self._set_radius(radius)

    def area(self):
        return round(pi * self._radius ** 2, 2)

    def _set_radius(self, radius):
        if isinstance(radius, str):
            try:
                radius = float(radius)
            except ValueError:
                raise ValueError(f"Cannot convert '{radius}' to a number")

        if not isinstance(radius, (int, float)):
            raise TypeError('Radius must be a number')
        if radius <= 0:
            raise ValueError('Radius must be positive')
        self._radius = radius

    @property
    def radius(self):
        return self._radius


class Triangle(Shape):
    def __init__(self, a, b, c):
        self._set_sides(a, b, c)

    def _convert_to_float(self, value):
        if isinstance(value, str):
            try:
                value = float(value)
            except ValueError:
                raise ValueError(f"Cannot convert '{value}' to a number")
        if not isinstance(value, (int, float)):
            raise TypeError(f"Side must be a number, got {type(value).__name__}")
        return value

    def _set_sides(self, a, b, c):
        a = self._convert_to_float(a)
        b = self._convert_to_float(b)
        c = self._convert_to_float(c)

        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("All sides must be positive")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("The sum of any two sides must be greater than the third side")

        self._a, self._b, self._c = a, b, c

    @property
    def sides(self):
        return self._a, self._b, self._c

    def area(self):
        p = (self._a + self._b + self._c) / 2
        return round(sqrt(p * (p - self._a) * (p - self._b) * (p - self._c)),2)

    def is_right(self):
        a, b, c = sorted([self._a, self._b, self._c])
        return isclose(a ** 2 + b ** 2, c ** 2, rel_tol=1e-9)
