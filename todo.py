#import the tkinter modules

import tkinter as tk # import the tkinter library as tk for easier reference

from tkinter import messagebox # import the messagebox module from 
                               #tkinter for displaying message boxes

from PIL import ImageTk, Image  # import the ImageTk and Image modules from PIL 
                                #(Python Imaging Library) for displaying images
                                 
# Define a class for the TodoList application
class Todo:

    selected_tasks = ["Running", "Walk Dog", "Clean Room", "Shopping", "Research", "Call Mom", "Workout", "Swimming", "Sleeping", "Reading", "Studying", "Netflix"]

    def __init__(self, master): # set the master window as an attribute of the Todo class

        # Set the master window
        self.master = master
        self.master.title("Everything You Need")

        # Create the main frame and pack it
        self.main_frame = tk.Frame(self.master)
        self.main_frame.pack(fill=tk.BOTH, expand=True) # pack the main frame and fill the entire space


        # Create a label for the task list and pack it
        self.task_label = tk.Label(self.main_frame, text="One day at a time: Things to do!!")
        self.task_label.pack(side=tk.TOP, padx=10, pady=5)

        self.task_label = tk.Label(self.main_frame, text="Task List -->")
        self.task_label.pack(side=tk.LEFT, padx=10, pady=5)

        # Initialize the task list
        self.tasks = []

        # Create the to-do list and pack it
        self.task_frame = tk.Listbox(self.main_frame, selectmode=tk.MULTIPLE)
        self.task_frame.pack(side=tk.LEFT, padx=10, pady=10)

        # Create the scrollbar and pack it
        self.scrollbar = tk.Scrollbar(self.main_frame) # create a scrollbar widget for the task frame
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)  # pack the scrollbar widget and place it on the right of the frame

        # Attach the scrollbar to the task frame
        self.task_frame.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_frame.yview)

        # Create a label for the buttons and pack it
        self.buttons_label = tk.Label(self.main_frame, text="ONE DAY AT A TIME! TODAY YOU CONQUERED THE WORLD!!")
        self.buttons_label.pack(side=tk.BOTTOM, padx=10, pady=5)

        # Create the buttons frame and pack it
        self.buttons_frame = tk.Frame(self.main_frame)
        self.buttons_frame.pack(side=tk.BOTTOM, padx=10, pady=10)

        # Create the "Add Task" button and pack it
        self.add_button = tk.Button(self.buttons_frame, text="Add Task", command=self.add_task)
        self.add_button.pack(side=tk.LEFT)

        # Create the "Delete Task" button and pack it
        self.delete_button = tk.Button(self.buttons_frame, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT)

        # Create the "Exit" button and pack it
        self.exit_button = tk.Button(self.buttons_frame, text="Exit", command=self.master.destroy)
        self.exit_button.pack(side=tk.RIGHT)

        # Bind the ListboxSelect event to update the selected tasks
        self.task_frame.bind('<<ListboxSelect>>', self.update_selected_tasks)

        # Create the images
        self.image1 = tk.PhotoImage(file="image1.png")
        self.image2 = tk.PhotoImage(file="image2.png")

        # Create the labels for the images
        self.label1 = tk.Label(self.main_frame, image=self.image1, text="Image 1")
        self.label1.pack(side=tk.TOP, padx=10, pady=10)

        self.label2 = tk.Label(self.main_frame, image=self.image2, text="Image 2")
        self.label2.pack(side=tk.TOP, padx=10, pady=10)

    def add_task(self):
        # Create the add task window
        add_window = tk.Toplevel(self.master)
        add_window.title("Add Task")

        # Create the task entry field
        task_entry = tk.Entry(add_window, width=50)
        task_entry.pack(padx=10, pady=10)

        # Create the add button
        add_button = tk.Button(add_window, text="Add", command=lambda: self.add_task_handler(add_window, task_entry.get()))
        add_button.pack(padx=10, pady=10)

        # Bind the Enter key to the add button
        add_window.bind('<Return>', lambda event: add_button.invoke())

    def add_task_handler(self, add_window, task):
        if task not in self.selected_tasks:
            messagebox.showerror("Error", "Please enter a valid task (Running, Walk Dog, Clean Room, Shopping, Call Mom, Workout, Swimming, Sleeping, Reading, Studying, Netflix)!")
            return
        if task.isnumeric() or not task.strip():
            messagebox.showerror("Error", "Please enter a valid task!")
            return

        # Add the task to the task list
        self.tasks.append(task)

        # Add the task to the task frame
        self.task_frame.insert(tk.END, task)

        # Clear the add task window
        add_window.destroy()

    def delete_task(self):
        # Get the selected tasks' indexes
        selected_indexes = self.task_frame.curselection()
        selected_indexes = tuple(int(index) for index in selected_indexes)

        # Remove the tasks from the task list and the task frame
        for index in reversed(selected_indexes):
            self.tasks.pop(index)
            self.task_frame.delete(index)

    def update_selected_tasks(self, event):
        # Get the selected tasks
        selected_tasks = [self.task_frame.get(index) for index in self.task_frame.curselection()]

        # Print the selected tasks
        print("Selected tasks:", selected_tasks)


if __name__ == "__main__":
    root = tk.Tk()
    app = Todo(root)
    root.mainloop()
