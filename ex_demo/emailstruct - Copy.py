#display the user name and sever name of a given email
s=input("Enter an email:")
str=s.partition('@')
print(f'user name:{str[0]} \nserver name:{str[2]}')