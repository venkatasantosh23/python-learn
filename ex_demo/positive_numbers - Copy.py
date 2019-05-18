#accept numbers form user until zero is entered and display allpositive numbers in sorted order
l=[]
po=[]
nv=[]
n=1
while n!=0:
    n=int(input("Enter number:"))
    if n==0:
        break
    l.append(n)
for i in l:
    if i>0:
        po.append(i)
    else:
        nv.append(i)
print(po)
po.sort()
print(po)