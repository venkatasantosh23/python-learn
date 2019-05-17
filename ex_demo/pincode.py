#check given pincode is valid or not
s=input("enter any pincode:")
if len(s)==6 and s.isdigit():
    print('your  entered pincode is correct')
else:
    print('your enter worng pincode please check ')