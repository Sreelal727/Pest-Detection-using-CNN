import tkinter as tk
from tkinter import filedialog
import cv2
import os
import numpy as np
from keras.models import load_model
import requests
from PIL import Image, ImageTk
import threading
import serial  # Add this import for serial communication

model = load_model('CNN.model')

data_dir = "data"
class_names = os.listdir(data_dir)

import urllib.request
import os
from datetime import datetime
import tensorflow as tf
from time import sleep

base = "http://192.168.137.75"

# Global variable to indicate when to perform analysis
perform_analysis = False

def transfer(my_url):   #use to send and receive data
    try:
        n = urllib.request.urlopen(base + my_url).read()
        n = n.decode("utf-8")
        return n

    except:
        pass

def capture_video():
    global perform_analysis
    esp32cam_url = "http://192.168.137.151/capture"
    
    while True:
        # Continuously capture frames from the ESP32-CAM
        response = requests.get(esp32cam_url, stream=True)
        if response.status_code == 200:
            # Decode the image bytes
            img_array = np.asarray(bytearray(response.content), dtype=np.uint8)
            frame = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            
            # Display the live video
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(img)
            img = ImageTk.PhotoImage(img)
            video_label.config(image=img)
            video_label.image = img
            
            # Check if analysis is requested
            if perform_analysis:
                perform_analysis = False
                
                # Perform analysis on the captured frame
                analyze_frame(frame)
        else:
            print("Failed to capture video from ESP32-CAM")


data_dir = "data"
CATEGORIES = os.listdir(data_dir)

def analyze_frame(frame):

    # Resize the frame for model input
    resized_frame = cv2.resize(frame, (100, 100))
    resized_frame = np.expand_dims(resized_frame, axis=0)
    resized_frame = resized_frame / 255.0  # Normalize the image
    
    prediction = model.predict(resized_frame)
    predicted_class = np.argmax(prediction)
    class_label = CATEGORIES[int(predicted_class)]
    result_label.config(text=f"Predicted Class: {class_label}")
    if int(predicted_class) <=6:
        two = transfer(str("1"))
        sleep(3)
        two = transfer(str("3"))
    elif int(predicted_class) >6:
        two = transfer(str("2"))
        sleep(3)
        two = transfer(str("3"))
        
        
    

#    ser.write(str(predicted_class).encode())
    

    
    


def on_q_pressed(event):
    global perform_analysis
    perform_analysis = True

# Create the Tkinter window
root = tk.Tk()
root.title("Live Video Analysis")

# Label to display the live video
video_label = tk.Label(root)
video_label.pack()

# Label to display the analysis result
result_label = tk.Label(root, text="")
result_label.pack()

solution_label = tk.Label(root, text="")
solution_label.pack()

# Bind the 'q' key to the on_q_pressed function
root.bind('q', on_q_pressed)

# Create a thread for capturing video
video_thread = threading.Thread(target=capture_video)
video_thread.start()

# Start the Tkinter main loop
root.mainloop()
