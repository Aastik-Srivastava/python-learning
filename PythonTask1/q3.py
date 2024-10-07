class sortwiz:
    
    def sorts(l):
        length = len(l)  
      
        for i in range(length-1):  
            minIndex = i  
            
            for j in range(i+1, length):  
                if l[j]<l[minIndex]:  
                    minIndex = j  
                    
            l[i], l[minIndex] = l[minIndex], l[i]  
            
        return l  
    n =int(input("enter number of strings - "))
    ls=[]
    i=0
    
    while i <n:
        ls.append(str(input()))
        i = i+1

    
    sorts(ls)
    print(ls)
    
    
    tstr = input("enter string to find: ")
    f = 0
    last = n - 1
    c = 0  

    while last >= f:
        mid = (f + last) // 2  
        if tstr == ls[mid]:
            print(f"found at {mid+1}")
            c = 1 
            break  
        elif tstr > ls[mid]:
            f = mid + 1  
        else:
            last = mid - 1  

    if c == 0:
        print("not found")

        

