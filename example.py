from geometry_lib.shapes import Circle, Triangle
from geometry_lib.utils import calculate_area

c = Circle(5)
t = Triangle(3, 4, 5)

print("Circle area:", calculate_area(c))
print("Triangle area:", calculate_area(t))
print("Is triangle right?", t.is_right())