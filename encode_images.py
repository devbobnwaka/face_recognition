import os
import numpy as np
from main import find_face_encodings


"""
Encode all images

store in a file

"""
folder_path = 'images'  # Replace with the path to your folder

if os.path.exists(folder_path) and os.path.isdir(folder_path):
    file_list = os.listdir(folder_path)
    image_encodings_arr = np.array([])
    for filename in file_list:
        image_encoding = find_face_encodings(f'images/{filename}')
        image_encodings_arr = np.append(image_encodings_arr, image_encoding)

    np.savetxt('my_array.csv', image_encodings_arr, delimiter=',')
        # using with statement
        # with open('encoded_images.txt', 'a') as file:
        #     file.write(image_encoding)   
        # 
        # Save the ndarray to a CSV file
     
