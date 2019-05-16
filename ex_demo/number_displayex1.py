# print no.of  -ve ,+ve and zero
f1=f2=f3=0
print( 'enter 10 numbers:')
for i in range(10):
    a=int(input())
    if a>0:
        f1=f1+1
    elif a<0:
        f2=f2+1
    else:
        f3=f3+1
print("you are entered",f1,"positive numbers")
print("you are entered",f2,"negative numbers")
print("you are entered",f3,"zeros")
