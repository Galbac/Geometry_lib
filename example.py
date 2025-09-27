from geometry_lib import Triangle, Circle, calculate_area

c = Circle(5)
t = Triangle(3, 4, 5)

print("Circle area:", calculate_area(c))
print("Triangle area:", calculate_area(t))
print("Is triangle right?", t.is_right())