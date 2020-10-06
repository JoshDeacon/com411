print("Please enter the first number: ")
num1=int(input())
print("Please enter the second number: ")
num2=int(input())
print("Please enter the third number: ")
num3=int(input())
even_num=0
odd_num=0
if num1%2==0:
    even_num+=1
else:
    odd_num+=1
if num2%2==0:
    even_num+=1
else:
    odd_num+=1
if num3%2==0:
    even_num+=1
else:
    odd_num+=1
print("There were {} even and {} odd numbers".format(even_num, odd_num))
