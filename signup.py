from tkinter import *
from tkinter import messagebox
import pymysql
from PIL import Image, ImageTk

class RegistrationWindow:
    def __init__(self, window):
        self.window = window
        self.window.title("Sign Up")
        self.window.geometry("400x400")
        # Resize the logo image
        logo_image = Image.open("logo.png")
        resized_logo = logo_image.resize((32, 32))  # Adjust the size as needed

         # Save the resized image as a temporary file
        resized_logo_path = "resized_logo.ico"  # Provide a path for the resized image
        resized_logo.save(resized_logo_path, format="ICO")

            # Set the resized image as the window icon
        window.iconbitmap(resized_logo_path)

         # Create the heading label
        heading_label = Label(window, text='Sign Up ', font=('arial', 16, 'bold'), fg='royalblue')
        heading_label.pack(pady=10)

        
        self.label_email = Label(self.window, text="E-mail", font=("Arial", 10, "bold"))
        self.label_email.pack(pady=10)
        
        self.emailEntry = Entry(self.window, width=30)
        self.emailEntry.pack()
        
        self.label_username = Label(self.window, text="Username:", font=("Arial", 10, "bold"))
        self.label_username.pack(pady=10)
        
        self.usernameEntry = Entry(self.window, width=30)
        self.usernameEntry.pack()
        
        self.label_password = Label(self.window, text="Password:", font=("Arial", 10, "bold"))
        self.label_password.pack(pady=10)
        
        self.passwordEntry = Entry(self.window, show="*", width=30)
        self.passwordEntry.pack()
        
        self.label_confirm = Label(self.window, text="Confirm Password", font=("Arial", 10, "bold"))
        self.label_confirm.pack(pady=10)
        
        self.ConfirmePasswordEntry = Entry(self.window, show="*", width=30)
        self.ConfirmePasswordEntry.pack()
        
        self.check = IntVar()
        self.agreeCheckbutton = Checkbutton(self.window, text="I agree to the terms", variable=self.check, font=("Arial", 8, "bold"))
        self.agreeCheckbutton.pack(pady=10)
        
        self.connectButton = Button(self.window, text="Sign up", command=self.connect_database, bg="cornflowerblue", width=20, height=1, fg="white", font=("Arial", 9, "bold"))
        self.connectButton.pack(pady=10)
        
        # Center the window on the screen
        self.center_window()
    
    def center_window(self):
        self.window.update_idletasks()
        window_width = self.window.winfo_width()
        window_height = self.window.winfo_height()
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x_coordinate = int((screen_width / 2) - (window_width / 2))
        y_coordinate = int((screen_height / 2) - (window_height / 2))
        self.window.geometry(f"+{x_coordinate}+{y_coordinate}")
    
    def clear(self):
        self.emailEntry.delete(0, END)
        self.usernameEntry.delete(0, END)
        self.passwordEntry.delete(0, END)
        self.ConfirmePasswordEntry.delete(0, END)
        self.check.set(0)
    
    def connect_database(self):
        if self.emailEntry.get() == '' or self.usernameEntry.get() == '' or self.passwordEntry.get() == '' or self.ConfirmePasswordEntry.get() == '':
            messagebox.showerror('Error', 'All Fields Are Required')
        elif self.passwordEntry.get() != self.ConfirmePasswordEntry.get():
            messagebox.showerror('Error', 'Password Mismatch')
        elif self.check.get() == 0:
            messagebox.showerror('Error', 'Please accept terms and conditions')
        else:
            try:
                con = pymysql.connect(host='localhost', user='root', password='')
                mycursor = con.cursor()
            except:
                messagebox.showerror('Error', 'Please Try again')
                return

            try:
                query = 'create database project_Camera'
                mycursor.execute(query)
                query = 'use project_Camera'
                mycursor.execute(query)
                query = 'create table userdata(id int auto_increment primary key not null , email varchar(20) , username varchar(50) ,password varchar(20))'
                mycursor.execute(query)
            except:
                mycursor.execute('use project_Camera')
                query = 'select * from userdata where username= %s'
                mycursor.execute(query, (self.usernameEntry.get()))
                row = mycursor.fetchone()

                if row is not None:
                    messagebox.showerror('Error', 'Username already Exist')
                    return

            query = 'insert into userdata(email,username ,password) values(%s,%s,%s)'
            mycursor.execute(query, (self.emailEntry.get(), self.usernameEntry.get(), self.passwordEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success', 'Registration is successful')
            self.clear()
            self.window.destroy()
            import LOGIN


# Create a Tkinter window
window = Tk()
registration_window = RegistrationWindow(window)

# Start the Tkinter event loop
window.mainloop()