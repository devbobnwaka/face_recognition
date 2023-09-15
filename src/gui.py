from tkinter import *
from tkinter import filedialog, ttk
from PIL import ImageTk, Image

def run_gui(open_image, run_search, take_photo, db_data):
    root = Tk()
    root.geometry('600x500')

    header = Label(root, text ='Face Recognition', font=('calibri', 40, 'bold'), ) 
    header.pack()

    message = Label(root, text='', font=('calibri', 20, 'bold'), fg ="red" )
    message.pack()

    #### IMAGE SIDE BY SIDE ################
    frame = ttk.Frame(root, padding=10)
    frame.pack()

    placeholder = ImageTk.PhotoImage(Image.open("C:/Users/60004821/Desktop/python/face_recognition/assests/placeholder.png"))

    panel1 = Label(frame, image=placeholder, padx=10, pady=10)
    panel2 = Label(frame, image=placeholder, padx=10, pady=10)
    # setting the application
    panel1.grid(row=0, column=0, sticky="nsew", padx=3, pady=3)
    panel2.grid(row=0, column=1, sticky="nsew",padx=3, pady=3)

    # Configure grid column weights to make labels take 50% each
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)

    # Configure grid row weight to allow labels to expand vertically
    frame.rowconfigure(0, weight=1)

    #### END IMAGE SIDE BY SIDE ################

    #### Button SIDE BY SIDE ################
    frame2 = ttk.Frame(root, padding=10)
    # frame2.pack()
    frame2.pack(expand=True, fill=BOTH)

    btn1 = Button(frame2, text="Select Image", bd = '5', padx=10, pady=10,  command=lambda:open_image(panel1))
    btn2 = Button(frame2, text="Search Image Database", bd = '5', padx=10, pady=10, command=lambda:run_search(panel2, message, db_data))
    # setting the application
    btn1.grid(row=1, column=0, sticky="nsew", padx=3, pady=3, )
    btn2.grid(row=1, column=1, sticky="nsew",padx=3, pady=3)

    # Configure grid column weights to make labels take 50% each
    frame2.columnconfigure(0, weight=1)
    frame2.columnconfigure(1, weight=1)

    # Configure grid row weight to allow labels to expand vertically
    frame2.rowconfigure(0, weight=1)

    #### END Button SIDE BY SIDE ################
    frame3 = ttk.Frame(root, padding=10)
    frame3.pack(side='bottom', expand=True, fill=BOTH)
    take_photo = Button(frame3, text="Take Photo", bd = '5', padx=10, pady=10, command=take_photo)
    take_photo.pack()

    root.mainloop()