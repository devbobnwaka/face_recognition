import os
from main import find_face_encodings

# getting face encodings for first image
image_1 = find_face_encodings("images/gerrad1.jpg")

print(image_1)