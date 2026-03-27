from datetime import datetime
import textwrap
import sqlite3

db = sqlite3.connect('ToDoList.db')
c = db.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS tasks
                 (
                     id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                     name        VARCHAR(50),
                     priority    INTEGER,
                     description VARCHAR(250),
                     task_date   DATE
                 )''')


def close_db():
    db.commit()
    db.close()
    pass

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

def safe_len(prompt, leng):
    while True:
        res = input(prompt)
        if len(res) > leng:
            print(f"The string must be less than {leng} characters.")
            continue
        return res


class Task:
    def __init__(self, id_, name, priority, description, date = None):
        self.id = id_
        self.name = name
        self.priority = priority
        self.description = description
        self.date = date or datetime.now()

    def __str__(self):
        date_field = self.date.strftime("%Y/%d/%m %H:%M:%S")
        return (f'ID:{self.id} | Name: {self.name} | Priority: {self.priority} '
                f'| Description: {self.description[:10]}... | Date: {date_field}')

    def print_description(self):
        print(textwrap.fill(f'{self.name} -> {self.description}\n', width=40))

    def edit_task(self):
        while True:
            option = input(
                f'Choose what you want to change in {self.name} | 1 - Name | 2 - Priority | 3 - Description | 4 - See full description | 0 - Exit ')
            match option:
                case '0':
                    print('Cancelling...\n')
                    return
                case '1':
                    n = safe_len(f'Choose new name for {self.name}(no more than 50 characters): ', 50)
                    self.name = n
                    c.execute("UPDATE tasks SET name = ? WHERE id = ?", (self.name, self.id))
                    db.commit()
                    print(f'New name successfully changed to {self.name}\n')
                    return
                case '2':
                    p = safe_priority_input(f'Choose new priority for {self.name}: ')
                    self.priority = p
                    c.execute("UPDATE tasks SET priority= ? WHERE id = ?", (self.priority, self.id))
                    db.commit()
                    print(f'New priority successfully changed to {self.priority}\n')
                    return
                case '3':
                    d = safe_len(f'Choose new description for {self.name}(no more than 250 characters): ', 250)
                    self.description = d
                    c.execute("UPDATE tasks SET description= ? WHERE id = ?", (self.description, self.id))
                    db.commit()
                    print(f'New description successfully changed to {self.description}\n')
                    return
                case '4':
                    self.print_description()
                case _:
                    print("Please enter a valid option!")

class TaskManager:

    def __init__(self):
        self._tasks: list[Task] = []
        c.execute("SELECT * FROM tasks")

        def parse_date(date_str):
            try:
                return datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")
            except ValueError:
                return datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")

        for task in c:
            self._tasks.append(Task(task[0], task[1], task[2], task[3], parse_date(task[4])))

    def is_empty(self):
        return not self._tasks

    def get_task(self, task_id):
        for index, task in enumerate(self._tasks):
            if task.id == task_id:
                return task
        print(f'Task with ID: "{task_id}" not found!')
        return None

    def add(self):
        n = safe_len('Enter name for new task(no more than 50 characters): | 0 - Cancel ', 50)
        if n == '0':
            print('Cancelling...\n')
            return
        p = safe_priority_input('Enter priority for new task (0-10): ')
        d = safe_len('Enter description for new task(no more than 250 characters): ', 250)
        now = datetime.now()

        c.execute(
            "INSERT INTO tasks (name, priority, description, task_date) VALUES (?, ?, ?, ?)",
            (n, p, d, now)
        )
        task_id = c.lastrowid
        self._tasks.append(Task(task_id, n, p, d, now))
        print(f'Added new task {n} successfully!\n')
        db.commit()

    def delete(self):
        while True:
            for task in self._tasks:
                print(task)
            try:
                option = int(input('Choose Task ID to Delete | 0 - for exit: '))
                if option == 0:
                    return
                else:
                    task = self.get_task(option)
                    print(f'Successfully deleted task {task.name}\n')
                    c.execute("DELETE FROM tasks WHERE id = ?", (task.id,))
                    self._tasks.remove(task)
                    db.commit()
            except (TypeError, IndexError, ValueError, AttributeError):
                print("Please enter a valid index!")

    def print_sorted(self, by_priority=True):
        key = 'priority' if by_priority else 'date'
        sorted_tasks = sorted(self._tasks, key=lambda t: getattr(t, key))
        for task in sorted_tasks :
            print(task)
        print()

    def edit(self):
        while True:
            for task in self._tasks:
                print(task)
            try:
                option = int(input('Choose Task ID to edit | 0 - for exit: '))
                if option == 0:
                    return
                else:
                    task = self.get_task(option)
                    task.edit_task()
            except (TypeError, IndexError, ValueError, AttributeError):
                print("Please enter a valid index!")