import face_recognition
import sqlite3


# Connect to the SQLite database
conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()

# Retrieve all encodings from the 'encodings' table
cursor.execute('SELECT encoding_data FROM encodings')
all_encodings_data = cursor.fetchall()

# Simulate a single face encoding for comparison (replace with your actual encoding)
single_encoding = face_recognition.face_encodings(single_face_image)[0]  # Replace with your actual image

# Iterate through all encodings and compare with the single encoding
for row in all_encodings_data:
    database_encoding_data = row[0]
    database_encoding = face_recognition.api.face_encoding_from_raw_image(database_encoding_data)

    # Perform your comparison logic here
    if database_encoding is not None:
        match = face_recognition.compare_faces([single_encoding], database_encoding[0])
        if match[0]:
            print("Matching encoding found")

# Close the database connection
conn.close()



# import sqlite3

# con = sqlite3.connect('image.db')
# cur = con.cursor()

# cur.execute("""
#     INSERT INTO face_recognition_images VALUES
#         ('Obama', 'file/images', '[2, 3, [2,3]]')
# """)
# con.commit()



# con.close()




