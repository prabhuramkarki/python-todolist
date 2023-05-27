import tkinter as tk

# Create a window
root = tk.Tk()
root.title("To-Do List")

# Create a list to store tasks
tasks = []

# Create functions to manipulate tasks
def add_task():
    task = task_input.get()
    if task:
        tasks.append(task)
        task_input.delete(0, tk.END)
        task_listbox.delete(0, tk.END)
        for task in tasks:
            task_listbox.insert(tk.END, task)

def remove_task():
    try:
        index = task_listbox.curselection()[0]
        task_listbox.delete(index)
        del tasks[index]
    except IndexError:
        pass

def clear_tasks():
    task_listbox.delete(0, tk.END)
    tasks.clear()

def save_tasks():
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")

def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            for line in f:
                task = line.strip()
                if task:
                    tasks.append(task)
        task_listbox.delete(0, tk.END)
        for task in tasks:
            task_listbox.insert(tk.END, task)
    except FileNotFoundError:
        pass

# Create a label and an entry field to add new tasks
task_label = tk.Label(root, text="Task:")
task_label.grid(row=0, column=0, padx=5, pady=5)

task_input = tk.Entry(root, width=30)
task_input.grid(row=0, column=1, padx=5, pady=5)

# Create a button to add new tasks
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.grid(row=0, column=2, padx=5, pady=5)

# Create a listbox to display tasks
task_listbox = tk.Listbox(root, height=10, width=40)
task_listbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

# Create buttons to remove tasks, clear tasks, and save/load tasks
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.grid(row=2, column=0, padx=5, pady=5)

clear_button = tk.Button(root, text="Clear Tasks", command=clear_tasks)
clear_button.grid(row=2, column=1, padx=5, pady=5)

save_button = tk.Button(root, text="Save Tasks", command=save_tasks)
save_button.grid(row=2, column=2, padx=5, pady=5)

load_button = tk.Button(root, text="Load Tasks", command=load_tasks)
load_button.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

# Load tasks from file (if exists)
load_tasks()

# Start the main loop
root.mainloop()
