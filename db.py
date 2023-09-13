import sqlite3

con = sqlite3.connect('image.db')
cur = con.cursor()

cur.execute("""
    INSERT INTO face_recognition_images VALUES
        ('Obama', 'file/images', '[2, 3, [2,3]]')
""")
con.commit()



con.close()




