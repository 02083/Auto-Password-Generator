
import random
import string
import re

def generate_password(length=12, use_upper=True, use_digits=True, use_special=True):
    lower=string.ascii_lowercase
    upper=string.ascii_uppercase if use_upper else ""
    digits=string.digits if use_digits else ""
    special = r"!@#$%^&*()-_=+[]{}|;:',<.>/?~`" if use_special else ""
    all_chars = lower+upper+digits+special

    if not all_chars:
        raise ValueError("No character sets selected for password generation..")
    return "".join(random.choice(all_chars)for _ in range(length))

def check_strength(password):
    length_score=len(password) >= 12
    upper_score=bool(re.search(r"[A-Z]",password))
    lower_score=bool(re.search(r"[a-z]",password))
    digit_score=bool(re.search(r"[0-9]",password))
    special_score = bool(re.search(r"[!@#$%^&*()\-_=+\[\]{}|;:',<.>/?~`]", password))
    score=sum([length_score, upper_score, lower_score,  digit_score, special_score])
    if score==5:
        return " strong passwaord"
    elif score>=3:
        return " Moderate password"
    else:
        return " weak password"

def main():
    while True:
        print("\n====== password tool ======")
        print("1. Generate password ")
        print("2. Check the password strength")
        print("3. Exit")

        choice =input("Enter choice: ")
        
        if choice=="1":
            length=int(input("length of password: "))
            use_upper= input("Include uppercase letters?(y/n): ").lower()=="y"
            use_digits= input("Include digits?(y/n): ").lower()=="y"
            use_special= input("Include special characters?(y/n): ").lower()=="y"
            pwd= generate_password(length,use_upper,use_digits,use_special)
            print("\n Generated password: ",pwd)
        elif choice=="2":
            pwd=input("Enter password to test: ")
            print("strength:",check_strength(pwd))
        elif choice=="3":
            print("Bye!")
            break
        else:
            print("Invalid choice. Try again.\n")
        

if __name__ =="__main__":

    main()
