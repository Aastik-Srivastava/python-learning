1
n =int(input("enter n"))
i=0
ls=[]
while i<n:
    ls.append(int(input("enter number")))
    i+=1
print(ls)


hashT= [[] * n for _ in range(10)] 
k=0
for x in ls:
    k=0
    while k<10:
        if(x%10==k):
            hashT[k].append(x)
        k+=1
print(hashT)

