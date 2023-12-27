 #name:Rabab Mohamed Abd El-Gafour Okasha ID:20237004
#name:Basmalah Nabil El-Said Muhammed ID:20235005
 
 import re
 
def display_menu_1():
    print("Menu 1:")
    print("A. Insert a new number")
    print("B. Exist")
    
def get_user_choice_1():
     input(choice_1)
     return choice_1
    
# understand it well
def validate_binary_number(num_1):
    num_1 = input()
    pattern = r'^[01]+$'  # Regular expression pattern for binary numbers
    if re.match(pattern, num_1):
        return True
    else:
        return False

def display_menu_2():
    print("Please select the operation")
    print("A. Compute one's complement")
    print("B. Compute two's complement")
    print("C. addition")
    print("D. subtraction")
    
def get_user_choice_2():
     input(choice_2)
     return choice_2
    
#def one_complement():
    
#def two_complement():
    
def addition():
    #understand it well
    if validate_binary_number():
       print("Valid binary number.")
    else:
       print("Please insert a valid binary number.")
    num_2 = input("Enter the second number")
    sum = num_1 + num_2
    return sum

def subtraction():
    #understand it well
    if validate_binary_number(num_1):
       print("Valid binary number.")
    else:
       print("Please insert a valid binary number.")
    num_2 = input ("Enter the second number")
    sub = num_2 - num_1
    return sub

def perform_action(choice_2):
    if choice_2 == 'A':
        result_1 = one_complement()
        display_menu_1
    elif choice == 'B':
        result_2 = two_complement()
        display_menu_1
    elif choice == 'C':
         sum = addition()
        display_menu_1()
    elif choice == 'D':
         sub = subtraction()
        display_menu_1()
        
def perform_action(choice_1):
    if choice_1 == 'A':
        num_1 = input("Please Enter a number:")
        validate_binary_number()
        #understand it well
        if validate_binary_number(num_1):
            print("Valid binary number.")
        else:
            print("Please insert a valid binary number.")
        display_menu_2()
        perform_action(choice_2)
    elif choice_1 == 'B':
         break
    else:
        print("Please select a valid choice")

display_menu_1()
get_user_choice_1()
    
        
    
    
    