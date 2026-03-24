from datetime import datetime
import textwrap

def safe_priority_input():
    while True:
        try:
            res = int(input('Enter priority for your task: '))
            if 0 <= res <= 10:
                return res
            else:
                print('Priority must be between 0 and 10')
        except ValueError:
            print("Please enter a valid value!")

class Task:
    def __init__(self, name, priority, description, date = datetime.now()):
        self.name = name
        self.priority = priority
        self.description = description
        self.date = date

    def __str__(self):
        date_field = self.date.strftime("%Y/%d/%m %H:%M:%S")
        return (f'Name: {self.name} | Priority: {self.priority} '
                f'| Description: {self.description[:10]}... | Date: {date_field}')

class TaskManager:

    def __init__(self):
        self._tasks: list[Task] = []

    def add(self, task: Task):
        self._tasks.append(task)
        return self

    def delete(self, task: Task):
        if task in self._tasks:1
            self._tasks.remove(task)
            print(f"{task.name} — удалён")

    def print_sorted(self, by_priority=True):
        key = 'priority' if by_priority else 'date'
        sorted_tasks = sorted(self._tasks, key=lambda t: getattr(t, key))
        for index, task in enumerate(sorted_tasks, start=1):
            print(f'№{index} | {task}')
        print()

    def print_description(self, index):
        task = self._tasks[index]
        print(textwrap.fill(f'{task.name} -> {task.description}\n', width=40))
        print()


    def edit_tasks(self):
        for index, task in enumerate(self._tasks):
            print(f'№{index} | {task}')






manager = TaskManager()

task1 = Task("Task 1", 10, "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. ", datetime.now())
task2 = Task("Task 2", 12, "Task 3", datetime.now())
task3 = Task("Task 3", 1, "Task 4", datetime.now())
task4 = Task("Task 4", 10, "Task 5", datetime.now())
task5 = Task("Task 5", 5, "Task 6", datetime.now())
task6 = Task("Task 6", 25, "Task 7", datetime.now())
task7 = Task("Task 7", 10, "Task 8", datetime.now())

manager.add(task1)
manager.add(task2)
manager.add(task3)
manager.add(task4)
manager.add(task5)
manager.add(task6)
manager.add(task7)

manager.print_description(0)

# manager.delete(task1)       # Task 1 — удалён
# manager.print_sorted()      # сортировка по приоритету
# manager.print_sorted(False) # сортировка по дате