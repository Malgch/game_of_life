class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def display_tasks(self):
        for task in self.tasks:
            print(task)

    def input_task(self):
        task = input("Enter a task: ")
        self.add_task(task)

    def delete_task(self):
        task = input("Delete task: ")
        self.delete_task(task)
