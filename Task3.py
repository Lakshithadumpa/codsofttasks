# PASSWORD GENERATOR
import random
import string
def password(n):
    if n!=0:
        data=string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
        random_data=random.choices(data, k=n)
        print("your desired password is :")
        print("".join(random_data))
    else:
        print("Enter the length greater than zero.")
n=int(input("Enter the desired length of the password: "))
password(n)