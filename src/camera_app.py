import cv2
import tkinter as tk
from PIL import Image, ImageTk

class CameraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Camera App")

        self.camera = cv2.VideoCapture(0)

        self.label = tk.Label(root)
        self.label.pack(pady=10)

        self.capture_button = tk.Button(root, text="Capture", command=self.capture_image)
        self.capture_button.pack(pady=5)

        self.update()

    def capture_image(self):
        ret, frame = self.camera.read()
        if ret:
            cv2.imwrite("captured_image.jpg", frame)
            print("Image captured.")

    def update(self):
        ret, frame = self.camera.read()
        if ret:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame_rgb)
            imgtk = ImageTk.PhotoImage(image=img)
            self.label.imgtk = imgtk
            self.label.configure(image=imgtk)

        self.root.after(10, self.update)

if __name__ == "__main__":
    root = tk.Tk()
    app = CameraApp(root)
    root.mainloop()
