# importing whole module
from tkinter import *
from tkinter import ttk
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


####################### MAIN ##############################
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
                panel2.config(image=photo)
                panel2.image = photo  # Keep a reference to prevent garbage collection
                message.config(text='Image Found')
                break
            else:
                message.config(text="Image not found")
                # label2.image = photo  # Keep a reference to prevent garbage collection
                print(f"The current image not same name: {row[1]}")


##################### END MAIN ############################
def run_search():
    main(file_path)

def open_image():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif *.bmp *.ppm *.pgm")])
    panel1.config(image=placeholder) 
    panel2.config(image=placeholder) 
    # print('THE FILE PATH IS ',file_path)
    if file_path:
        # Open and display the selected image
        image = Image.open(file_path)
        photo = ImageTk.PhotoImage(image)
        panel1.config(image=photo)
        panel1.image = photo  # Keep a reference to prevent garbage collection

root = Tk()
root.geometry('600x500')

header = Label(root, text ='Face Recognition', font=('calibri', 40, 'bold'), ) 
header.pack()

message = Label(root, text='', font=('calibri', 20, 'bold'), fg ="red" )
message.pack()

#### IMAGE SIDE BY SIDE ################
frame = ttk.Frame(root, padding=10)
frame.pack()

placeholder = ImageTk.PhotoImage(Image.open("C:/Users/60004821/Desktop/python/face_recognition/assests/placeholder.png"))

panel1 = Label(frame, image=placeholder, padx=10, pady=10)
panel2 = Label(frame, image=placeholder, padx=10, pady=10)
# setting the application
panel1.grid(row=0, column=0, sticky="nsew", padx=3, pady=3)
panel2.grid(row=0, column=1, sticky="nsew",padx=3, pady=3)

# Configure grid column weights to make labels take 50% each
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)

# Configure grid row weight to allow labels to expand vertically
frame.rowconfigure(0, weight=1)

#### END IMAGE SIDE BY SIDE ################

#### Button SIDE BY SIDE ################
frame2 = ttk.Frame(root, padding=10)
frame2.pack(side='left', expand=True, fill=BOTH)

btn1 = Button(frame2, text="Select Image", bd = '5', padx=10, pady=10,  command=open_image)
btn2 = Button(frame2, text="Search Image Database", bd = '5', padx=10, pady=10, command=run_search)
# setting the application
btn1.grid(row=1, column=0, sticky="nsew", padx=3, pady=3, )
btn2.grid(row=1, column=1, sticky="nsew",padx=3, pady=3)

# Configure grid column weights to make labels take 50% each
frame2.columnconfigure(0, weight=1)
frame2.columnconfigure(1, weight=1)

# Configure grid row weight to allow labels to expand vertically
frame2.rowconfigure(0, weight=1)

#### END Button SIDE BY SIDE ################


root.mainloop()