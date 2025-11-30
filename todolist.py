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