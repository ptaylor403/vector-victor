
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
    length = [len(i) for i in args]
    if max(length) != min(length):
        raise ShapeError
    return [sum(a) for a in zip(*args)]

def dot(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ShapeError
    return sum(x * y for x, y in zip(vector1, vector2))

def vector_multiply(vector1, number):
    return [x * number for x in vector1[:]]

def vector_mean(*args):
    return [float(sum(vector))/len(vector) for vector in zip(*args)]

def magnitude(vector):
    return sum(a**2 for a in vector)**0.5

class ShapeError(Exception):
    pass
