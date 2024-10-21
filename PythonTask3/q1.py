import math

def dist(a,b,c,d):
    dis = math.sqrt((c-a)**2 +(d-b)**2)
    return dis

ref = input("enter coordinate with comma in between: ").split(sep=",")
coords= [(0,1) , (0,3) , (1,2),(1,0)] 


n = len(coords)
for i in range(n):
    for j in range(0, n-i-1):
        distance1 = dist(int(ref[0]), int(ref[1]), coords[j][0], coords[j][1])
        distance2 = dist(int(ref[0]), int(ref[1]), coords[j+1][0], coords[j+1][1])
        if distance1 > distance2:
            coords[j], coords[j+1] = coords[j+1], coords[j]

print(f"output: {coords}")

