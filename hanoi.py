def hanoi(n, A, B, C):
    if n > 0:
        hanoi(n-1, A, C, B)
        print("{} --> {}".format(A,C))
        hanoi(n-1, B, A, C)
m = int(input())
hanoi(m, 'A', 'B', 'C')
#小袁添加注释