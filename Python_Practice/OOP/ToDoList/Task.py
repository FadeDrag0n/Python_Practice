from datetime import datetime
import textwrap

def safe_priority_input(prompt):
    while True:
        try:
            res = int(input(prompt))
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

    def print_description(self):
        print(textwrap.fill(f'{self.name} -> {self.description}\n', width=40))

    def edit_task(self):
        while True:
            option = input(
                f'Choose what you want to change in {self.name} | 1 - Name | 2 - Priority | 3 - Description | 4 - See full description | 0 - Cancel ')
            match option:
                case '0':
                    print('Cancelling...\n')
                    return
                case '1':
                    n = input(f'Choose new name for {self.name}: ')
                    self.name = n
                    print(f'New name successfully changed to {self.name}\n')
                    return
                case '2':
                    p = safe_priority_input(f'Choose new priority for {self.name}: ')
                    self.priority = p
                    print(f'New priority successfully changed to {self.priority}\n')
                    return
                case '3':
                    d = input(f'Choose new description for {self.name}: ')
                    self.description = d
                    print(f'New description successfully changed to {self.description}\n')
                    return
                case '4':
                    self.print_description()
                case _:
                    print("Please enter a valid option!")

class TaskManager:

    def __init__(self):
        self._tasks: list[Task] = []

    def add(self):
        n = input('Enter name for new task: | 0 - Cancel ')
        if n == '0':
            print('Cancelling...\n')
            return
        p = safe_priority_input('Enter priority for new task (0-10): ')
        d = input('Enter description for new task: ')
        self._tasks.append(Task(n, p, d, datetime.now()))
        print(f'Added new task {n} successfully!\n')

    def delete(self):
        while True:
            for index, task in enumerate(self._tasks, start=1):
                print(f'№{index} | {task}')
            try:
                option = int(input('Choose Task index to Delete | 0 - for exit: '))
                if option == 0:
                    return
                else:
                    print(f'Successfully deleted task {self._tasks[option - 1].name}\n')
                    self._tasks.remove(self._tasks[option-1])
            except (IndexError, ValueError):
                print("Please enter a valid index!")

    def print_sorted(self, by_priority=True):
        key = 'priority' if by_priority else 'date'
        sorted_tasks = sorted(self._tasks, key=lambda t: getattr(t, key))
        for index, task in enumerate(sorted_tasks, start=1):
            print(f'№{index} | {task}')
        print()

    def edit_tasks(self):
        while True:
            for index, task in enumerate(self._tasks, start=1):
                print(f'№{index} | {task}')
            try:
                option = int(input('Choose Task index to edit | 0 - for exit: '))
                if option == 0:
                    return
                else:
                    self._tasks[option-1].edit_task()
            except (IndexError, ValueError):
                print("Please enter a valid index!")






manager = TaskManager()

# task2 = Task("Task 2", 12, "Task 3", datetime.now())
# task3 = Task("Task 3", 1, "Task 4", datetime.now())
# task4 = Task("Task 4", 10, "Task 5", datetime.now())
# task5 = Task("Task 5", 5, "Task 6", datetime.now())
# task6 = Task("Task 6", 25, "Task 7", datetime.now())
# task7 = Task("Task 7", 10, "Task 8", datetime.now())

# manager.add(task1)
# manager.add(task2)
# manager.add(task3)
# manager.add(task4)
manager.add()

manager.delete()



manager.edit_tasks()

# manager.delete(task1)       # Task 1 — удалён
# manager.print_sorted()      # сортировка по приоритету
# manager.print_sorted(False) # сортировка по дате