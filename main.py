from src.db_config import DatabaseConfig
from src.gui import run_gui
from src.utils import (
    open_image,
    compare_upload_face_db
    )


def main():
    db = DatabaseConfig('image.db')
    cursor = db.connect_db()
    sql_statement = 'SELECT image_encoding, name, image_path FROM face_recognition_images'
    db_data = db.retrieve_data(cursor, sql_statement)

    run_gui(open_image, compare_upload_face_db, db_data)



if __name__ == "__main__":
    main()