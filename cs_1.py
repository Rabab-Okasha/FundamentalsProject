#name:Rabab Mohamed Abd El-Gafour Okasha 
#name:Basmalah Nabil El-Said Muhammed 
 
import re
# menu 1
def display_menu_1():
    print("Menu 1:")
    print("A. Insert a new number")
    print("B. Exist")
    
# menu 2
def display_menu_2():
    print("Please select the operation:")
    print("A. Compute one's complement")
    print("B. Compute two's complement")
    print("C. addition")
    print("D. subtraction\n")
    
def get_user_choice():
     choice_1 = input("Please Enter Your Choice\n ")
     return choice_1
    
# check a number is binary 
def validate_binary_number(number):
    pattern = r'^[01]+$'  # Regular expression pattern for binary numbers
    if re.match(pattern, number):
        return True
    else:
        return False

def insert_number():
     num_2 = input("Please enter second  number \n")
     while not validate_binary_number(num_2):
        print("Please insert a valid binary number\n")
        num_2 = input("Please enter second number again\n")
     return num_2

def bin_add(num_1,num_2):
        num_1=str(num_1)
        num_2=str(num_2)
        result = ""
        carry = 0
        i, j = len(num_1) - 1, len(num_2) - 1
        while i >= 0 or j >= 0 or carry != 0:
            sum = carry
            if i >= 0:
                sum += int(num_1[i])
                i -= 1
            if j >= 0:
                sum += int(num_2[j])
                j -= 1
            carry = sum // 2
            result = str(sum % 2) + result
        return result 
def one_complement(number):
    result = ""
    for i in number:
        if i == '0':
            result += "1"
        else: 
            result += "0"
    return result
    
def two_complement(num_1):
    result = one_complement(num_1)
    result_twos_complement=bin_add(result,1)
    return  result_twos_complement
    


def subtraction(num_1,num_2): # subtraction methode
    result = int(num_2 ,2) - int(num_1 ,2)
    sub = bin(result)
    return sub[2:]
    
def bin_subtract(num_1,num_2): # to make subtraction operation always positive
    if num_2 > num_1:
        sub=subtraction(num_1,num_2)
    else:
        sub=subtraction( num_2,num_1)
    return sub

def perform_action_menu_2(choice,num_1):
    if choice == 'A':
         result_one_complement=one_complement(num_1)
         print(f'Result of ones complement = {result_one_complement}\n')
    elif choice == 'B':
          result_two_complement=two_complement(num_1)
          print(f'Result of twos complement = {result_two_complement}\n')
    elif choice == 'C':
         num_2=insert_number()
         sum=bin_add(num_1,num_2)
         print(f'Sum = {sum}\n')
    elif choice == 'D':
         num_2=insert_number()
         sub=bin_subtract(num_1,num_2)
         print(f'Subtraction = {sub}\n')
         
    main()
        
def perform_action_menu_1(choice):
    if choice == 'A':
        num_1 = input("Please Enter First Number:\n")
        while not validate_binary_number(num_1):
            print("Please insert a valid binary number.\n")
            num_1 = input("Please Enter First Number Again\n")
        display_menu_2()
        choice=get_user_choice()
        perform_action_menu_2(choice,num_1)
    elif choice == 'B':
         quit()
    else:
        print("Please select a valid choice(A\B) \n")
        choice=get_user_choice()


def main():
    display_menu_1()
    choice=get_user_choice()
    perform_action_menu_1(choice)
    
main()       
