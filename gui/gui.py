from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image


import sqlite3
import numpy as np
import face_recognition


conn = sqlite3.connect('image.db')
cursor = conn.cursor()

# Retrieve all encodings from the 'encodings' table
cursor.execute('SELECT image_encoding, name, image_path FROM face_recognition_images')
all_encodings_data = cursor.fetchall()

def find_face_encodings(image_path):
    # load image
    image = face_recognition.load_image_file(image_path)
    # get face encodings from the image
    face_enc = face_recognition.face_encodings(image)
    # return face encodings
    return face_enc[0]


def main(file_path):
    uploaded_image  = find_face_encodings(file_path)

    for row in all_encodings_data:
        image_encoding_bytes = row[0]

        # Convert the bytes object to a NumPy array
        encoded_data = np.frombuffer(image_encoding_bytes, dtype=np.float64)

        # Perform your comparison logic here
        if encoded_data is not None:
            is_same = face_recognition.compare_faces([uploaded_image], encoded_data)[0]
            
            if is_same:
                # finding the distance level between images
                distance = face_recognition.face_distance([uploaded_image], encoded_data)
                distance = round(distance[0] * 100)
                
                # calcuating accuracy level between images
                accuracy = 100 - round(distance)
                print(f"The current image is the same as {row[1]}")
                print(f"Accuracy Level: {accuracy}%")

                file_path = f'C:/Users/60004821/Desktop/python/face_recognition/{row[2]}'
                image = Image.open(file_path)
                photo = ImageTk.PhotoImage(image)
                label2.config(image=photo)
                label2.image = photo  # Keep a reference to prevent garbage collection
                label3.config(text='Image Found')
                break
            else:
                label3.config(text="Image not found")
                # label2.image = photo  # Keep a reference to prevent garbage collection
                print(f"The current image not same name: {row[1]}")









def open_image():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif *.bmp *.ppm *.pgm")])
    # print('THE FILE PATH IS ',file_path)
    if file_path:
        # Open and display the selected image
        image = Image.open(file_path)
        photo = ImageTk.PhotoImage(image)
        label2.config(image=photo)
        label2.image = photo  # Keep a reference to prevent garbage collection


def display_found_image(file_path):    
    if file_path:
        # Open and display the selected image
        image = Image.open(file_path)
        photo = ImageTk.PhotoImage(image)
        # Create a label to display the selected image
        
        label2.config()
        label.config(image=photo)
        label.image = photo  # Keep a reference to prevent garbage collection

root = Tk()
root.title('Face Recognition GUI')
root.geometry('500x400')

# Create a button to open the image dialog
open_button = Button(root, text="Select Image", command=open_image)
open_button.grid(row=1, column=0)


def run_search():
    main(file_path)

open_button = Button(root, text="Search Image Database", command=run_search)
open_button.grid(row=2, column=0)

# Create a label to display the selected image
label = Label(root)
label.grid(row=0, column=0)

# Create a label to display the selected image
label2 = Label(root)
label2.grid(row=0, column=2)

label3 = Label(root)
label3.grid(row=4, column=2)

root.mainloop()