def add_task():
    try:
        with open("task.txt","a+") as f:
            task=input("Enter the task: ")
            if task:
                line=task+ "\n"
                f.write(line)
            else:
                print("Plese enter a valid task!")
    except Exception as e:
        print(f"An Error Occur which is '{e}'")


def remove_task():
    try:
        with open("task.txt", "r") as g:
            tasks = g.readlines()
        if not tasks:
            print("Task not found!!!")
            return
        print("=" * 15)
        for task in tasks:
            print(task.strip())
        print("=" * 15)
        task_to_remove = input("Enter the task you want to remove: ").strip()
        with open("task.txt", "w") as g:
            for task in tasks:
                if task.strip() != task_to_remove:
                    g.write(task)
    except Exception as e:
        print(f"An Error occur which is '{e}'")

def view():
    try:
        with open("task.txt", "r") as h:
            tasks = h.readlines()

        print("=" * 15)
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task.strip()}")
        print("=" * 15)

    except Exception as e:
        print(f"An Error occur which is '{e}'")

def main():
    while True:
        try:
            print("="*35,"\n")
            print("Choose the operation")
            print("1.Add the task\n2.Remove the task.\n3.View the To Do List\n4.Exit the program")
            choice=int(input("Enter the prefrence: "))
            print("="*35,"\n")
            try:
                if choice in range(1,5):
                    if choice==1:
                        add_task()
                        
                    elif choice==2:
                        remove_task()
                        
                    elif choice==3:
                        view()
                        
                    elif choice==4:
                        print("Thanks for operating on this.")
                        exit()
                else:
                    print("Invalid Choice")
            except Exception as e:
                print(f"An Error occur which is '{e}'")
        except Exception as e:
            print(f"An error occurr which is '{e}'")

if __name__=="__main__":
    main()