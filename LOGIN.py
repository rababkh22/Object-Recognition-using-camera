from tkinter import *
from tkinter import messagebox
import pymysql
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def login_user():
    if username_entry.get() == '' or password_entry.get() == '':
        messagebox.showerror('Error', 'All Fields Are Required')
    else:
        try:
          con=pymysql.connect(host='localhost',user='root',password='')   
          mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Connection is not established try again ')
            return
    query='use project_Camera'
    mycursor.execute(query)
    query='select * from userdata where username= %s and password =%s'
    mycursor.execute(query,(username_entry.get(),password_entry.get()))
    row=mycursor.fetchone()
    if row == None:
        messagebox.showerror('Error','Invalid username or password')
    else:
        messagebox.showinfo('welcome','login is sucessful ')
    import Home
        
    

def forgot_password():
    
    def change_password():
        if entry_username.get()=='' or entry_newpassword.get()=='' or entry_Conpassword.get()=='':
            messagebox.showerror('Error','All Fields Are Required',parent=window)
        elif entry_newpassword.get() != entry_Conpassword.get() :
             messagebox.showerror('Error', 'Password and confirm password are not matching ',parent=window)
        else:
           con=pymysql.connect(host='localhost',user='root',password='',database='project_Camera')   
           mycursor=con.cursor()
           query='select * from userdata where username= %s' 
           mycursor.execute(query,(username_entry.get()))
           row=mycursor.fetchone()

           if row== None:
                messagebox.showerror('Error','Incorrect Username')

           else:
               query='update userdata set password =%s where username=%s'
               mycursor.execute(query,(entry_newpassword.get(),username_entry.get()))
               con.commit()
               con.close()
               messagebox.showinfo('Success','Password is reset , Please login with new password',parent=window)
               window.destroy()
   
    # Create a Tkinter window
    window = Tk()
    window.geometry("400x400")
    window.title('Forget The Password')
    # Resize the logo image
    logo_image = Image.open("logo.png")
    resized_logo = logo_image.resize((32, 32))  # Adjust the size as needed

     # Save the resized image as a temporary file
    resized_logo_path = "resized_logo.ico"  # Provide a path for the resized image
    resized_logo.save(resized_logo_path, format="ICO")

     # Set the resized image as the window icon
    window.iconbitmap(resized_logo_path)
    # Load the background image


    # Center the window on the screen
    window.update_idletasks()
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_coordinate = int((screen_width / 2) - (window_width / 2))
    y_coordinate = int((screen_height / 2) - (window_height / 2))
    window.geometry(f"+{x_coordinate}+{y_coordinate}")

    # Create the heading label
    heading_label = Label(window, text='Reset Password', font=('arial', 16, 'bold'), fg='royalblue')
    heading_label.pack(pady=20)

    # Create the username label and entry
    label_username = Label(window, text="Username", font=("Arial", 10, "bold"))
    label_username.pack()
    entry_username = Entry(window, width=30)
    entry_username.pack()

    # Create the new password label and entry
    label_newpassword = Label(window, text="New password", font=("Arial", 10, "bold"))
    label_newpassword.pack()
    entry_newpassword = Entry(window, width=30)
    entry_newpassword.pack()

    # Create the confirm password label and entry
    label_Conpassword = Label(window, text="Confirm password", font=("Arial", 10, "bold"))
    label_Conpassword.pack()
    entry_Conpassword = Entry(window, width=30)
    entry_Conpassword.pack()

    # Create the reset password button
    button_Submit = Button(window, text="Submit", command=change_password, bg="cornflowerblue", width=20, height=1, fg="white", font=("Arial", 9, "bold"))
    button_Submit.pack(pady=20)

    # Start the Tkinter event loop
    window.mainloop()
    
def create_account():
    # Add your logic to navigate to the sign-up page here
    print("Create Account button clicked")
    import signup



def clear_password_placeholder(event):
    if password_entry.get() == "Enter your password":
        password_entry.delete(0, "end")



def clear_username_placeholder(event):
    if username_entry.get() == "Enter your username":
        username_entry.delete(0, "end")


# Create a Tkinter window
window = Tk()
window.geometry("400x400")
window.title('Login Page ')
# Resize the logo image
logo_image = Image.open("logo.png")
resized_logo = logo_image.resize((32, 32))  # Adjust the size as needed

# Save the resized image as a temporary file
resized_logo_path = "resized_logo.ico"  # Provide a path for the resized image
resized_logo.save(resized_logo_path, format="ICO")

# Set the resized image as the window icon
window.iconbitmap(resized_logo_path)


 # Create the heading label
heading_label = Label(window, text='Login Page', font=('arial', 18, 'bold'), fg='royalblue')
heading_label.pack(pady=10)

# Username Entry
username_entry = Entry(window, width=30)
username_entry.insert(0, "Enter your username")  # Placeholder text for username
username_entry.bind("<FocusIn>", clear_username_placeholder)
username_entry.pack(pady=30)

# Password Entry
password_entry = Entry(window, show="*", width=30)
password_entry.insert(0, "Enter your password")  # Placeholder text for password
password_entry.bind("<FocusIn>", clear_password_placeholder)
password_entry.pack(pady=5)

# Login Button
login_button = Button(window, text="Login", bg="cornflowerblue", command=login_user, width=20, height=1, fg="white", font=("Arial", 9, "bold"))
login_button.pack(pady=15)

# Forgot Password Button
forgot_password_button = Button(window, bg="cornflowerblue",text="Forgot Password", command=forgot_password, width=20, height=1, fg="white", font=("Arial", 9, "bold"))
forgot_password_button.pack(pady=10)



# Center the window on the screen
window.eval('tk::PlaceWindow . center')

window.mainloop()