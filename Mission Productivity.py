import pandas as pd
class Task_Manager:
    def __init__(self):
        self.Tasks = {}

    def add(self, sprint, status):
        self.Tasks[sprint] = status
    
    def remove(self, sprint):
        if (sprint not in self.Tasks):
            print("Task is not present in To-Do List!")
            return
        else:
            self.Tasks.pop(sprint)

    def show(self):
        if not self.Tasks:
            print("Your to-do list is empty!")
            return
        else:
            print("Here is your To-Do List")
            df=pd.DataFrame(list(self.Tasks.items()), columns=['Tasks', 'Status'])
            print(df)

    def manage(self):
        print("Hi, Welcome to your To Do list manager!")
        while True:
            print("Options:")
            print("1. Add or update a task")
            print("2. Remove a task")
            print("3. View all tasks")
            print("4. Exit")
            choice = input("Enter your next choice: ")

            if choice == '1':
                key = input("Enter a task you want to update: ").lower()
                value = input("Enter the status of your task ['Completed' or 'Pending']: ").lower()
                self.add(key, value)
                self.show()
            elif choice == '2':
                key = input("Enter a task you want to remove: ").lower()
                self.remove(key)
                self.show()
            elif choice == '3':
                self.show()
            elif choice == '4':
                print("Exiting...!")
                break
            else:
                print("Invalid Choice!! Please try again")
                continue



if __name__ == "__main__":
    m = Task_Manager()
    m.manage()