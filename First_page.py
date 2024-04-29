from tkinter import *
from PIL import Image, ImageTk

class FirstPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Welcome Page")
        # Create a Tkinter window
      
        root.geometry("500x700")
        root.title('Login Page ')
        self.root.configure(bg="#B0C4DE")
        # Resize the logo image
        logo_image = Image.open("logo.png")
        resized_logo = logo_image.resize((32, 32))  # Adjust the size as needed

        # Save the resized image as a temporary file
        resized_logo_path = "resized_logo.ico"  # Provide a path for the resized image
        resized_logo.save(resized_logo_path, format="ICO")

          # Set the resized image as the window icon
        root.iconbitmap(resized_logo_path)
        
        self.create_widgets()
    
    def remove_background(self, image_path):
        # Open the image
        image = Image.open(image_path)
        
        # Convert the image to RGBA mode
        image = image.convert("RGBA")
        
        # Get the pixel data of the image
        pixel_data = image.getdata()
        
        # Create a new image with transparent background
        new_image_data = []
        
        for item in pixel_data:
            # Set the pixel to transparent if it matches the background color
            if item[:3] == (0, 0, 0):
                new_image_data.append((0, 0, 0, 0))
            else:
                new_image_data.append(item)
        
        # Update the image data
        image.putdata(new_image_data)
        
        return image
    
    def signup_button_clicked(self):
        import signup  
        pass
    
    def login_button_clicked(self):
        import LOGIN
        pass

    def create_widgets(self):

        # Create a canvas to place the logo
        canvas = Canvas(self.root, bg="#B0C4DE", highlightthickness=0)
        canvas.pack()

        # Create a frame for the logo
        logo_frame = Frame(self.root, bg="#B0C4DE")
        logo_frame.pack(fill=X)

            # Load the logo image
        logo_image = Image.open("logo.png")
        logo_image = logo_image.resize((200, 200))  # Adjust the size as needed

         # Convert the logo image to Tkinter-compatible format
        logo_photo = ImageTk.PhotoImage(logo_image)

        # Create a label to display the logo
        logo_label = Label(logo_frame, image=logo_photo, bg="#B0C4DE")
        logo_label.image = logo_photo  # Keep a reference to the image
        logo_label.pack(padx=10, pady=10)  # Adjust the padding as needed


        # Create a label under the logo image
        label_under_logo = Label(logo_frame, text="GUESS THE OBJECT",fg="darkcyan", font=("Pale", 12, "bold"), bg="#B0C4DE")
        label_under_logo.pack(pady=(0, 10))  # Adjust the padding as needed

        # Create a login button
        login_button = Button(self.root, text="Login", command=self.login_button_clicked, width=17, height=1)
        login_button.configure(font=("Helvetica", 12, "bold"), fg="white", bg="royalblue")  
        login_button.pack(pady=(0, 10))  # Adjust the pady to remove the space
        
        # Create a signup button
        signup_button = Button(self.root, text="Sign Up", command=self.signup_button_clicked, width=17, height=1)
        signup_button.configure(font=("Helvetica", 12, "bold"), fg="white", bg="royalblue")  
        signup_button.pack(pady=(0, 20))  # Adjust the pady to remove the space
        
        # Create a label for the signature
        signature_label = Label(self.root, text="© 2024 MeryMRabaB. All rights reserved.", font=("Helvetica", 8), bg="#B0C4DE")
        signature_label.pack(side="bottom", pady=10)



if __name__ == "__main__":
    root = Tk()
    app = FirstPage(root)
    root.mainloop()