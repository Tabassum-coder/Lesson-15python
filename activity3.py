def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def prod(n1,n2):
    return n1*n2
def quo(n1,n2):
    return n1//n2


print("a - add")
print("b - substraction")
print("c - multiplication")
print("d - division")

choice=input("Enter any choice from a/b/c/d")
num1=int(input("Enter first number"))
num2=int(input("Enter second number"))

if choice=='a':
    print("The sum of {0} and {1} is {2}".format(num1,num2,add(num1,num2)))
elif choice=='b':
    print("The diff of {0} and {1} is {2}".format(num1,num2,sub(num1,num2)))
elif choice=='c':
    print("The product of {0} and {1} is {2}".format(num1,num2,prod(num1,num2)))
elif choice=='d':
    print("The quotient of {0} and {1} is {2}".format(num1,num2,quo(num1,num2)))
else:
    print("Please enter correct choice")