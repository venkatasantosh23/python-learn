#accept 10 numbers from user and display all odd numbers and even next
num=[]
newls=[]
n=9
n1=0
for i in range(10):
    num.append(int(input("Enter number:")))
for i in range(10):
    if num[i]%2!=0:
        newls.insert(n1,num[i])
        n1+=1
    else:
        newls.append(num[i])
        n-=1
print(newls)


