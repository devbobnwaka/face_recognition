import sqlite3
import numpy as np
import face_recognition


conn = sqlite3.connect('image.db')
cursor = conn.cursor()

# Retrieve all encodings from the 'encodings' table
cursor.execute('SELECT image_encoding, name FROM face_recognition_images')
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
            else:
                print(f"The current image not same name: {row[1]}")

# if __name__ == "__main__":
#     main()







# def main():
#     try:
#         # getting face encodings for first image
#         image_1 = find_face_encodings("images/gerrad1.jpg")
#         # getting face encodings for second image
#         image_2  = find_face_encodings("images/gerrad2.jpg")

#         # checking both images are same
#         is_same = face_recognition.compare_faces([image_1], image_2)[0]
#         print(f"Is Same: {is_same}")
#     except Exception as e:
#         print(e)

#     if is_same:
#         # finding the distance level between images
#         distance = face_recognition.face_distance([image_1], image_2)
#         distance = round(distance[0] * 100)
        
#         # calcuating accuracy level between images
#         accuracy = 100 - round(distance)
#         print("The images are same")
#         print(f"Accuracy Level: {accuracy}%")
#     else:
#         print("The images are not same")



