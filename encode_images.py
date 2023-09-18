import os
import sqlite3
import numpy as np
# from main import find_face_encodings

from src.utils import find_face_encodings
"""
Encode all images

store in a file

"""
con = sqlite3.connect('image.db')
folder_path = 'images'  # Replace with the path to your folder
data = []
if os.path.exists(folder_path) and os.path.isdir(folder_path):
    file_list = os.listdir(folder_path)
    for index, filename in enumerate(file_list):
        image_encoding = find_face_encodings(f'images/{filename}')
        data.append((index, filename, f'images/{filename}', image_encoding))
        # print(type(index))
    # print(data)
    
    cur = con.cursor()
    cur.executemany("INSERT INTO face_recognition_images VALUES(?, ?, ?, ?)", data)
    con.commit()  # Remember to commit the transaction after executing INSERT.

    con.close()


     
