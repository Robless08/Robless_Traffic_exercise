import sys
import numpy as np
import cv2
import tensorflow as tf
import tkinter as tk
from tkinter import filedialog, Label, Button
from PIL import Image, ImageTk

# Constants
IMG_WIDTH = 30
IMG_HEIGHT = 30

CATEGORIES = [
    "Speed limit (20km/h)",
    "Speed limit (30km/h)",
    "Speed limit (50km/h)",
    "Speed limit (60km/h)",
    "Speed limit (70km/h)",
    "Speed limit (80km/h)",
    "End of speed limit (80km/h)",
    "Speed limit (100km/h)",
    "Speed limit (120km/h)",
    "No passing",
    "No passing for vehicles over 3.5 metric tons",
    "Right-of-way at the next intersection",
    "Priority road",
    "Yield",
    "Stop",
    "No vehicles",
    "Vehicles over 3.5 metric tons prohibited",
    "No entry",
    "General caution",
    "Dangerous curve to the left",
    "Dangerous curve to the right",
    "Double curve",
    "Bumpy road",
    "Slippery road",
    "Road narrows on the right",
    "Road work",
    "Traffic signals",
    "Pedestrians",
    "Children crossing",
    "Bicycles crossing",
    "Beware of ice/snow",
    "Wild animals crossing",
    "End of all speed and passing limits",
    "Turn right ahead",
    "Turn left ahead",
    "Ahead only",
    "Go straight or right",
    "Go straight or left",
    "Keep right",
    "Keep left",
    "Roundabout mandatory",
    "End of no passing",
    "End of no passing by vehicles over 3.5 metric tons"
]

class TrafficSignRecognizer:
    def __init__(self, root, model_file):
        self.root = root
        self.root.title("Traffic Sign Recognition")
        self.model = tf.keras.models.load_model(model_file)
        
        self.label = Label(root, text="Select an image to predict", font=("Arial", 14))
        self.label.pack(pady=10)
        
        self.image_label = Label(root)
        self.image_label.pack()
        
        self.predict_button = Button(root, text="Select Image", command=self.load_image)
        self.predict_button.pack(pady=10)
        
        self.result_label = Label(root, text="", font=("Arial", 12))
        self.result_label.pack()
    
    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.ppm;*.png;*.jpg;*.jpeg")])
        if not file_path:
            return
        
        image = cv2.imread(file_path)
        if image is None:
            self.result_label.config(text="Error: Could not read the image file.")
            return
        
        image = cv2.resize(image, (IMG_WIDTH, IMG_HEIGHT))
        self.predict(image, file_path)
    
    def predict(self, image, file_path):
        prediction = self.model.predict(np.array([image]))
        predicted_category = np.argmax(prediction)
        confidence = np.max(prediction) * 100
        
        img = Image.open(file_path)
        img = img.resize((200, 200), Image.Resampling.LANCZOS)
        img = ImageTk.PhotoImage(img)
        
        self.image_label.config(image=img)
        self.image_label.image = img
        
        self.result_label.config(text=f"Predicted Category: {CATEGORIES[predicted_category]}\nConfidence: {confidence:.2f}%")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python recognition.py model.h5")
    
    model_file = sys.argv[1]
    root = tk.Tk()
    app = TrafficSignRecognizer(root, model_file)
    root.mainloop()
