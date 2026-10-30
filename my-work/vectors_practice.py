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