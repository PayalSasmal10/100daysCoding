# NormalWay list
ls = []
for i in range(100):
    if i % 3 == 0:
        ls.append(i)
print(ls)

# list comprehension
lst = [i for i in range(100) if i % 3 == 0]
print(lst)

# https://www.hackerrank.com/challenges/list-comprehensions/problem
x = int(input())
y = int(input())
z = int(input())
n = int(input())
print([[a, b, c] for a in range(x+1) for b in range(y+1)
       for c in range(z+1) if a+b+c != n])

# set comprehension
test = {test for test in ['A', 'B', 'B', 'A']}
print(test)

# generator comprehension. This is denoted with ()
even_number = (even for even in range(100) if even % 2 == 0)
for i in even_number:
    print(i)

# How to get value: key pair in dictionary using dictionary comprehension
dict1 = {k: f"{k-1}" for k in range(10)}
print(dict1)
dict1 = {f"{k-1}": k for k in range(10)}
print(dict1)

# dictionary comprehension
input1 = int(input())
name_with_no = [input().split() for _ in range(input1)]
name_with_phonenoDict = {k: v for k, v in name_with_no}
while True:
    try:
        name = input()
        if name in name_with_phonenoDict:
            print(f"{name}={name_with_phonenoDict[name]}")
        else:
            print("Not found")
    except:
        break
