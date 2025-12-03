import todolist

tasks = []

print("Welcome to your to-do list!")

while True:
    option1 = todolist.menu_options()
    if option1 == 1:
        todolist.add_task(tasks)
    elif option1 == 2:
        todolist.show_tasks(tasks)
    else:
        todolist.mark_done(tasks)
    
    while True:
        try:
            print("\nDo you want to perform something else?")
            print("\n1) Yes, show me the options again")
            print("\n2) No, this was all I wanted to do")
            option2 = int(input("\nYour answer: "))
            if option2 not in {1, 2}:
                print("\nYou have to select a valid option within the provided range")
            else:
                break
        except ValueError:
            print("\nYou have to provide a numeric answer, please. Try again!")
    
    if option2 == 1:
        pass
    else:
        break

print("\nProcess Finished!")