def first():
    try:
        name = input("Enter your name please: ")
        salary = int(input("Enter your desired salary level: "))
        tax = salary * 0.2
        print(f"Adam, the tax level you will pay with the salary {salary} is {int(tax)}")
    except:
        print("Error!")



def second():
    try:
        oper = int(input("Please chose the task you want to perform:\t1. Addition\t2. Multiplication\t3. Division\t4. Exponentiation\n"))
        if oper == 1:
            x = lambda a, b : a + b
        elif oper == 2:
            x = lambda a,b : a * b
        elif oper == 3:
            x = lambda a, b: a / b
        elif oper == 4:
            x = lambda a, b : a ** b

        print(x(3,2))
    except:
        print("Error!")



def third():
    try:
        n = int(input())
        a = 0
        b = 1
        sum = 0
        while sum <= n:
            print(a)
            a, b = b, a + b
            sum += 1
        print()
    except:
        print("Error!")

def forth():
    try:
        task = int(input("Code Output:\nPlease chose the task you want to perform:\n1. Enter items\n2. Exit"))
        if task == 1:
            user_input = input("Please enter items separated by comma")
            items = [item.strip().lower() for item in user_input.split(',')]

            item_counts = {}
            unique_items = set()
            not_unique_items = []

            for item in items:
                if item in item_counts:
                    item_counts[item] += 1
                else:
                    item_counts[item] = 1

            for item, count in item_counts.items():
                if count == 1:
                    unique_items.add(item)
                else:
                    not_unique_items.append((item, count))

            print(f"Unique items: {', '.join(unique_items)}")
            print(f"Not unique items: {', '.join([f'({item}, {count})' for item, count in not_unique_items])}")

        elif task == 2:
            print("q")
    except:
        print("Error!")


def five():
    tasks = []
    completed_tasks = []

    while True:
        print("Please choose the task you want to perform:")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Mark Task as Completed")
        print("4. View All Completed Tasks")
        print("5. Exit")

        choice = input()

        if choice == '1':
            task = input("Enter the task: ")
            tasks.append(task)
            print("Task added successfully!")

        elif choice == '2':
            if not tasks:
                print("No tasks to display.")
            else:
                print("All Tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")

        elif choice == '3':
            if not tasks:
                print("No tasks to mark as completed.")
            else:
                print("Tasks to Mark as Completed:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
                task_index = int(input("Enter the task number to mark as completed: "))
                if 1 <= task_index <= len(tasks):
                    completed_task = tasks.pop(task_index - 1)
                    completed_tasks.append(completed_task)
                    print(f"Task '{completed_task}' marked as completed!")

        elif choice == '4':
            if not completed_tasks:
                print("No completed tasks to display.")
            else:
                print("All Completed Tasks:")
                for i, task in enumerate(completed_tasks, 1):
                    print(f"{i}. {task}")

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("напиши число 1-5")


first()
second()
third()
forth()
five()