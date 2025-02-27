#create a calculator with basic arthematic operations
def calculator():
    print("Simple calculator")
    while(True):
        

        try:
            print("Enter any two numbers")
            a=float(input())
            b=float(input())
            print("Enter the operation (+,-,*,/)")
            ch=input()
        


            if ch=='+':
                result=a+b
            elif ch=='-':
                result=a-b
            elif ch=='*':
                result=a*b
            elif ch=='/':
                if b==0:
                    print("Error: Division is not possible with zero.It gives infinite number.")
                    return 
                result=a/b
            else:
                print("Invalid operator : Give valid operator.")
            
            print(f"Result:{a} {ch} {b} = {result}")
            print(" ")
            print("Please Enter [End] if want to stop [continue]to move")
            ip=input()
            if (ip=="End" or ip =='end'):
                print("Thankyou!")
                break
            else:
                continue
            
        except ValueError:
            print("Invalid values:Please enter the valid input.")
calculator()




    