# any logic can be put in map
# syntax: map(function,sequence)
# Let's double of a list
l = [6, 9, 5, 4, 7, 12]


def double(x):
    return 2*x


l1 = list(map(double, l))
print(l1)

# using lambda
l2 = list(map(lambda x: x*2, l))
print(l2)

# Map can take 2 sequence as well but sequence length should be equal, if we put extra length those will be ignored
ls = [12, 90, 7, 5, 1, 0]


def doublseq(l, ls):
    return l*ls


l3 = list(map(doublseq, l, ls))
print(l3)
print("lambda is going to be used")
l4 = list(map(lambda x, y: x*y, ls, l))
print(l4)
