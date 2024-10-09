n = int(input("Enter n: "))
i = 0
ls = []
while i < n:
    ls.append(int(input("Enter number: ")))
    i += 1

hashT = [[] for _ in range(10)]

def bibsort(subss, num):
    f = 0
    l = len(subss) - 1 
    if l == -1: 
        subss.append(num)
        return
    
    while f <= l:
        mid = (f + l) // 2
        if num < subss[mid]:  
            l = mid - 1
        else:  
            f = mid + 1
            

    subss.insert(f, num)  
        
        
        
for num in ls:
    index = num % 10
    bibsort(hashT[index], num)

print(hashT)

