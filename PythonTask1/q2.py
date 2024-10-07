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

    print(ls)
    
    sorts(ls)
    print(ls)

