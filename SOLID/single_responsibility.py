class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, task):
        self.tasks.remove(task)

class TaskPresenter:
    @staticmethod
    def display_tasks(tasks):
        for task in tasks:
            print(task)

class TaskInput:
    @staticmethod
    def input_task():
        return input("Enter a task")

    @staticmethod
    def delete_task():
        task = input("Delete task ")
        return task
