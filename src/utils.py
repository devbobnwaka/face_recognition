import face_recognition
import numpy as np
from tkinter import filedialog
from PIL import ImageTk, Image


import cv2
import time
import os
# from PIL import ImageTk, Image

def resize_image(image, max_width, max_height):
    width, height = image.size
    aspect_ratio = min(max_width / width, max_height / height)
    new_width = int(width * aspect_ratio)
    new_height = int(height * aspect_ratio)
    return image.resize((new_width, new_height), Image.Resampling.LANCZOS)

def capture_image(panel, panel2):
    # global file_path
    camera = cv2.VideoCapture(0)
    while(True):
        ret, frame = camera.read()

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == 13:
            if ret:
                relative_file_path = f"uploads/captured_image__{time.time()}.jpg"
                res = cv2.imwrite(relative_file_path, frame)
                print("Image captured.")
                global file_path

                file_path = relative_file_path
                print("2", file_path)
                 # Open and display the selected image
                original_image = Image.open(file_path)
                resized_image = resize_image(original_image, 300, 300)
                photo = ImageTk.PhotoImage(resized_image)
                panel.config(image=photo)
                panel.image = photo  # Keep a reference to prevent garbage collection

                current_dir = os.getcwd()
                absolute_placeholder_path = os.path.join(current_dir, "assests/placeholder.png").replace("\\", "/")
                placeholder_image = ImageTk.PhotoImage(Image.open(absolute_placeholder_path))
                panel2.config(image=placeholder_image)
                panel2.image = placeholder_image
            break
  
    # After the loop release the cap object
    camera.release()
    # Destroy all the windows
    cv2.destroyAllWindows()



def find_face_encodings(image_path):
    # load image
    image = face_recognition.load_image_file(image_path)
    # get face encodings from the image
    face_enc = face_recognition.face_encodings(image)
    # return face encodings
    print(face_enc)
    return face_enc[0]

# find_face_encodings('C:\\Users\\60004821\\Desktop\\python\\face_recognition\\images\\lawrence2.jpg')
    
def open_image(panel1, panel2):
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif *.bmp *.ppm *.pgm")])
    # print('THE FILE PATH IS ',file_path)
    if file_path:
        # Open and display the selected image
        original_image = Image.open(file_path)
        resized_image = resize_image(original_image, 300, 300)
        photo = ImageTk.PhotoImage(resized_image)
        panel1.config(image=photo)

        current_dir = os.getcwd()
        absolute_placeholder_path = os.path.join(current_dir, "assests/placeholder.png").replace("\\", "/")
        placeholder_image = ImageTk.PhotoImage(Image.open(absolute_placeholder_path))
        panel2.config(image=placeholder_image)

        panel1.image = photo  # Keep a reference to prevent garbage collection
        panel2.image = placeholder_image  # Keep a reference to prevent garbage collection

def compare_upload_face_db(panel, message, db_data):
    global file_path
    print("3: ", file_path)
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

                # file_path = f'C:/Users/60004821/Desktop/python/face_recognition/{row[2]}'
                file_path = f"{row[2]}"

                original_image = Image.open(file_path)
                resized_image = resize_image(original_image, 300, 300)
                photo = ImageTk.PhotoImage(resized_image)
                panel.config(image=photo)
                panel.image = photo  # Keep a reference to prevent garbage collection
                message.config(text=f'Image Found {accuracy}%')
                return photo
            else:
                message.config(text="Image not found")
                print(f"The current image not same name: {row[1]}")