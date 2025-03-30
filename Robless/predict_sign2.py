import sys, os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np
import cv2
from tensorflow.keras.models import load_model

# Constants
IMG_WIDTH = 30
IMG_HEIGHT = 30
NUM_CATEGORIES = 43

# Set the model path
CURRENT_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(CURRENT_DIR,"best_model.h5")
    
# Load the trained model
model = load_model(MODEL_PATH)

# String representation of the gtsrb dataset categories
CATEGORY_STRINGS = [
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

def predictor_function(image_path):
    """
    Predict the category of the traffic sign in the given image file.
    """
    try:
        # Load and preprocess the image
        image = cv2.imread(image_path)
        image = cv2.resize(image, (IMG_WIDTH, IMG_HEIGHT))
        image = np.array(image) / 255.0  # Normalize pixel values
        image = np.expand_dims(image, axis=0)  # Add batch dimension

        # Predict using the model
        predictions = model.predict(image)
        predicted_category = np.argmax(predictions)
        accuracy = np.max(predictions)

        return predicted_category, CATEGORY_STRINGS[predicted_category], accuracy
    
    except Exception as e:
        messagebox.showerror("Error", f"Failed to predict image: {e}")
        return None

def file_opener():
    """
    Open a file dialog to select an image and display the prediction.
    """
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image Files", "*.ppm;*.jpg;*.jpeg;*.png;*.bmp;*.tiff;*.webp")]
    )
    if not file_path:
        return
    try:
        # Display the selected image
        image = Image.open(file_path)
        max_size = (250, 250)
        image.thumbnail(max_size, Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo

        # Predict the traffic sign category
        number, sign, probability  = predictor_function(file_path)
        if sign and probability:
            results = f"Prediction \n Sign: {sign}, Accuracy: {probability:.2f}"
            result_label.config(text=results)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open image: {e}")

# Create the tkinter interface
root = tk.Tk()
root.title("Road Sign Predictor")

root.geometry("500x500")

# Create and place widgets
frame = tk.Frame(root)
frame.pack(pady=20)

text_label = tk.Label(frame, text="Upload A Traffic Sign Image", font=("Arial", 14, "bold"))
text_label.pack()

image_label = tk.Label(frame)
image_label.pack(pady=10)

button = tk.Button(frame, text="Select Image", command=file_opener)
button.pack(pady=10)


result_label = tk.Label(frame, text="Predicted Category: None", font=("Arial", 12))
result_label.pack(pady=10)

# Run the tkinter main loop
root.mainloop()