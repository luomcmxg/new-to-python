# a = int(input("Please enter the base: "))
# b = int(input("Please enter the square: "))
# c = list(range(1, b + 1))
# print(list(map(lambda x: a**x, c[1:b + 1:2])))
A = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]


def a(lst): return map(list, zip(*lst))


print(list(a(A)))
print(list(zip(*list(map(tuple, A)))))
b = a(A)
print(list(map(list, *zip(*zip(list(map(tuple, A)))))))

C = list(map(list, *zip(*zip(list(map(tuple, A))))))

print(list(map(list, (i for i, j in zip(A, C) if i == j))))
print(list(map(list,zip(*A))))