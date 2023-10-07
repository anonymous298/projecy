def to_do(lst):
    add = input("Enter Your Task: ")
    lst.append(add)

def to_read(lst):
    print(lst)

def more_tasks():
    while True:
        print("\nWrite (i) To Add Tasks")
        print("Write (r) To See Tasks")
        user = input("\nEnter Here: ").strip().lower()

        if user == "i":
            to_do(lst)

        elif user == "r":
            to_read(lst)

        else:
            print("Invalid Input.Please enter 'i' or 'r'")

lst = []
to_do(lst)
more_tasks()



