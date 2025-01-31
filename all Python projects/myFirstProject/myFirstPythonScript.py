#make username generator based on name and date of birth and mobile number

import json
import random
import time

first_time_loading_files = True

# these must update with previous files when app starts including counter     # NO IDEA HOW TO DO THIS!!!  # well now i have some!
counter = 0
generated_username = []
generated_username_number = []
mobile_numbers = []
admin_privilege = []
generate_username_and_counter = {}
userdata_with_key_username = {}

store_data_files_path1 = "store_data_files/counter.json"
store_data_files_path2 = "store_data_files/generated_username.json"
store_data_files_path3 = "store_data_files/generated_username_number.json"
store_data_files_path4 = "store_data_files/mobile_numbers.json"
store_data_files_path5 = "store_data_files/admin_privilege.json"
store_data_files_path6 = "store_data_files/generate_username_and_counter.json"
store_data_files_path7 = "store_data_files/userdata_with_key_username.json"

#must not be modified
atoz = {0:"",1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",7:"g",8:"h",9:"i",10:"j",11:"k",12:"l",13:"m",14:"n",15:"o",16:"p",17:"q",18:"r",19:"s",20:"t",21:"u",22:"v",23:"w",24:"x",25:"y",26:"z"}

#username generator function in sign up screen function
def create_username(use_first_name,use_last_name,date_of_birth,mobile_number):
    username = ""
    global counter

    use_first_name = use_first_name.lower()
    use_last_name = use_last_name.lower()

    username = use_first_name[2] + use_first_name[0]  + date_of_birth[1] + atoz.get(random.randint(1,26)) + use_last_name[1] + atoz.get(random.randint(1,26)) + date_of_birth[-1] + use_first_name[-1] + use_last_name[-2] + mobile_number[2] + mobile_number[7] + atoz.get(random.randint(1,26))

    if username not in generated_username:
        # print("generated username not found in the list")
        mobile_numbers.append(mobile_number)
        generated_username.append(username)
        generated_username_number.append(counter)
        #adding the username with counter as the key
        generate_username_and_counter.update({str(counter) : username})

        #here should be modefyed according to need later on !!!
        #adding the user data with username as the key
        userdata_with_key_username.update({username : {"first_name": use_first_name,"last_name": use_last_name,"date_of_birth":date_of_birth,"mobile_number":mobile_number}})
        # userdata_with_key_username[counter] = { username : { "first_name": use_first_name, "last_name": use_last_name,"date_of_birth": date_of_birth, "mobile_number": mobile_number } }

        counter +=1
        with open(store_data_files_path1,"w") as counter_file:
            json.dump(counter,counter_file)
        with open(store_data_files_path2,"w") as generated_username_file:
            json.dump(generated_username,generated_username_file)
        with open(store_data_files_path3,"w") as generated_username_number_file:
            json.dump(generated_username_number,generated_username_number_file)
        with open(store_data_files_path4,"w") as mobile_numbers_file:
            json.dump(mobile_numbers,mobile_numbers_file)
        with open(store_data_files_path6,"w") as generate_username_and_counter_file:
            json.dump(generate_username_and_counter,generate_username_and_counter_file)
        with open(store_data_files_path7,"w") as userdata_with_key_username_file:
            json.dump(userdata_with_key_username,userdata_with_key_username_file)
    else :
        # print("generated username found in the list.generating new username")
        create_username(use_first_name,use_last_name,date_of_birth,mobile_number)

    return username       # I HAVE NO IDEA WHAT I AM MAKING AT THIS POINT

#login screen function
def login_screen():
    print()
    print("***** User Login *****")
    print("1. login with username")
    print("2. login with number")
    print("3. sign up")
    login_input = input("Enter your choice: ")
    while login_input != "1" and login_input != "2" and login_input != "3":
        login_input = input("Enter your choice: ")

    if login_input == "1":

        print("***** login with username *****")
        entered_username_count = 0
        entered_username = ""
        while not entered_username and entered_username_count < 3:
            entered_username = input("Enter your username: ")
            if entered_username in generated_username:
                entered_password = ""
                while not entered_password:
                    entered_password = input("Enter your Password: ")
                    if entered_password in mobile_numbers:
                        print("correct password")
                        home_page_screen(entered_username,entered_password)
                    else:
                        print("Incorrect Password!")
                        print("Try Again!")
                        entered_password = ""
            else:
                print("Incorrect username!")
                print("Try Again!") if entered_username_count < 2 else print()
                entered_username = ""

                entered_username_count +=1
        find_username = input("Enter Registered mobile no to find your username: ")
        if find_username:
            if find_username not in mobile_numbers:
                print("this mobile number is not registered")
                register = input("would you like to register (y/n)?: ")
                while register != "y" and register != "n":
                    register = input("would you like to register?: ")
                if register == "y":
                    sign_up()
                else:
                    login_screen()
            elif find_username in mobile_numbers:
                print(f"you username is: {generate_username_and_counter.get(str(mobile_numbers.index(find_username)))}")
                print("register mobile number is the password")
                login_screen()
        else:
            login_screen()
    elif login_input == "2":
        print("***** login with number *****")
        enter_number = ""
        while not enter_number or not enter_number.isdigit() or len(enter_number) != 10:
            enter_number = input("Enter your registered mobile number: ")
        if enter_number in mobile_numbers:
            if verify_user(enter_number):
                home_page_screen(generate_username_and_counter.get(str(mobile_numbers.index(enter_number))),enter_number)
            else:
                login_screen()
        #elif enter_number not in mobile_numbers:
        else:
            print("this mobile number is not registered")
            register_number = input("would you like to register (y/n)?: ")
            while register_number != "y" and register_number != "n":
                register_number = input("would you like to register (y/n)?: ")
            if register_number == "y":
                sign_up()
            else:
                login_screen()
    else:             # WHY AM I DOING THIS TO MY-SELF WHY!!!
        sign_up()

#verify the user mobile number
def verify_user(verify_number):       # WHAT EVEN IS THIS! WHAT THIS THING EVEN DOING! WHAT DID I MAKE HERE! I DONT WANNA READ ALL THIS
    generated_otp = random.randint(1000,9999)
    print(f"message received on mobile number {verify_number}")
    print(f"you have received otp: {generated_otp} for user verification of mobile number {verify_number}")
    enter_otp = input("Enter 4 digit otp send on registered number: ")
    while not enter_otp.isdigit() or len(enter_otp) !=4:
        enter_otp = input("Enter 4 digit otp send on registered number: ")
    enter_otp = int(enter_otp)
    if enter_otp != generated_otp:
        print("invalid OTP")
        print("verification failed!")
        resend_otp = input("resend Otp (y/n): ")
        while resend_otp != "y" and resend_otp != "n":
            resend_otp = input("resend Otp (y/n): ")
        if resend_otp == "y":
            verify_user(verify_number)
        else:
            return False
    else:
        print("number verification successful!")
        return True

#see all your details screen
def your_details(your_username,your_password):
    print()
    print("***** User Details *****")
    print(f"Username: {your_username}      Password: {your_password}")
    print(f"first name: {userdata_with_key_username.get(your_username).get("first_name")}")
    print(f"last name: {userdata_with_key_username.get(your_username).get("last_name")}")
    print(f"date of birth: {userdata_with_key_username.get(your_username).get("date_of_birth")}")
    print(f"mobile number: {userdata_with_key_username.get(your_username).get("mobile_number")}")
    print()
    go_back = input("press (Q) to go back: ")
    while go_back.lower() != "q":
        go_back = input("press (Q) to go back: ")
    home_page_screen(your_username,your_password)

def modify_user_details(user_username,user_number):
    print("***** Modify User Data *****")         # I HAVE NO IDEA WHAT IS GOING ON FROM HERE
    print("1. Change First Name")
    print("2. Change Last Name")
    print("3. Change Date of Birth")
    print("4. Go Back")
    modify_user_data = input("Enter your choice: ")
    while modify_user_data != "1" and modify_user_data != "2" and modify_user_data != "3" and modify_user_data != "4":
        modify_user_data = input("Enter your choice: ")
    modify_user_data = int(modify_user_data)
    if modify_user_data == 1:
        print("***** change first name *****")
        print(f"current first name: {userdata_with_key_username.get(user_username).get("first_name")}")
        new_first_name = input("Enter new first name: ")
        while not new_first_name:
            new_first_name = input("Enter new first name: ")
        userdata_with_key_username.update({user_username: {"first_name": new_first_name,"last_name": userdata_with_key_username.get(user_username).get("last_name"),"date_of_birth": userdata_with_key_username.get(user_username).get("date_of_birth"),"mobile_number": userdata_with_key_username.get(user_username).get("mobile_number")}})
        modify_user_details(user_username,user_number)

    elif modify_user_data == 2:
        print("***** change last name *****")
        print(f"current last name: {userdata_with_key_username.get(user_username).get("last_name")}")
        new_last_name = input("Enter new last name: ")
        while not new_last_name:
            new_last_name = input("Enter new last name: ")

        userdata_with_key_username.update({user_username: {"first_name": userdata_with_key_username.get(user_username).get("first_name"),"last_name": new_last_name,"date_of_birth": userdata_with_key_username.get(user_username).get("date_of_birth"),"mobile_number": userdata_with_key_username.get(user_username).get("mobile_number")}})
        modify_user_details(user_username, user_number)

    elif modify_user_data == 3:
        print("***** Change Your Date of Birth *****")
        print(f"current date of birth: {userdata_with_key_username.get(user_username).get("date_of_birth")}")
        new_date_of_birth = input("Enter new Date of Birth: ")
        while not new_date_of_birth:
            new_date_of_birth = input("Enter new Date of Birth: ")
        userdata_with_key_username.update({user_username: {"first_name": userdata_with_key_username.get(user_username).get("first_name"), "last_name": userdata_with_key_username.get(user_username).get("last_name"),"date_of_birth": new_date_of_birth,"mobile_number": userdata_with_key_username.get(user_username).get("mobile_number")}})
        modify_user_details(user_username, user_number)

    else:
        home_page_screen(user_username,user_number)

def add_new_user():
    sign_up()

def ask_for_admin_homepage_screen(ask_admin_homepage_username,ask_admin_homepage_password):
    if ask_admin_homepage_username not in admin_privilege:
        print("you can't access this you are not the admin")
        home_page_screen(ask_admin_homepage_username,ask_admin_homepage_password)
    else:
        admin_homepage_screen(ask_admin_homepage_username,ask_admin_homepage_password)

def ask_for_admin_privilege(ask_for_username,ask_for_password):
    print()
    print("***** Ask for Admin Privilege *****")
    if ask_for_username not in admin_privilege:
        print("1. send request")    #request accepted or rejected
        print("2. Go Back")
        ask_for_choice = input("Enter your choice: ")
        while ask_for_choice != "1" and  ask_for_choice != "2":
            ask_for_choice = input("Enter your choice: ")
        ask_for_choice = int(ask_for_choice)
        if ask_for_choice == 1:
            luck = random.randint(0,1)
            if luck == 0:
                print("request accepted!")
                admin_privilege.append(ask_for_username)
                print(f"username {ask_for_username} set to admin.")
                with open(store_data_files_path5, "w") as admin_privilege_file:
                    json.dump(admin_privilege, admin_privilege_file)
                home_page_screen(ask_for_username,ask_for_password)
            else:
                print("request rejected!")
                send_request = input("send request again (y/n)?: ")
                while send_request != "y" and send_request != "n":
                    send_request = input("send request again (y/n)?: ")
                if send_request == "y":
                    ask_for_admin_privilege(ask_for_username,ask_for_password)
                else:
                    home_page_screen(ask_for_username,ask_for_password)
        else:
            home_page_screen(ask_for_username,ask_for_password)
    else:
        print("you are already a admin")
        home_page_screen(ask_for_username,ask_for_password)

def logout_current_account():
    login_screen()

def print_counter(cou_username,cou_number):
    print()
    print(counter)
    print()
    admin_homepage_screen(cou_username,cou_number)

def print_generated_username(gen_user_username,gen_user_number):
    print()
    print(generated_username)
    print()
    admin_homepage_screen(gen_user_username,gen_user_number)

def print_generated_username_number(gen_user_num_username,gen_user_num_number):
    print()
    print(generated_username_number)
    print()
    admin_homepage_screen(gen_user_num_username,gen_user_num_number)

def print_mobile_numbers(mob_num_username,mob_num_number):
    print()
    print(mobile_numbers)
    print()
    admin_homepage_screen(mob_num_username,mob_num_number)

def print_admin_privilege(admin_pri_username,admin_pri_number):
    print()
    print(admin_privilege)
    print()
    admin_homepage_screen(admin_pri_username,admin_pri_number)

def print_generate_username_and_counter(gen_user_and_count_username,gen_user_and_count_number):

    print()
    for counter_key,username_value in generate_username_and_counter.items():
        print(f"{{'{counter_key}': '{username_value}'}}")
    print()

    admin_homepage_screen(gen_user_and_count_username,gen_user_and_count_number)

def print_userdata_with_key_username(user_key_username,user_key_number):

    print()
    for username_key,userdata_value in userdata_with_key_username.items():
        print(f"{{'{username_key}': {userdata_value}}}")
    print()
    admin_homepage_screen(user_key_username,user_key_number)

def admin_homepage_screen(admin_homepage_username,admin_homepage_number):
    print()
    print("***** Admin Homepage Screen *****")
    print(f"username: {admin_homepage_username}      number: {admin_homepage_number}")
    print("1. counter")
    print("2. generated_username")
    print("3. generated_username_number")
    print("4. mobile_numbers")
    print("5. admin_privilege")
    print("6. generate_username_and_counter")
    print("7. userdata_with_key_username")
    print("8. Go Back to user homepage screen")
    admin_homepage_input = input("Enter your choice: ")
    while admin_homepage_input != "1" and admin_homepage_input != "2" and admin_homepage_input != "3" and admin_homepage_input != "4" and admin_homepage_input != "5" and admin_homepage_input != "6" and admin_homepage_input != "7" and admin_homepage_input != "8":
        admin_homepage_input = input("Enter your choice: ")
    admin_homepage_input = int(admin_homepage_input)

    if admin_homepage_input == 1:
        print_counter(admin_homepage_username,admin_homepage_number)

    elif admin_homepage_input == 2:
        print_generated_username(admin_homepage_username,admin_homepage_number)

    elif admin_homepage_input == 3:
        print_generated_username_number(admin_homepage_username,admin_homepage_number)

    elif admin_homepage_input == 4:
        print_mobile_numbers(admin_homepage_username,admin_homepage_number)

    elif admin_homepage_input == 5:
        print_admin_privilege(admin_homepage_username,admin_homepage_number)

    elif admin_homepage_input == 6:
        print_generate_username_and_counter(admin_homepage_username,admin_homepage_number)

    elif admin_homepage_input == 7:
        print_userdata_with_key_username(admin_homepage_username,admin_homepage_number)

    elif admin_homepage_input == 8:
        home_page_screen(admin_homepage_username,admin_homepage_number)
                  # WHY IS HERE SO MANY ELIF HERE WHAT WAS I THINKING WHEN I WAS WRITING THIS
    else:
        print("Something went Wrong!")


#home screen function
def home_page_screen(home_page_username,home_page_number):
    print()
    print("***** User Homepage Screen *****")
    print(f"username: {home_page_username}      number: {home_page_number}")
    if home_page_username in admin_privilege:
        print("you are now the admin")
    print("1. see all your details")
    print("2. modify your details")
    print("3. add new user")
    print("4. go to admin homepage screen")
    print("5. ask for admin privilege")
    print("6. logout current account")
    print("7. exit.")
    home_page_input = input("Enter your choice: ")
    while home_page_input != "1" and home_page_input != "2" and home_page_input != "3" and home_page_input != "4" and home_page_input != "5" and home_page_input != "6" and home_page_input != "7":
        home_page_input = input("Enter your choice: ")
    home_page_input = int(home_page_input)

    if home_page_input == 1:
        your_details(home_page_username, home_page_number)

    elif home_page_input == 2:
        modify_user_details(home_page_username, home_page_number)

    elif home_page_input == 3:
        add_new_user()

    elif home_page_input == 4:
        ask_for_admin_homepage_screen(home_page_username,home_page_number)

    elif home_page_input == 5:
        ask_for_admin_privilege(home_page_username, home_page_number)

    elif home_page_input == 6:
        logout_current_account()

    elif home_page_input == 7:
        exit(0)

    else:
        print("Something went Wrong!")

#sign up screen function
def sign_up():
    global first_time_loading_files
    first_name = ""
    last_name = ""
    dob = ""
    number = ""
    noUser = False

    print()
    print("***** New User Sign Up *****")
    print("Generate your unique username.")
    while not first_name:
        first_name = input("Enter your first name: ")
    while not last_name:
        last_name = input("Enter your last name: ")
    while not dob:
        dob = input("Enter you date of birth (dd-mm-yyyy): ")
    while not number:
        number = input("Enter your mobile number: ")
        number = number.replace(" ", "")
        number = number.replace("-", "")
        if number in mobile_numbers:
            print("this number is already registered please use another number or login")
            print("1. login")
            print("2. continue signing up")
            numberFound = input("Enter your choice: ")
            while numberFound != "1" and numberFound != "2":
                numberFound = input("Enter your choice: ")
            if numberFound == "1":
                login_screen()
                first_name = ""
                last_name = ""
                dob = ""
                number = ""
                noUser = True
                break
            else:
                number = ""

        #removing das and spaces from the strings
    first_name = first_name.replace(" ","")
    last_name = last_name.replace(" ","")
    original_dob = dob          #dob is cleaned no das or space original_dob is keeping the original user typed dob
    # dob = dob.replace(" ","")
    # dob = dob.replace("-","")

    make_username = ""

    if not noUser:
        make_username = create_username(first_name,last_name,dob,number)

    print("Your Entered Details are Shown.")
    print(f"your name is: {first_name.capitalize()} {last_name.capitalize()}")
    print(f"your date of birth is: {original_dob}")
    print(f"your mobile number is: {number}")
    print("Generating your Username...")
    time.sleep(1)
    print("Your Username is Generated Successfully.")
    # print("Your Account has been Created Successfully.")
    print("You are Successfully Signed Up.")
    print(f"Your Generated Username is: {make_username}")
    print(f"Your mobile number is the password: {number}")
    print("You will be automatically redirected to the Homepage.")

    first_time_loading_files = False
    first_time_file_path = "store_data_files/first_time.json"

    with open(first_time_file_path,"w") as first_time_file:
        json.dump(first_time_loading_files,first_time_file)

    home_page_screen(make_username,number)

    print()
    print("***** generated username list *****")
    print(mobile_numbers)
    print(generated_username)
    print(generated_username_number)
    print(generate_username_and_counter)
    for i in range(len(generated_username_number)):
        print(i)
        print(userdata_with_key_username.get(generate_username_and_counter.get(i)))
    # for j in range(len(generated_username_number)):
    #     print(j)
    #     print(f"{userdata_with_key_username.get(j).get(generate_username_and_counter.get(j)).get("first_name")} {userdata_with_key_username.get(j).get(generate_username_and_counter.get(j)).get("last_name")}")
    #     print(f"{userdata_with_key_username.get(j).get(generate_username_and_counter.get(j)).get("date_of_birth")}")
    #     print(f"{userdata_with_key_username.get(j).get(generate_username_and_counter.get(j)).get("mobile_number")}")

def load_all_userdata():

    global counter
    global generated_username
    global generated_username_number
    global mobile_numbers
    global admin_privilege
    global generate_username_and_counter
    global userdata_with_key_username
    global first_time_loading_files

    with open(store_data_files_path1,"r") as counter_read_file:
        counter = json.load(counter_read_file)
        # print(counter)

    with open(store_data_files_path2,"r") as generated_username_read_file:
        generated_username = json.load(generated_username_read_file)
        # print(generated_username)

    with open(store_data_files_path3,"r") as generated_username_number_read_file:
        generated_username_number = json.load(generated_username_number_read_file)
        # print(generated_username_number)

    with open(store_data_files_path4,"r") as mobile_numbers_read_file:
        mobile_numbers = json.load(mobile_numbers_read_file)
        # print(mobile_numbers)

    with open(store_data_files_path5,"r") as admin_privilege_read_file:
        admin_privilege = json.load(admin_privilege_read_file)
        # print(admin_privilege)

    with open(store_data_files_path6,"r") as generate_username_and_counter_read_file:
        generate_username_and_counter = json.load(generate_username_and_counter_read_file)
        # print(generate_username_and_counter)

    with open(store_data_files_path7,"r") as userdata_with_key_username_read_file:
        userdata_with_key_username = json.load(userdata_with_key_username_read_file)
        # print(userdata_with_key_username)

#first screen login or sign up function
first_time_file_path = "store_data_files/first_time.json"
try:
    with open(first_time_file_path,"r") as first_time_file:
        first_time_loading_files = json.load(first_time_file)
        print(first_time_loading_files)
except FileNotFoundError:
    ...

if not first_time_loading_files:
    print("loading all the files...")
    load_all_userdata()
    print("All the files loaded successfully.")
print("***** You need to login first before entering *****")
print("if you dont have an account then sign up first")
print("1. Sign Up")
print("2. Login")
sign_or_login = input("Enter you choice: ")

while sign_or_login != "1" and sign_or_login != "2":
    sign_or_login = input("Enter you choice: ")
if sign_or_login == "1":
    #print("You will automatically redirected to the Sign Up page.")
    time.sleep(1)
    sign_up()
elif sign_or_login == "2":
    login_screen()

else:
    print("something went wrong!")





