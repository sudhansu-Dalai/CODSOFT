def add(x,y):
    return x + y
def substract(x,y):
    return x-y

def multiply(x,y):
    return  x*y

def divide(x,y):
    if y==0:
        return  "Error ! Division by Zero"
    else:
        return x / y


print("----SELECT AN OPERATION ----")
print("1. ADD (+)")
print("2. Substract (-)")
print("3. Multiply (X)")
print("4. Divide (/)")

print("------------------------------")

while True :
    choice = input("Enter Your Choice : ")
    if choice in  ('1' ,'2','3','4'):
        num1 = float(input("Enter The First Number : "))
        num2 = float(input("Enter The Second Number : "))

        if choice == '1':
            print("Result : ",add(num1,num2))
        elif choice == '2':
            print("Result : ",substract(num1,num2))
        elif choice == '3':
            print("Result : ",multiply(num1,num2))
        elif choice=='4':
            print("Result : ",divide(num1,num2))


        else:
            print("Invalid Input ")

        next_calulation = input("Do You Want To Perform Another Calculation (yes Or No) ?  ")

        if next_calulation.lower() != "yes":
            break



