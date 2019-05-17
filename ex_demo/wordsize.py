#display each word along with size
s=input("Enter an string:")
str=s.split(' ')
for i in str:
    print(f"{i}-{len(i)}")