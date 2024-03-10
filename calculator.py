def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    if y==0:
        return "Error! Division by zero."
    else:
        return x/y


print("Select your operation...\n1.Add \n2.Subtract \n3.Multiply \n4.Divide")
choice=input("Enter choice(1/2/3/4):")
num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
if choice=='1':
    print("Addition of 2 numbers: ",add(num1,num2))
elif choice=='2':
    print("Subtraction of 2 numbers: ",sub(num1,num2))
elif choice=='3':
    print("Multiplication of  of 2 numbers: ",mul(num1,num2))
elif choice=='4':
    print("Division of 2 numbers: ",div(num1,num2))
else:
    print("Invalid input")
