# addition of vectors
def add(a: list, b: list):
    result = []
    for i in range(len(a)):
        result.append(a[i] + b[i])
    return result

a = [6, 5, 4]
b = [3, 2, 1]
new = add(a, b)
print(new)

# subtraction of vectors
def sub(a: list, b: list):
    result = []
    for i in range(len(a)):
        result.append(a[i] - b[i])
    return result

a = [6, 5, 4]
b = [3, 2, 1]
new = sub(a, b)
print(new)
print(sub([1, 2, 3], [4, 5, 6]))
print(sub([4, 5, 6], [1, 2, 3]))

# vector magnitude
import math
def mag(a: list):
    result = 0
    for i in range(len(a)):
        square = a[i]**2
        result += square
    return math.sqrt(result)

print(mag([3, 4]))
print(mag([1, 2, 3]))

# dot product 
def dot(a: list, b: list):
    result = 0
    for i in range(len(a)):
        result += a[i] * b[i]
    return result

print(dot([1, 0], [0, 1]))
print(dot([2, 3], [4, 1]))
print(dot([1, 1], [-1, -1]))

"""
cosine similarity = dot product / mag(a) * mag(b)

"""
def cosine_similarity(a: list, b: list):
    return dot(a, b) / (mag(a) * mag(b))

print(cosine_similarity([1, 1], [-1, -1]))
print(cosine_similarity([3, 4], [6, 8]))
print(cosine_similarity([2, 3], [4, 1]))