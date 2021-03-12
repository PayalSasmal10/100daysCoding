# When we want grouping uses
# syntax: filter(function,sequence), this always checks true & false
# finding enven number
ls = [42, 25, 9, 8, 7, 3]
# Normal function


def even(x):
    if x % 2 == 0:
        return True
    else:
        return False


l = list(filter(even, ls))
print(l)
print("using lambda function started")
s = list(filter(lambda x: x % 2 == 0, ls))
print(s)
