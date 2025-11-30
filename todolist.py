import datetime 

def main():
    print("Welcome to your to-do list!")
    while True:
        try:
            print("\nChoose an action between the following ones:")
            print("\n1) Add a task")
            print("\n2) View all tasks")
            print("\n3) Mark a task as complete")
            option = int(input("\nOption: "))
            if option not in {1,2,3}:
                print("\nYou have to select one of the three possible options")
            else:
                break
        except ValueError:
            print("\nYou have to select a valid numeric option")

def add_task(tasks):
    name = input("\nName of the task: ")
    description = input("\nDescription of the task: ")
    while True:
        try:
            print("\nNow, pick a date for completing this task:")
            print("\n1) Today")
            print("\n2) Tomorrow")
            print("\n3) The day after tomorrow")
            print("\n4) Choose a specific date")
            option = int(input("\nOption: "))
            if option not in {1,2,3,4}:
                print("\nYou have to choose a valid option between the ones provided")
            else:
                break
        except ValueError:
            print("\nyou have to pick a valid numeric option")
    date = datetime.date.today()
    match option:
        case 1:
            pass
        case 2:
            date = date + datetime.timedelta(days=1)
        case 3:
            date = date + datetime.timedelta(days=2)
        case 4:
            while True:
                try:
                    day = int(input("\nPick a day: "))
                    month = int(input("\nPick a month: "))
                    year = int(input("\nPick a year: "))
                    date = datetime.date(year, month, day)
                    if date < datetime.date.today():
                        print("\nUnless you have a time machine, you have to select another date")
                        print("\nTry again, please")
                    else:
                        break
                except ValueError:
                    print("\nYou have to choose a valid date, please")
    while True:
        try:
            print("\nPick the priority of this task")
            print("\n1) Low")
            print("\n2) Normal")
            print("\n3) High")
            priority = int(input("\nOption: "))
            if priority not in {1,2,3}:
                print("\nYou have to select one of the provided options")
            else:
                if priority == 1:
                    priority = "Low"
                elif priority == 2:
                    priority = "Normal"
                else:
                    priority = "High"
                break
        except ValueError:
            print("\nYou have to provide a valid numeric option")
    
    task = {
        "name": name,
        "description": description,
        "date": date,
        "priority": priority
    }

    tasks.append(task)


def show_tasks(tasks):
    for i in range(len(tasks)):
        print("\nList of all tasks:\n\n")
        print("##############################################")
        print(f"\nTask {i+1}:")
        print(f"\nName: {tasks[i]["name"]}")
        print(f"\nDescription: {tasks[i]["description"]}")
        print(f"\nDate: {tasks[i]["date"]}")
        print(f"\nPriority: {tasks[i]["priority"]}")
        print("\n##############################################\n")


tasks = []
add_task(tasks)
show_tasks(tasks)