n = int(input("Enter n: "))
i = 0
ls = []
while i < n:
    ls.append(int(input("Enter number: ")))
    i += 1

hashT = [[] for _ in range(10)]

def insort(sublist, num):
    for i in range(len(sublist)):
        if num < sublist[i]:
            sublist.insert(i, num)
            return
    sublist.append(num)

for num in ls:
    index = num % 10
    insort(hashT[index], num)

print(hashT)

