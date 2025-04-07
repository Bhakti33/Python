from tkinter import *
from tkinter import messagebox

# Initialize the main window
root = Tk()
root.title("To-Do List")
root.geometry("400x500")

# List to store tasks
tasks = []

# Function to update the task list display
def update_task_list():
    task_listbox.delete(0, END)  # Clear the listbox
    for task in tasks:
        task_listbox.insert(END, task)  # Insert all tasks

# Function to add a task
def add_task():
    task = task_entry.get()
    if task.strip():  # Ensure the task isn't empty
        tasks.append(task)
        task_entry.delete(0, END)  # Clear the entry box
        update_task_list()
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

# Function to delete the selected task
def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        tasks.pop(selected_task_index)  # Remove the selected task
        update_task_list()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

# UI Elements
# Input Field
task_entry = Entry(root, width=30, font=("Arial", 14))
task_entry.pack(pady=10)

# Add Button
add_button = Button(root, text="Add Task", command=add_task, font=("Arial", 12), bg="lightgreen")
add_button.pack(pady=5)

# Task List
task_listbox = Listbox(root, width=40, height=15, font=("Arial", 12), selectmode=SINGLE)
task_listbox.pack(pady=10)

# Delete Button
delete_button = Button(root, text="Delete Task", command=delete_task, font=("Arial", 12), bg="lightcoral")
delete_button.pack(pady=5)

# Run the application
root.mainloop()
