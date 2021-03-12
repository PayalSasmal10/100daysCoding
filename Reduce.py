# reduce to single value
from functools import reduce
l = [1, 9, 6, 20, 45]
s = ''


def sum1(s, x):
    return s+x


ls = reduce(sum1, l)
print(ls)

print("using lambda")
result = reduce(lambda x, y: x+y, l)
print(result)
