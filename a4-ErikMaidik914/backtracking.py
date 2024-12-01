# A4
# 10
from Dynamic import *
from itertools import permutations

def backtracking_recursive(n, r):
    if len(r) == n:
        print(r)
    for i in range(1, n + 1):
        r.append(i)
        if partial(r) == 1:
            backtracking_recursive(n, r)
        r.pop()


def partial(l):
    m = len(l)
    for i in range(m):
        for j in range(i + 1, m):
            if l[i] == l[j]:
                return 0
    for i in range(m - 1):
        if abs(l[i] - l[i + 1]) == 1:
            return 0
    return 1


def set(List):
    return ''.join(List)


def permutetions(lst, answer):
    for i in range(len(lst)):
        c = lst[i]
        left = lst[0:i]
        right = lst[i + 1:]
        r = left + right
        permutetions(r, answer + c)


def backtracking_iterative(n):
    l=[]
    l = list(permutations(range(1, n+1)))
    for i in l:
        if len(i)==n and partial(i)==1:
            print (i)


if __name__ == "__main__":
    n = int(input("YOUR CHOSEN NUMBER IS:"))
    lst=[]
    answer = ""
    for i in range(1,n+1):
        lst.append(i)
    if n <= 3:
        print(f"There are no combinations available")
    else:
        print(f"{backtracking_recursive(n,[])}")











"""if __name__ == '__main__':
    A = []
    nr = int(input("Type the length of the array:"))
    for i in range(0, nr):
        element = int(input())
        A.append(element)
    print(f"{dynamic(A, nr)}")"""