n =int(input("enter number of strings - "))
print(n)
ls =[]
dict ={}
i =0
while i <n:
    ls.append(str(input()))
    i = i+1
for x in ls:
    for y in x:
        if y in dict:
            dict[y] += 1
        else:
            dict[y]=1 

print(dict)

