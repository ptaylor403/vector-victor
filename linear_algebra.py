
def shape(vector):
    return (len(vector), )

def vector_add(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ShapeError
    return [x + y for x, y in zip(vector1, vector2)]

def vector_sub(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ShapeError
    return [x - y for x, y in zip(vector1, vector2)]

def vector_sum(*args):
    if len(a) != len(a):
        raise ShapeError
    return [sum(a) for a in zip(*args)]

def vector_multiply(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ShapeError
    return [x * y for x, y in zip(vector1, vector2)]


class ShapeError(Exception):
    pass
