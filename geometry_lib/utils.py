def calculate_area(shape):
    if not hasattr(shape, 'area') or not callable(getattr(shape, 'area')):
        raise TypeError("Object must have an 'area' method")
    return shape.area()
