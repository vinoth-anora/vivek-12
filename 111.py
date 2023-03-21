rows=6
for i in range(rows):
    for j in range(rows-i):
        print("*",end="")
    print("\r")
l=[1,2,3,4,5,6,7]
for i in range(len(l)+1):
    if i%2:
        print(i)
for i in range(2,len(l),2):
    print(i)

for item in range(6,1,-1):
    print("*"*item)
l=[1,2,3,4,5,9,6,100,.7,55]
l9=[]
max=l[0]
for i in l:
    if i>max:
        max=i

