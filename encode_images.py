import os
from main import find_face_encodings


"""
Encode all images

store in a file

"""
folder_path = 'images'  # Replace with the path to your folder

if os.path.exists(folder_path) and os.path.isdir(folder_path):
    file_list = os.listdir(folder_path)
    
    for filename in file_list:
        image_encoding = find_face_encodings(f'images/{filename}')
        
