
n=int(input("enter rows of first matrix"))

m=int(input("enter columns of first matrix"))

a=int(input("enter rows of second matrix"))

b=int(input("enter columns of second matrix"))
one = [[0] * m for _ in range(n)]  
two = [[0] * b for _ in range(a)]

print("one:\n")
for i in range(n):
    for j in range(m):
        one[i][j] = int(input(f"Enter element [{i}][{j}]: "))
print("two:\n")
for i in range(a):
    for j in range(b):
        two[i][j] = int(input(f"Enter element [{i}][{j}]: "))


def multi(arr1,arr2):
    if m !=a:
        print("error")
        exit(0)
    else:
        c=[[0]*b for _ in range(n)]
        for i in range(n):
            for j in range(b):
                for k in range(m):
                    c[i][j]+= arr1[i][k]*arr2[k][j]
    return c
print(multi(one,two))



    
    