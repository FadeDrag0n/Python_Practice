from Task import TaskManager as Tm

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
        choose_option = input("1 - Add new task | 2 - delete task | 3 - edit task | 4 - view tasks | 5 - exit ")
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
                    name_option = input("Enter a name to see description: | 0 - Exit ")
                    if name_option == '0':
                        print('\n')
                        continue
                    task = manager.get_task(name_option)
                    if task:
                        task.print_description()
                    else:
                        print(f"Sorry, {name_option} is not in your tasks!\n")
                except ValueError:
                    print("Invalid option!")

            case '5':
                print('Goodbye!')
                break

            case _:
                print("Invalid option!")