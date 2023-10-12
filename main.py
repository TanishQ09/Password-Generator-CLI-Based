import datetime
import functions2
import  random
import pyperclip
name = input("Enter Your name : ")
current_year = datetime.date.today()
while True:
    date = int(input("Enter Your birth date : "))
    if (date >= 1 and date <= 31):
        break
    else:
        print("Sorry Invalid Date please enter between (1 to 31)")
        continue
while True:
    month = int(input("Enter Your birth month : "))
    if (month >= 1 and month <= 12):
        break
    else:
        print("Sorry Invalid Month please enter between (1 to 12)")
        continue
while True:
    year = int(input("Enter Your birth year : "))
    if (year >= 1950 and year <= current_year.year):
        break
    else:
        print("Sorry Invalid Year please enter between (1 to", current_year.year,")")
        continue
age = current_year.year-year-((current_year.month, current_year.day)<(month, date))
while True:
    contact_no = input("Enter Your Contact No. : ")
    if (len(contact_no) <  10) :
        print("Sorry number is less than of 10 digits")
        print("Try Again")
        continue
    elif (len(contact_no) > 10):
        print("Sorry number is greater than of 10 digits")
        print("Try Again")
        continue
    elif (len(contact_no) == 10) :
        break
    else:
        print("Invalid No.")
        print("Try Again")
        continue
print("Do You want to add someone in your password (y/n) : ")
name_choice = input()
if (name_choice == 'n' or name_choice == 'N'):
    list1 = []
    while(True):
        rand_choice = random.randint(0,13)
        if rand_choice not in list1:
            print("Password is : ")
            if(rand_choice == 0):
                passcode = functions2.name_begin_num(name,date)
                print(passcode)
            elif(rand_choice == 1):
                passcode = functions2.name_mid_num(name, date)
                print(passcode)
            elif(rand_choice == 2):
                passcode = functions2.name_end_num(name, date)
                print(passcode)
            elif(rand_choice == 3):
                passcode = functions2.name_begin_num(name, month)
                print(passcode)
            elif(rand_choice == 4):
                passcode = functions2.name_mid_num(name, month)
                print(passcode)
            elif(rand_choice == 5):
                passcode = functions2.name_end_num(name,month)
                print(passcode)
            elif(rand_choice == 6):
                passcode = functions2.name_begin_num(name, year)
                print(passcode)
            elif(rand_choice == 7):
                passcode = functions2.name_mid_num(name, year)
                print(passcode)
            elif(rand_choice == 8):
                passcode = functions2.name_end_num(name,year)
                print(passcode)
            elif(rand_choice == 9):
                passcode = functions2.name_begin_num(name, age)
                print(passcode)
            elif(rand_choice == 10):
                passcode = functions2.name_mid_num(name, age)
                print(passcode)
            elif(rand_choice == 11):
                passcode = functions2.name_end_num(name,age)
                print(passcode)
            list1.append(rand_choice)
            pass_choice = input("Do you like the password ? (y or n)\n")
            if(pass_choice == 'y' or pass_choice == 'Y'):
                copy_choice = input("Do you want to copy the password in your clipboard ? (y or no)\n")
                if(copy_choice == 'y' or copy_choice == 'Y'):
                    pyperclip.copy(passcode)
                    print("Thanks for using password genertor !!\n")
                    break
                if(copy_choice == 'n' or copy_choice == 'N'):
                    print("Thanks for using password genertor !!\n")
                    break
                
            if(len(list1) == 11):
                print("Sorry we have these combinations only try after sometime!!\n")
                break
        if rand_choice in list1:
            continue

if (name_choice == 'y' or name_choice == 'Y'):
    person = input("Who is that person ? ")
    print("Enter name of your", person," : ")
    person_name = input()
    while True:
        print("Enter Your ",person," birth date : ")
        person_date = int(input())
        if (person_date >= 1 and person_date <= 31):
            break
        else:
            print("Sorry Invalid Date please enter between (1 to 31)")
            continue
    while True:
        print("Enter Your ",person," birth month : ")
        person_month = int(input())
        if (person_month >= 1 and person_month <= 12):
            break
        else:
            print("Sorry Invalid Month please enter between (1 to 12)")
            continue
    while True:
        print("Enter Your ",person," birth year : ")
        person_year = int(input())
        if (person_year >= 1950 and person_year <= current_year.year):
            break
        else:
            print("Sorry Invalid Year please enter between (1 to", current_year.year, ")")
            continue
    age = current_year.year-person_year-((current_year.month, current_year.day)<(person_month, person_date))
    print("Do your ", person, " have separate contact no ? (y/n)")
    person_choice = input()
    if (person_choice == 'y' or person_choice == 'Y'):
        while True:
            print("Enter Your",person," Contact No. : ")
            contact_no = input()
            if (len(contact_no) < 10):
                print("Sorry number is less than of 10 digits")
                print("Try Again")
                continue
            elif (len(contact_no) > 10):
                print("Sorry number is greater than of 10 digits")
                print("Try Again")
                continue
            elif (len(contact_no) == 10):
                break
            else:
                print("Invalid No.")
                print("Try Again")
                continue