import tkinter as tk
import cv2 as cv
from PIL import ImageTk, Image
import shutil
import os
from tkinter import Label, messagebox
from tkinter import filedialog
import numpy as np
from tensorflow import keras
from tensorflow.keras.preprocessing import image


from predection import load_and_display_image, predict_image_class
IMAGE_SIZE = 224  # Set the desired image size


class HomePage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Camera Object Classifier")
        self.master.geometry("800x800")
         # Resize the logo image
        logo_image = Image.open("logo.png")
        resized_logo = logo_image.resize((32, 32))  # Adjust the size as needed

        # Save the resized image as a temporary file
        resized_logo_path = "resized_logo.ico"  # Provide a path for the resized image
        resized_logo.save(resized_logo_path, format="ICO") 
        # Set the resized image as the window icon
        master.iconbitmap(resized_logo_path)
        
        # Create the heading label
        heading_label = Label(master, text='PICK YOUR OBJECT PICTURE  ', font=('arial', 16, 'bold'), fg='royalblue')
        heading_label.pack(pady=10)
        self.camera = Camera()  # Create an instance of the Camera class
        self.current_image = None
        self.create_widgets()

    def create_widgets(self):
        # Top Frame
        self.top_frame = tk.Frame(self.master, bg="#f0f0f0")
        self.top_frame.pack(fill=tk.BOTH, expand=True)
   
        self.canvas = tk.Canvas(self.top_frame, width=640, height=480, bg="#B0C4DE")
        self.canvas.pack(pady=20)

        # Bottom Frame
        self.bottom_frame = tk.Frame(self.master, bg="#f0f0f0")
        self.bottom_frame.pack(pady=20)
        self.btn_capture = tk.Button(self.bottom_frame, text="Take Picture", command=self.capture_picture, width=15,
                                     bg="#B0C4DE", fg="black", font=("Arial", 12, "bold"))
        self.btn_capture.pack(side=tk.LEFT, padx=10)
        self.btn_import = tk.Button(self.bottom_frame, text="Import Picture", command=self.import_picture, width=15,
                                    bg="#B0C4DE", fg="black", font=("Arial", 12, "bold"))
        self.btn_import.pack(side=tk.LEFT, padx=10)
        self.btn_save = tk.Button(self.bottom_frame, text="Save Picture", command=self.save_picture,
                                  state=tk.DISABLED, width=15, bg="#B0C4DE", fg="red", font=("Arial", 12, "bold"))
        self.btn_save.pack(side=tk.LEFT, padx=10)
        self.btn_analyse = tk.Button(self.bottom_frame, text="Analyse", command=self.analyse_image,
                                     state=tk.DISABLED, width=15, bg="green", fg="white", font=("Arial", 12, "bold"))
        self.btn_analyse.pack(side=tk.LEFT, padx=10)

    def capture_picture(self):
        frame = self.camera.get_frame()
        if frame is not None:
            self.current_image = ImageTk.PhotoImage(Image.fromarray(frame))
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.current_image)
            self.btn_save.config(state=tk.NORMAL)
            self.btn_analyse.config(state=tk.NORMAL)
        else:
            self.show_message("Failed to capture image!")

    def display_image(self, file_path):
        image = Image.open(file_path)
        self.current_image = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.current_image)

    def import_picture(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        if file_path:
            self.imported_image_path = file_path
            self.display_image(file_path)
            self.btn_save.config(state=tk.NORMAL)
            self.btn_analyse.config(state=tk.NORMAL)

    def save_picture(self):
        if self.current_image is not None:
            image = ImageTk.getimage(self.current_image)
            image = image.convert("RGB")  # Convert image to RGB mode
            img_path = r'C:\Users\hp\Desktop\Machine learning project\IMAGE\ThisImage.jpg'  # Set the desired save path here
            image.save(img_path)
            self.show_message("Image saved successfully!")
            self.btn_analyse.config(state=tk.NORMAL)
            load_and_display_image(img_path, IMAGE_SIZE)
            return img_path
        
    def analyse_image(self):
        img_path = self.save_picture()

        if img_path is not None:
           predicted_class = predict_image_class(img_path)

           analyze_window = tk.Toplevel(self.master)
           analyzed_image_label = tk.Label(analyze_window, image=self.current_image)
           analyzed_image_label.pack()

           predicted_class_label = tk.Label(analyze_window, text="The object is: {}".format(predicted_class))
           predicted_class_label.pack()

    
    def analyse(self):

        return "Image analysis results"

    def show_message(self, message):
        messagebox.showinfo("Message", message)

    def exit_application(self):
        self.master.destroy()


class Camera:
    def __init__(self):
        self.camera = cv.VideoCapture(0)
        if not self.camera.isOpened():
            raise ValueError("Unable to open camera!")

    def __del__(self):
        if self.camera.isOpened():
            self.camera.release()

    def get_frame(self):
        if self.camera.isOpened():
            ret, frame = self.camera.read()

            if ret:
                return np.array(frame, dtype=np.uint8)
        else:
            return None

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg="#f0f0f0")
    app = HomePage(root)
    app.pack(fill=tk.BOTH, expand=True)

    root.mainloop()