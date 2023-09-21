import cv2
import time
from .utils import compare_upload_face_db


camera = cv2.VideoCapture(0)

def capture_image(panel, message, db_data):
    while(True):
        ret, frame = camera.read()

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == 13:
            if ret:
                relative_file_path = f"uploads/captured_image__{time.time()}.jpg"
                res = cv2.imwrite(relative_file_path, frame)
                print("Image captured.")
                if res:
                    return relative_file_path
            break
  
    # After the loop release the cap object
    camera.release()
    # Destroy all the windows
    cv2.destroyAllWindows()



# while(True):
#     ret, frame = camera.read()

#     cv2.imshow('frame', frame)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     if ret:
    #         cv2.imwrite("captured_image.jpg", frame)
    #         print("Image captured.")
    #     break
#     if cv2.waitKey(1) & 0xFF == 13:
#         if ret:
#             cv2.imwrite("captured_image.jpg", frame)
#             print("Image captured.")
#         break
  
# # After the loop release the cap object
# camera.release()
# # Destroy all the windows
# cv2.destroyAllWindows()
