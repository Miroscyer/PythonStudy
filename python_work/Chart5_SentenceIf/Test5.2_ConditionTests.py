str1='welCome'
str2='Welcome'

print(str1==str2)
print(str1.lower()==str2.lower())

print("\n")
num1=46
num2=-12
print(num1==num2)
print(num1!=num2)
print(num1>num2)
print(num1<num2)
print(num1>=num2)
print(num1<=num2)

if(num1>0 and num2>0):
    print("Both >0")

elif(num1>0 or num2>0):
    print("at least one >0")

nums=[1,46,53,15]
if(num1 in nums):
    print("in")
else:
    print("not in")
    
if(num2 not in nums):
    print("not in")
else:
    print("in")
