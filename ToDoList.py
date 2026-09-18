import csv

class Task:
    def __init__(self, subject, priority):
        self.subject = subject
        self.priority = priority
class ToDoList:
    def __init__(self):
        self.tasks = []
        self.load()

    def add_tasks(self, subject, priority):
        task = Task(subject, priority)
        self.tasks.append(task)

    def remove_tasks(self, subject, priority):
        for item in self.tasks:
            if item.subject == subject and item.priority == priority:
                self.tasks.remove(item)
                return
        return "there is no tasks like this"      

    def show(self):
        sorted_tasks = sorted(self.tasks, key = lambda task: int(task.priority))
        for task in sorted_tasks:
            print(f"subject : {task.subject} | priority: {task.priority}")
        

    def save(self):
        with open("tasks.csv", "w", newline="") as todolist:
            writer = csv.writer(todolist, delimiter = "|")
            for task in self.tasks :
                writer.writerow([task.subject, task.priority])

    def load(self):
        try:
            with open("tasks.csv", "r", newline="") as todolist:
                reader = csv.reader(todolist, delimiter = "|")
                for item in reader :
                    subject = item[0]
                    priority = int(item[1])
                    task = Task(subject, priority)
                    self.tasks.append(task)
        except FileNotFoundError:
            pass
        


        

todo = ToDoList()  
def menu():
    while(True):
        print("""
            1.add task
            2.remove task
            3.show ToDoList
            4.save ToDoList
            5.exit
              """)
        choice = input("Choose an option:")
        if choice == "1":
            subject = input("Subject:")
            priority = int(input("Priority:"))
            todo.add_tasks(subject, priority)

        elif choice == "2":
            subject = input("Subject:")
            priority = int(input("Priority:"))
            todo.remove_tasks(subject, priority)

        elif choice == "3":
            todo.show()

        elif choice == "4":
            todo.save()

        elif choice == "5":
            break

        else:
            print("please enter a num beteen 1 and 5:")


menu()