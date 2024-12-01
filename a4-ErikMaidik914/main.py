from backtracking import *


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