from Task import TaskManager as Tm
from Task import close_db

if __name__ == "__main__":

    manager = Tm()


    def requires_tasks(action):
        if manager.is_empty():
            print("You don't have any tasks!\n")
            return False
        if action:
            action()
        return True


    while True:
        print("|------------------------------- ToDo List Menu -------------------------------|")
        choose_option = input("1 - Add new task | 2 - Delete task | 3 - Edit task | 4 - View tasks | 5 - Save & exit ")
        match choose_option:
            case '1':
                manager.add()

            case '2':
                requires_tasks(manager.delete)

            case '3':
                requires_tasks(manager.edit)

            case '4':
                if not requires_tasks(None):
                    continue
                try:
                    sort_option = int(input("Enter sort option: | 1 - priority | 0 - date "))
                    manager.print_sorted(bool(sort_option))
                    id_option = int(input("Enter ID to see description: | 0 - Exit "))
                    if id_option == 0:
                        print('\n')
                        continue
                    task = manager.get_task(id_option)
                    if task:
                        task.print_description()
                except ValueError:
                    print("Invalid option!")

            case '5':
                print('Goodbye!')
                close_db()
                break

            case _:
                print("Invalid option!")