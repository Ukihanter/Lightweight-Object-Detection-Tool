from ultralytics import YOLO  
import cv2
import os
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, filedialog
import tkinter as tk  

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\python\OD\build\assets\frame0")  

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.title("Object Detection Tool by Uki")
window.geometry("656x386")
window.configure(bg="#262626")

# Load YOLO model
model = YOLO("../yolo/yolov8n.pt")

# Global variable to store the selected file path
selected_image_path = None

def get_image():
    global selected_image_path
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", ["*.png", "*.jpg", "*.jpeg"])])
    if file_path:
        selected_image_path = file_path  # Store the selected image path
        entry_1.delete(0, tk.END)
        entry_1.insert(0, file_path)  # Show the full path in the entry field

def detect_objects():
    global selected_image_path
    if selected_image_path:  # Check if an image has been selected
        results = model(selected_image_path, show=True)
        cv2.waitKey(0)  # Wait for key press before closing the window
    else:
        print("No image selected! Please select an image first.")

canvas = Canvas(
    window,
    bg="#262626",
    height=386,
    width=656,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.create_text(
    175.0,
    55.0,
    anchor="nw",
    text="Simple Object Detection Tool",
    fill="#FFFFFF",
    font=("Handjet Bold", 32 * -1)
)

canvas.create_text(
    480.0,
    91.0,
    anchor="nw",
    text="by Uki",
    fill="#FFFFFF",
    font=("YsabeauOffice Bold", 14 * -1)
)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=get_image,
    relief="flat"
)
button_1.place(x=175.0, y=160.0, width=305.0, height=54.0)

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(331.5, 249.5, image=entry_image_1)

entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(x=183.0, y=235.0, width=297.0, height=27.0)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=detect_objects,  # Call the object detection function
    relief="flat"
)
button_2.place(x=238.0, y=309.0, width=199.0, height=46.0)

window.resizable(False, False)
window.mainloop()
