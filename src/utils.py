import face_recognition
import numpy as np
from tkinter import filedialog
from PIL import ImageTk, Image


def find_face_encodings(image_path):
    # load image
    image = face_recognition.load_image_file(image_path)
    # get face encodings from the image
    face_enc = face_recognition.face_encodings(image)
    # return face encodings
    return face_enc[0]

def take_photo():
    print('Photo taken')
    
def open_image(panel):
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif *.bmp *.ppm *.pgm")])
    # print('THE FILE PATH IS ',file_path)
    if file_path:
        # Open and display the selected image
        image = Image.open(file_path)
        photo = ImageTk.PhotoImage(image)
        panel.config(image=photo)
        panel.image = photo  # Keep a reference to prevent garbage collection

def compare_upload_face_db(panel, message, db_data):
    global file_path
    uploaded_image  = find_face_encodings(file_path)

    for row in db_data:
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
                panel.config(image=photo)
                panel.image = photo  # Keep a reference to prevent garbage collection
                message.config(text=f'Image Found {accuracy}%')
                return photo
            else:
                message.config(text="Image not found")
                print(f"The current image not same name: {row[1]}")