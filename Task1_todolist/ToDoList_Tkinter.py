"""
Company : CodeSoft
_______________________________________
Student : AUBAI ALKHABBAZ
_______________________________________
Program :  ToDoList App using GUI tkinter
_______________________________________
py version : 3.8
_______________________________________
Libraries :  customtkinter (Modern GUI) and tkinter
_______________________________________
the main fucntion of this App to insert tasks and save it in .txt file or load .txt inside this app /
the user can Add - Edit - Delete tasks /
_______________________________________
"""

from  tkinter import filedialog,messagebox,Listbox
import customtkinter  as tk

tk.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
tk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
# init class todolist
class TodolistApp(tk.CTk):

    def __init__(self):
        super().__init__()
        #define geometry of frame
        self.geometry("400x400")
        # define title of frame
        self.title("TO DO LIST")
        # define resizable of frame (fix the size of frame )
        self.resizable(False, False)
        # define main function  of App
        self.create_widgets()

    def create_widgets(self):
        # create object to input tasks  tk.CTkEntry()  -- main frame = self
        self.task_input = tk.CTkEntry(self,width =250)
        # pack() to place it in  main frame
        self.task_input.pack(pady=10)
        # create object button  to add tasks  tk.CTkButton() this button connects to add_task function when you click on it -- main frame = self
        self.add_task_button = tk.CTkButton(self,text="Add Task",command=self.add_task)
        # pack() to place button in  main frame
        self.add_task_button.pack(pady=5)
        # create object Listbox from tkinter to display tasks that we addded it  -- main frame = self
        self.task_listbox = Listbox(self,selectmode=tk.SINGLE,width=50,bg='#ADD8E6',font = "Helvetica")
        # pack() to place listbox in main frame
        self.task_listbox.pack(pady=5)
        # create object frame inside main frame (self)  --- for buttons [save-load-delete-edit]
        self.button_frame=tk.CTkFrame(self)
        # pack() to place the new frame in main frame
        self.button_frame.pack(pady=5)
        # create object button for edit  inside the new frame (self.button_frame)
        self.edit_task_button= tk.CTkButton(self.button_frame,text="Edit Text",command=self.edit_task)
        # pack() to place button in the new frame
        self.edit_task_button.grid(row=0,column=0,padx=5)
        # create object button for delete  inside the new frame (self.button_frame)
        self.delete_task_button = tk.CTkButton(self.button_frame,text="Delete Task",command=self.delete_task)
        # pack() to place button in the new frame
        self.delete_task_button.grid(row=0, column=1, padx=5)
        # create object button for save inside the new frame (self.button_frame)
        self.save_button= tk.CTkButton(self,text='Save',command=self.save_tasks)
        # pack() to place button in the new frame
        self.save_button.pack(pady=5)
        # create object button for load inside the new frame (self.button_frame)
        self.load_button = tk.CTkButton(self,text="Load",command=self.load_tasks)
        # pack() to place button in the new frame
        self.load_button.pack(pady=5)
        #define object button in the new frame
        self.about_button = tk.CTkButton(self,text="About this App ",command=self.about_app)
        # pack() to place button in the new frame
        self.about_button.pack(pady=5)

    #define about_app function
    def about_app(self):
        # Massagebox to show info when you click on about this app button
        messagebox.showinfo('About App','To do list App / created by AUBAI / CODSOFT')

    # define add function for add_task_button
    def add_task(self):
        # get input from CTkEntry and but it inside task
        task = self.task_input.get()
        # check if task is not empty
        if task :
            # insert task from CTKENtry to listbox
            self.task_listbox.insert(tk.END,task)
            # and delete task from CTKENtry  after inserted in listbox
            self.task_input.delete(0,tk.END)


    #define edit fucntion for edit_task_button
    def edit_task(self):
        # input curselection() in listbox when you select text in listbox
        task_index = self.task_listbox.curselection()
        #check if the selection that you chose is not empty
        if task_index :
            #get the new input from CTkEntry to new_task
            new_task = self.task_input.get()
            # check if the new_task is not empty
            if new_task:
                # delete the old task in listbox that you selected
                self.task_listbox.delete(task_index)
                # insert  the new_task in the place of task_index (old task that you selected)
                self.task_listbox.insert(task_index,new_task)
                # delete the input in CTk.Entry
                self.task_input.delete(0,tk.END)

    #define delete function for delete_task_button
    def delete_task(self):
        # input curselection() in listbox when you select text in listbox
        task_index = self.task_listbox.curselection()
        # check if the selection that you chose is not empty
        if task_index:
            # delete the selected task from listbox
            self.task_listbox.delete(task_index)

    # define save function for save_button
    def save_tasks(self):
        # get all task from listbox into tasks variable
        tasks = self.task_listbox.get(0,tk.END)
        # create variable file_path for file .txt , select the defaultextension to txt file
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        # check the file_path
        if file_path:
            # open this file with write mode to write in it
            with open(file_path,"w") as file:
                # for loop to write  all tasks in this txt file  from (tasks variable)
                for task in tasks:
                    #file.write () function towrite into txt and \n for newline
                    file.write(task + "\n")

    # define load function for laod_button
    def load_tasks(self):
        # load the file into file_path variable
        file_path = filedialog.askopenfilename(filetypes=[("Text files","*.txt")])
        #check the file_path
        if file_path :
            # open this file with read mode to read from it
            with open(file_path,'r') as file:
                # for loop into all line of txt and insert them into  tasks variable
                tasks = [line.strip()for line in file.readlines()]
            #delete the old data in listbox
            self.task_listbox.delete(0,tk.END)
            # for loop to insert the tasks variable into listbox
            for task in tasks :
                    self.task_listbox.insert(tk.END,task)

if __name__ == "__main__":
    # start the app
    app = TodolistApp()
    app.mainloop()