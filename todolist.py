import datetime 
import json

def menu_options():
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
    return option

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
    
    # --- START OF MODIFIED PRIORITY SECTION ---
    priority_map = {1: "Low", 2: "Normal", 3: "High"}
    
    while True:
        try:
            print("\nPick the priority of this task")
            print("\n1) Low")
            print("\n2) Normal")
            print("\n3) High")
            priority_option = int(input("\nOption: "))
            
            # Check if the input is a valid key in the map
            if priority_option not in priority_map:
                print("\nYou have to select one of the provided options")
            else:
                # Assign the string value directly from the map
                priority = priority_map[priority_option]
                break
        except ValueError:
            print("\nYou have to provide a valid numeric option")
    # --- END OF MODIFIED PRIORITY SECTION ---
    
    task = {
        "name": name,
        "description": description,
        "date": date,
        "priority": priority,
        "status": False #It indicates if the task has been resolved or not
    }

    tasks.append(task)


def show_tasks(tasks):
    print("\nList of all tasks:\n\n")
    for i in range(len(tasks)):
        print("##############################################")
        print(f"\nTask {i+1}:")
        print(f"\nName: {tasks[i]["name"]}")
        print(f"\nDescription: {tasks[i]["description"]}")
        print(f"\nDate: {tasks[i]["date"]}")
        print(f"\nPriority: {tasks[i]["priority"]}")
        if tasks[i]["status"] == False:
            print("\nStatus: Not resolved")
        else:
            print("\nStatus: Resolved")
        print("\n##############################################\n")


def mark_done(tasks):
    print("\nThese are all of your tasks")
    show_tasks(tasks)
    while True:
        try:
            option = int(input("\nWhich of the tasks you want to mark as resolved: "))
            if option < 1 or option > len(tasks):
                print("\nYou have to select a valid value among the ones provided, try again")
            else:
                if tasks[option-1]["status"] == True:
                    print("\nThis task is already solved")
                else:
                     tasks[option-1]["status"] = True
                break
        except ValueError:
            print("\nYou have to provide a valid numeric answer, try again")
    print("\nTask completed!")

def save_tasks(tasks):
    """Saves the current list of tasks to a JSON file."""
    # datetime.date objects are not directly JSON serializable,
    # so we convert them to strings before saving.
    serializable_tasks = []
    for task in tasks:
        # Create a copy so we don't modify the date object in the main list
        temp_task = task.copy()
        # Convert the date object to an ISO format string (e.g., '2025-12-05')
        temp_task["date"] = temp_task["date"].isoformat()
        serializable_tasks.append(temp_task)

    try:
        with open("tasks.json", "w") as f:
            json.dump(serializable_tasks, f, indent=4)
        print("\nTasks saved successfully.")
    except Exception as e:
        print(f"\nError saving tasks: {e}")

def load_tasks():
    """Loads tasks from a JSON file, or returns an empty list if the file doesn't exist."""
    try:
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
            # JSON reads the 'date' back as a string, so we convert it back to a datetime.date object.
            for task in tasks:
                # The date string needs to be parsed back into a date object
                task["date"] = datetime.date.fromisoformat(task["date"])
            print("\nTasks loaded successfully.")
            return tasks
    except FileNotFoundError:
        # This is expected on the first run, so we return an empty list
        return []
    except Exception as e:
        print(f"\nError loading tasks: {e}. Starting with an empty list.")
        return []