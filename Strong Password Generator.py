"""
Company : CodeSoft
_______________________________________
Student : AUBAI ALKHABBAZ
_______________________________________
Program :  Generate Password App using GUI tkinter
_______________________________________
py version : 3.8
_______________________________________
Libraries :  customtkinter (Modern GUI) and tkinter,random,string
_______________________________________
the main fucntion of this App to insert len of password /Generate Password and display it  /save it in .txt file /
_______________________________________
"""

import random
import string
from  tkinter import filedialog,messagebox,Listbox,Text
import customtkinter  as tk
tk.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
tk.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

# init class password for main func
class password:
    def __init__(self, min_length, numbers, special_characters):
        self.min_length = min_length
        self.numbers = numbers
        self.special_characters = special_characters
    # main func for password
    def __generate_password(self):
        letters = string.ascii_letters
        digits = string.digits
        special = string.punctuation
        characters = letters
        # user input y so  self.numbers == True
        if self.numbers :
            # insert digits to password
            characters += digits
        # user input y so  self.special_characters == True
        if self.special_characters:
            # insert special to password
            characters += special
        #define password var
        pwd=""
        # local var
        meets_criteria =False
        has_number = False
        has_special = False
        # while loop  to generate password
        # Break while loop if min_length <  len(pwd)  or meets_criteria == True
        while not meets_criteria or len(pwd) < int(self.min_length) :
            new_char = random.choice(characters)
            pwd += new_char
            # check if the new_char  has at less one or one special character to beak while loop
            if new_char in digits:

                has_number = True
            elif new_char in special:

                has_special =True

            meets_criteria = True

            if self.numbers:
                meets_criteria = has_number
            if self.special_characters:
                meets_criteria = meets_criteria and has_special

        return pwd
# init class generate_password for tkinter
class generate_password(tk.CTk):

    def __init__(self):
        super().__init__()
        #define geometry of frame
        self.geometry("400x450")
        # define title of frame
        self.title("Generate Password")
        # define resizable of frame (fix the size of frame )
        self.resizable(False, False)
        # define main function  of App
        self.create_widgets()
    def create_widgets(self):
        # create object CTkLabel  -- main frame = self
        self.label_password_1 = tk.CTkLabel(self, width=250,text=" Enter the desired password length:  ")
        # pack() to place it in  main frame
        self.label_password_1.pack(pady=5)
        # create object to input password length  tk.CTkEntry()  -- main frame = self
        self.password_input_1 = tk.CTkEntry(self,width =250)
        # pack() to place it in  main frame
        self.password_input_1.pack(pady=5)


        # create object CTkLabel  -- main frame = self
        self.label_password_2 = tk.CTkLabel(self, width=250, text=" Include digits? (yes/no):  ")
        # pack() to place it in  main frame
        self.label_password_2.pack(pady=5)
        # create object to input  has_number  tk.CTkEntry()  -- main frame = self
        self.password_input_2 = tk.CTkEntry(self,width =250)
        # pack() to place it in  main frame
        self.password_input_2.pack(pady=5)


        # create object CTkLabel  -- main frame = self
        self.label_password_3 = tk.CTkLabel(self, width=250, text=" Include symbols? (yes/no): ")
        # pack() to place it in  main frame
        self.label_password_3.pack(pady=5)
        # create object to input  has_speacial  tk.CTkEntry()  -- main frame = self
        self.password_input_3 = tk.CTkEntry(self,width =250)
        # pack() to place it in  main frame
        self.password_input_3.pack(pady=5)


        # create object to display password  Text()  -- main frame = self
        self.Output = Text(self, height=5,width=50, bg="light cyan")
        # pack() to place it in  main frame
        self.Output.pack(pady=10)
# _____________________________________________________________________________________
        # create object frame inside main frame (self)  --- for buttons [save-Generate Password-About]
        self.button_frame=tk.CTkFrame(self)
        # pack() to place the new frame in main frame
        self.button_frame.pack(pady=5)
        # create object button  to Generate Password  tk.CTkButton() this button connects to generate function when you click on it -- self.button_frame
        self.add_task_button = tk.CTkButton(self.button_frame,text="Generate Password",command=self.generate)
        # pack() to place button in  main frame
        self.add_task_button.pack(pady=5)
        # create object button for save inside the new frame (self.button_frame)
        self.save_button= tk.CTkButton(self.button_frame,text='Save',command=self.save_password)
        # pack() to place button in the new frame
        self.save_button.pack(pady=5)
        #define object button in the new frame (self.button_frame)
        self.about_button = tk.CTkButton(self.button_frame,text="About this App ",command=self.about_app)
        # pack() to place button in the new frame
        self.about_button.pack(pady=5)

    def generate(self):
            # get input from CTkEntry
            min_length  = self.password_input_1.get()

            has_number = self.password_input_2.get()
            if has_number =="y":
                has_number=True
            else:
                has_number = False


            has_special = self.password_input_3.get()
            if has_special =="y":
                has_special=True
            else:
                has_special = False


            # check if min_length is not empty
            if min_length :

                gp = password(min_length,has_number,has_special )
                x =gp._password__generate_password()
                self.Output.delete(1.0,tk.END)
                self.Output.insert(tk.END,x)

    # define save function for save_button
    def save_password(self):
        # get password from Text box into password_save variable
        password_save = self.Output.get(1.0,tk.END)
        # create variable file_path for file .txt , select the defaultextension to txt file
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        # check the file_path
        if file_path:
            # open this file with write mode to write in it
            with open(file_path,"w") as file:
                    file.write(str(password_save))

    #define about_app function
    def about_app(self):
        # Massagebox to show info when you click on about this app button
        messagebox.showinfo('About App','Advanced Password Generator / created by AUBAI / CODSOFT')


if __name__ == "__main__":

    app = generate_password()
    app.mainloop()