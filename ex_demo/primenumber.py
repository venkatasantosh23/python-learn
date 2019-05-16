# given number is prime or not
a=int(input("Enter any number:"))
i=2
while i<a:
    if a%i == 0:
        print('given number is not a prime number')
        break
    i+=1
else:
    print( 'given number is prime')