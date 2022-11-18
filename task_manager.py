# imported datetime to timestamp tasks as they are set using the today variable
from datetime import datetime
today = str(datetime.today())

# new_user_list will be needed when registering a user
new_user_list = []

# ====Login Section====
# while loop that iterates for each username and password
while True:
    input_user = input("Enter your username: ")
    input_password = input("Enter your password: ")

    # logged_in  and user booleans assigned to false initially
    logged_in = False
    user = False

    # reads, splits ", " and strips user.txt file and assigns user_name and password to index 0 and index 1 from the file
    with open("user.txt", "r") as f:

        # for loop that iterates for each user_name and password in the txt file
        for line in f.readlines():
            temp = line.strip().split(", ")
            user_name = f"{temp[0]}"
            password = f"{temp[1]}"

            # if statement changes the logged_in boolean to True if usernames and passwords match.
            if input_user == user_name and input_password == password:
                print("You have successfully logged in.")
                logged_in = True
                # for loop will be broken
                break

            # elif statement changes the user boolean to True if the user inputs the correct username but incorrect
            # password
            elif input_user == user_name and input_password != password:
                user = True
                # for loop will be broken
                break

    # if the user is able to log in then the while loop will break.
    if logged_in:
        break

    # elif prints "You have entered the incorrect password" and then will go back to the beginning of the while loop
    elif user:
        print("You entered the incorrect password.")

    # else prints "You have entered the incorrect username and password" and will go back to the beginning of while loop
    else:
        print("You entered the incorrect username and password.")

 # while loop that iterates the menu until the user logs out by typing in 'e'
#
while True:
    admin = False
    if input_user == "admin" and input_password == "adm1n":
        admin = True
    if admin:
        menu = input("Select one of the following Options below:\n"
                    "s - Statistics\n"
                    "r - Registering a user\n"
                    "a - Adding a task\n"
                    "va - View all tasks\n"
                    "vm - View my task\n"
                    "e - Exit\n".lower())

        if menu.lower() == "s":
            with open("user.txt", "r") as f:
                x = len(f.readlines())
                print(f"________________________________________\nThere are a total of {x} registered users.\n_________"
                f"_______________________________")

        with open("tasks.txt", "r") as f:
            y = len(f.readlines())
            print(f"________________________________________\nThere are a total of {y} registered tasks.\n_________"
                          f"_______________________________")

        # if user inputs 'r' to register a new user they will be asked to input the new user and password
        if menu.lower() == "r":
            new_user_name = input("Please enter the new username you would like to register:  ")
            new_user_password = input("Please create a password for the new user you would like to register: ")
            password_confirmation = input("Please re-enter your password to confirm: ")

            #   nested if statement activates if the new password and confirmed password match
            if password_confirmation == new_user_password:
                # an empty user list is created to assign new users to later
                new_user_list = []
                # new_user concatenates new_suer_name and _new_user_password
                new_user = f"{new_user_name}, {new_user_password}"
                # append command to add a new user to the new user list
                new_user_list.append(new_user)

             # with open txt file set to a+ to append to the document without deleting any data
            with open("user.txt", "a+") as f:
                # for loop iterates for each appended new user and writes this into the txt file
                for new_user in new_user_list:
                    f.write(f"{new_user_name}, {new_user_password}\n")

    elif input_user != "admin" and input_user != "adm1n":
        admin = False
        if admin == False:
            menu = input("Select one of the following Options below:\n"
             # r - Registering a user
            "a - Adding a task\n"
            "va - View all tasks\n"
            "vm - View my task\n"
            "e - Exit\n".lower())



    if menu == 'a':
    # variables needed to register a new task
        new_task_username = input("Enter the username of whom the task will be assigned to: ")
        new_task_title = input("Enter a title for the task: ")
        task_description = input("Please enter a description of the task: ")
        task_due_date = input("Please enter the due date of the task in year/month/day format. E.g. 2022-11-16: ")
        task_complete_no = "No"
        task_complete_yes = "Yes"

        # all of the above variables assigned to the new_task_information variable ready to be added to new task list
        new_task_information_list = []
        new_task_information = f"{new_task_username}, {new_task_title}, {task_description}, {today[0:10]}, " \
                                f"{task_due_date}, {task_complete_no}"

        # append command to add new_task_information to a list
        new_task_information_list.append(new_task_information)

        # with open txt set to a+ to add detail to the file without deleting anything
        with open("tasks.txt", "a+") as f:
            for new_task_information in new_task_information_list:
                f.write(f"{new_task_information}\n")

    elif menu == 'va':
        # with tasks open set to r to read
        with open('tasks.txt', 'r') as f:
            # indexing of the read txt file to create new variables
            for line in f.readlines():
                temp = line.strip().split(", ")
                name_assigned = temp[0]
                task_title = temp[1]
                task_description = temp[2]
                date_issued = temp[3]
                date_due = temp[4]
                task_complete_no = temp[5]

                # variables assigned in a user friendly way
                read_task_list = []
                read_task = "-------------------------------------------------------------------------\n" \
                                        f"Assigned to: \t \t {name_assigned}\n" \
                                        f"Task Name: \t \t     {task_title}\n" \
                                        f"Task Description: \t {task_description}\n" \
                                        f"Date Assigned: \t \t {date_issued}\n" \
                                        f"Due Date: \t \t     {date_due}\n" \
                                        f"Task Complete: \t \t {task_complete_no}\n" \
                                        f"------------------------------------------------------------------------\n"
                # read task variable added to the read_task_list
                read_task_list.append(read_task)
                # for loop prints the information in the read_task variable for each iteration, which shows all tasks
                for read_task in read_task_list:
                    print(f"{read_task}\n")

    elif menu == 'vm':
        # with open task set as r to read
         with open('tasks.txt', 'r') as f:
            # for loop reads, strips and splits every line and then uses indexing to create variables with specific info
            for line in f.readlines():
                temp = line.strip().split(", ")
                name_assigned = temp[0]
                task_title = temp[1]
                task_description = temp[2]
                date_issued = temp[3]
                date_due = temp[4]
                task_complete_no = temp[5]

                # all of the variables above and assigned to the read_task variable in ux friendly format
                read_task_list = []
                read_task = "-------------------------------------------------------------------------\n" \
                            f"Assigned to: \t \t {name_assigned}\n" \
                            f"Task Name: \t \t     {task_title}\n" \
                            f"Task Description: \t {task_description}\n" \
                            f"Date Assigned: \t \t {date_issued}\n" \
                            f"Due Date: \t \t     {date_due}\n" \
                            f"Task Complete: \t \t {task_complete_no}\n" \
                            f"------------------------------------------------------------------------\n"
                   # append command is used to add each read task to a list
                read_task_list.append(read_task)

                    # if statement checks if the username used to log in matches the username tasks are assigned to
                if input_user == name_assigned:
                    # for loop prints every read_task variable for each task that is assigned to the logged in user
                    for read_task in read_task_list:
                        print(f"{read_task}\n")
    elif menu == 'e':
        print('Goodbye!')
        exit()

    else:
        print("You have made a wrong choice. Please Try again.")
