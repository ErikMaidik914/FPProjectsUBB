#a4 -6
import copy


def naive(A, nr):
    if nr<4:
        return False
    max_sum = -99999
    for q in range(0, nr-3):
        for p in range(q+1, nr-2):
            for n in range(p+1, nr-1):
                for m in range(n+1, nr):
                    s = A[m] - A[n] + A[p] - A[q]
                    if s > max_sum:
                        max_sum = s
                        a = A[m]
                        b = A[n]
                        c = A[p]
                        d = A[q]

    print(f"the maximum value is:{max_sum} and the expression used to calculate it is:{a} - {b} + {c} - {d}")


def dynamic(A, nr):
    if nr<4:
        return False
    max_sum=-9999999
    dp=[[0 for _ in range(nr+1)] for __ in range(nr+1)]        #dp- substractions>0 dp1-all relevant substracions+the previous pozitive substraction in dp
    dp1=[[0 for _ in range(nr+1)] for __ in range(nr+1)]       #we create a matrix of n+1 i and n+1 j.
    for i in range(1,nr+1):
        for j in range(1,nr+1):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            if j>i:
                dp[i][j]=max(A[j-1] - A[i-1],dp[i][j])         #dp becomes the list with the best case scenario for substractions
                dp1[i][j]=A[j-1] - A[i-1] + dp[i-1][i-1]       #does A[m]-A[n]+A[p]-A[q] (current generated substraction + highest result subsraction
                if dp1[i][j]>=max_sum and i>=3:
                    max_sum=dp1[i][j]                          #selects the highest result
    return max_sum

















"""if __name__ == '__main__':
    A = []
    nr = int(input("Type the length of the array:"))
    for i in range(0, nr):
        element = int(input())
        A.append(element)
    print(f"{dynamic(A, nr)}")"""
