# This program allows the user to register new users, create tasks and assign them to a user, view all tasks and view
# their own tasks.
# The admin can generate reports that displays statistics in separate txt files.

# datetime imported to use time
from datetime import datetime

# Global variables

today = datetime.today()
today = today.strftime("%d/%m/%Y")
read_task_list = []
menu_choice = 0
completed_tasks = []
not_completed = []
overdue = []
total_tasks_1 = []
total_users = []
user_tasks = []


# Functions used for the program

# username_check function opens and reads user.txt. If there is not an empty line then the program adds the user
# and their password to the users dictionary
def username_check():
    users = {}

    with open("user.txt", "r") as f:
        for line in f:
            user_check = line.strip("\n")

            if user_check != "":
                user_check = user_check.split(", ")
                users.update({user_check[0]: user_check[1]})

    return users


# task_check function opens and reads tasks.txt and if there is not a blank line the information is split on the comma
# and extended to the tasks list.
def task_check():
    tasks = []
    count = 1

    with open("tasks.txt", "r") as f:
        for line in f:
            task_check = line.strip("\n")

            if task_check != "":
                task_check = [task_check.split(", ") + [count]]
                tasks.extend(task_check)
                count += 1

    return tasks


# user_statistics function opens and reads the user.txt file, calculates the length of the lines which is used to
# identify the amount of users.
def user_statistics():
    with open("user.txt", "r") as a:
        total_users = len(a.readlines())
        print(f"________________________________________\nThere are a total of {total_users} registered users.\n_______"
              f"_________________________________")


# task_statistics function opens and reads the tasks.txt file, calculates the length of the lines which is used to
# identify the amount of users.
def task_statistics():
    with open("tasks.txt", "r") as b:
        total_tasks = len(b.readlines())
        print(f"________________________________________\nThere are a total of {total_tasks} registered tasks.\n_______"
              f"_________________________________")


# register_user functions opens and appends+ the user.txt file with the newly registered user.
def register_user():
    with open("user.txt", "a+") as f:
        # seek is used to find the beginning of the file after continue in the while not loop
        f.seek(0)
        names = []
        for line in f.readlines():
            temp = line.split(",")[0].strip()
            names.append(temp)

        # while registered is False the user will be prompted to input a username to register
        registered = False

        while not registered:
            print("\nEnter the name and password of the user you would like to register")
            new_user_name = input("Username: ")
            if new_user_name in names:
                print("Username already exists.\n")
                continue

            # if the username is available then a password and confirmation password are required
            new_user_password = input("Password: ")
            confirm_password = input("Confirm password: ")

            # if confirmation password does not match then the user is displayed an error message and the continue
            # takes them back to having to input a user again
            if new_user_password != confirm_password:
                print("Your passwords do not match.\n")
                continue

            # credentials are written to the user.txt file
            f.write(f"\n{new_user_name}, {new_user_password}")
            print("New user registered.\n")

            # once registered is True the while not loop will be broken
            registered = True


# add_task function opens and appends+ tasks.txt file with the relevant information for the new task
def add_task():
    with open("tasks.txt", "a+") as d:
        # range of user input needed to describe the task
        new_task_username = input("Enter the username of whom the task will be assigned to: ")
        new_task_title = input("Enter a title for the task: ")
        task_description = input("Please enter a description of the task: ")
        task_due_date = input("Please enter the due date of the task in day/month/year format. E.g. 05/11/2022: ")
        is_task_complete = "No"

        # list created with the user variables assigned. The new task information is appended to the list
        # today[0:10] will always be whatever day the task has been created on. [0:10] specifies just the date and cuts
        # out the time of the file being created
        new_task_information_list = []
        new_task_information = f"{new_task_username}, {new_task_title}, {task_description}, {today[0:10]}, " \
                               f"{task_due_date}, {is_task_complete}"

        new_task_information_list.append(new_task_information)

        # the new task information is written to the tasks.txt file
        for new_task_information in new_task_information_list:
            d.write(f"{new_task_information}\n")


# view_all function creates an empty task_list and opens and reads the tasks.txt file. Each line is stripped and split
# the new information stored as the temp variable. Various variables are then created by the index of the information
def view_all():
    read_task_list = []
    with open('tasks.txt', 'r') as f:
        for line in f.readlines():
            temp = line.strip().split(", ")
            name_assigned = temp[0]
            task_title = temp[1]
            task_description = temp[2]
            date_issued = temp[3]
            date_due = temp[4]
            task_complete_no = temp[5]

            # read_task variable has assigned each individual element of the task in a user-friendly way
            read_task = "-------------------------------------------------------------------------\n" \
                        f"Assigned to: \t \t {name_assigned}\n" \
                        f"Task Name: \t \t     {task_title}\n" \
                        f"Task Description: \t {task_description}\n" \
                        f"Date Assigned: \t \t {date_issued}\n" \
                        f"Due Date: \t \t     {date_due}\n" \
                        f"Task Complete: \t \t {task_complete_no}\n" \
                        f"------------------------------------------------------------------------\n"
            # read_task is appended to read_task_list
            read_task_list.append(read_task)

        # read_task_list has been enumerated to show the number of the task
        for num, read_task in enumerate(read_task_list):
            print(f"\t \t \t \t \tTask number: {num}\n{read_task}\n")

# open_tasks function opens and reads the tasks.txt file
def open_tasks():
    with open('tasks.txt', 'r') as f:
        for line in f.readlines():
            data = line.strip().split(", ")
            read_task_list.append(data)


# write_file opens and writes+ to the tasks.txt file
def write_file():
    with open('tasks.txt', 'w+') as f:
        for task in read_task_list:
            f.write(f"{', '.join(task)}\n")


# generate_reports allows the admin to generate a user_overview.txt report that displays statistics relevant to the
# registered users and a tasks_overview.txt file that displays statistics relevant to the registered tasks.
def generate_reports():
    # calls the users and task functions
    users = username_check()
    task = task_check()
    # converts users dictionary into a list
    users = [*users]
    total = len(task)
    total_users = len(users)
    complete = 0
    incomplete = 0
    overdue = 0
    percent_incomplete = 0
    percent_overdue = 0

    # for loop that runs for the duration of tasks in the tasks.txt file
    for i in range(0, total):
        # if fifth index on each line is "Yes" then the complete counter increases by 1
        if task[i][5].capitalize() == "Yes":
            complete += 1
        # if the fifth index on each line is "No" and the due date is less than today's date then the incomplete
        # and overdue counters increases by 1
        elif task[i][5].lower() == "no" and datetime.strptime(task[i][4], "%d/%m/%Y") < datetime.today():
            incomplete += 1
            overdue += 1
            # percentage of incomplete and overdue tasks are calculated
            percent_incomplete = (incomplete / total) * 100
            percent_overdue = (overdue / total) * 100
        # if the fifth index on each line is only "No" but still within the due date then only the incomplete counter
        # will increase
        elif task[i][5].lower() == "no":
            incomplete += 1
            percent_incomplete = (incomplete / total) * 100

    # task_overview.txt file is generated in a user friendly manner
    with open("task_overview.txt", "w") as f:
        f.write(f"----------------------REPORT GENERATED {today[0:16]}--------------------\n\n")
        f.write(f"Total number of tasks registered:     \t\t\t\t{total}\n")
        f.write(f"Total number of tasks completed:     \t\t\t\t{complete}\n")
        f.write(f"Total number of tasks not completed:\t\t\t\t{incomplete}\n")
        f.write(f"Total number of tasks overdue and not completed:\t\t{overdue}\n")
        f.write(f"Total percentage of tasks not completed:\t\t\t\t{percent_incomplete:.1f}%\n")
        f.write(f"Total percentage of tasks overdue:\t\t\t\t\t{percent_overdue:.1f}%\n")
        f.write(f"\n----------------------END OF REPORT----------------------------------")
        print("\nTask overview report generated.")

    # the beginning of user_overview.txt file is generated in a user friendly way
    with open("user_overview.txt", "w") as g:
        g.write(f"------------------REPORT GENERATED {today[0:16]}-----------------\n\n")
        g.write(f"\t\t\tTotal number of users registered\t- {total_users}\n")
        g.write(f"\t\t\tTotal number of tasks registered\t- {total}\n\n")

        # the rest of user_overview.txt relies on user specific data which needs to be calculated
        # for loop which iterates for the length of total_users in the file
        for i in range(0, total_users):
            user_tasks = 0
            completed = 0
            not_complete = 0
            user_overdue = 0
            task_percent = 0
            percent_complete = 0
            percent_not_complete = 0
            percent_overdue = 0

            # for loop which iterates for the amount of tasks a user has
            for j in range(0, total):
                # if user name and task[0] match and task[5] is "Yes" then the counters for user_tasks and completed
                # increase by 1
                if users[i] == task[j][0] and task[j][5].capitalize() == "Yes":
                    user_tasks += 1
                    completed += 1
                #if user name and task[0] mathc and task[5] is "No" and task[1][4], which is the due date, is less than
                # today then the user_tasks, not_complete and user_overdue counters increase by 1
                elif users[i] == task[j][0] and task[j][5].capitalize() == "No" and datetime.strptime(task[i][4],
                                                                                                      "%d/%m/%Y") < datetime.today():
                    user_tasks += 1
                    not_complete += 1
                    user_overdue += 1
                #if user name and task[0] and task[5] is "No" then only user_tasks and not_complete counters increase
                # by 1
                elif users[i] == task[j][0] and task[j][5].capitalize() == "No":
                    user_tasks += 1
                    not_complete += 1
                # task_percent is calculated
                task_percent = (user_tasks / total) * 100

                # if a user has at least 1 task then the appropriate percentages are calculated
                if user_tasks != 0:
                    percent_complete = (completed / user_tasks) * 100
                    percent_not_complete = (not_complete / user_tasks) * 100
                    percent_overdue = (user_overdue / user_tasks) * 100

            # the rest of the user_overview.txt file is written in a user-friendly way
            g.write("-" * 62 + "\n")
            g.write(f"User: {users[i]}\n\n")
            g.write(f"Total number of user tasks\t\t\t\t- {user_tasks}\n")
            g.write(f"Total percentage of all tasks\t\t\t\t- {task_percent:.2f}%\n")
            g.write(f"Total percentage of user tasks completed\t\t- {percent_complete:.2f}%\n")
            g.write(f"Total percentage of user tasks not completed\t- {percent_not_complete:.2f}%\n")
            g.write(f"Total percentage of user tasks overdue\t\t- {percent_overdue:.2f}%\n")

        g.write(f"\n-------------------------END OF REPORT------------------------")
        print("User overview report generated.\n")


# view_mine function allows the user to view only their tasks. Some information in each task can be edited by
# the registered user
def view_mine():
    # tasks.txt file is open and read with each line being stripped and split
    with open('tasks.txt', 'r') as f:
        for line in f.readlines():
            temp = line.strip().split(", ")
            read_task_list.append(temp)

        # the information in read_task_list is enumerated which makes it easier to identify a task
        for num, temp in enumerate(read_task_list):
            name_assigned = temp[0]
            task_title = temp[1]
            task_description = temp[2]
            date_issued = temp[3]
            date_due = temp[4]
            is_task_complete = temp[5]

            # read_task variable is created which has individual indexes  from the line assigned
            read_task = "-------------------------------------------------------------------------\n" \
                        f"Assigned to: \t \t {name_assigned}\n" \
                        f"Task Name: \t \t     {task_title}\n" \
                        f"Task Description: \t {task_description}\n" \
                        f"Date Assigned: \t \t {date_issued}\n" \
                        f"Due Date: \t \t     {date_due}\n" \
                        f"Task Complete: \t \t {is_task_complete}\n" \
                        f"------------------------------------------------------------------------\n\n"

            # if the input_user and name assigned to a task match then the task will be printed in a user-friendly way
            if input_user == name_assigned:
                print(f"\t\t\t\t\tTask number: {num}\n{read_task}")

    # while loop which always asks the user which task number they would like to edit. The user breaks out of this by
    # typing "-1"
    while True:
        question = int(input("What task would you like to edit? -1 to exit:  "))

        if question == -1:
            break

        elif question != -1:
            # the fifth index of the task the user would like to edit is assigned to is_task_complete variable
            is_task_complete = read_task_list[question][5]
            # if the fifth index of the task is "Yes" then the task is already complete and cannot be edited
            if is_task_complete.capitalize() == "Yes":
                print("This task has already been completed and cannot be edited.\n")
                break
            # if the fifth index of the task is "No" then the task can be edited. This will ask the user to input
            # whether they would like to mark the task as complete and assign a new name to the task
            elif is_task_complete.capitalize() == "No":
                complete = input("Would you like to mark the task as 'complete'? Yes/No: ".capitalize())

                new_name = input(
                    "Type in the username of whom you would like to allocate this task to. If you would like to "
                    "keep it assigned to yourself then re-type your name: ")

                new_date = input(
                    "Type in the new date for which the assignment must be completed by in years, month and "
                    "day. For example 2022-12-05 for 5th December 2022: ")

                # the task the user would like to edit is assigned a new variable name which has the appropriate
                # indexes manipulated to reflect the edited information
                new_data = read_task_list[question]
                task_title = new_data[1]
                task_description = new_data[2]
                date_issued = new_data[3]

                # the new information is assigned to the position in the read_task_list of the user's earlier choice
                read_task_list[question] = [new_name, task_title, task_description, date_issued, new_date, complete]
                print("\nThe task has been updated.\n")
                # write_file function is called that will write the new information to tasks.txt
                write_file()
                break

            else:
                print("Username does not exist\n")

            continue


# admin_menu functions prints the admin menu
def admin_menu():
    print("r - Registering a user")
    print("a - Adding a task")
    print("va - View all tasks")
    print("vm - View my task")
    print("gr - Generate Reports")
    print("s - Statistics")
    print("e- Exit")


# print_menu function prints the regular user menu
def print_menu():
    print("a - Adding a task")
    print("va - View all tasks")
    print("vm - View my task")
    print("e - Exit")


# Main program
# while loop which runs while the user attempts to log in using their username and password
while True:

    input_user = input("Enter your username: ")
    input_password = input("Enter your password: ")

    # logged_in and user assigned to False
    logged_in = False
    user = False

    # user.txt is opened and read with user_name and password defined
    with open("user.txt", "r") as f:
        for line in f.readlines():
            temp = line.strip().split(", ")
            user_name = f"{temp[0]}"
            password = f"{temp[1]}"

            # is matching credentials then user is logged in = True
            if input_user == user_name and input_password == password:
                print("You have successfully logged in.")
                logged_in = True
                break

            # is only the username matches then only user = True
            elif input_user == user_name and input_password != password:
                user = True
                break

    if logged_in:
        break

    # if only user = True then appropriate error message is displayed
    elif user:
        print("You entered the incorrect password.")

    # if username and password are incorrect then appropriate error message is displayed
    else:
        print("You entered the incorrect username and password.")
    # once user logs in then while loop is broken

# new while loop which allows the logged_in user to navigate the program menu
# the logged_in menu calls on the relevant functions
while True:
    admin = False

    if input_user == "admin" and input_password == "adm1n":
        admin = True

    if admin:
        admin_menu()
        admin_choice = input("Type in your option (r, a, va, vm, gr,s, e): ".lower())

        if admin_choice == 'r':
            register_user()

        elif admin_choice == 'a':
            add_task()

        elif admin_choice == 'va':
            view_all()

        elif admin_choice == 'vm':
            view_mine()

        elif admin_choice == 'gr':
            generate_reports()

        elif admin_choice == 's':
            user_statistics()
            task_statistics()

        elif admin_choice == 'e':
            print("Goodbye.")
            break

        else:
            print("Please make a valid selection")
            admin_menu()

    elif input_user != "admin" and input_password != "adm1n":
        admin = False

        if not admin:
            print_menu()
            menu_choice = input("Type in your option (a, va, vm, e): ".lower())

            if menu_choice == "a":
                add_task()

            elif menu_choice == "va":
                view_all()

            elif menu_choice == "vm":
                view_mine()

            elif menu_choice == "e":
                print("Goodbye.")
                break

            else:
                print("You did not make a valid selection.")
                print_menu()

