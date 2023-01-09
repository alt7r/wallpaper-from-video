import cv2
import os
import random
import ctypes
import tkinter as tk
from tkinter import filedialog

def set_wallpaper(image_path):
    # Check if the file exists
    if not os.path.exists(image_path):
        print('File does not exist')
        return
    # Set the wallpaper
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)

def save_frame(dir):
    # Open the video file
    video = cv2.VideoCapture(dir)

    # Check if the video was opened successfully
    if not video.isOpened():
        print('Error opening video file')

    # Get the total number of frames in the video
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    # Select a random frame number
    frame_number = random.randint(0, total_frames)

    # Set the video to the selected frame
    video.set(cv2.CAP_PROP_POS_FRAMES, frame_number)

    # Read the frame
    success, frame = video.read()

    # Check if the frame was read successfully
    if success:
        # Create a directory for the images, if it doesn't already exist
        if not os.path.exists('C:/Users/anjel/Pictures/Wallpaper'):
            os.makedirs('C:/Users/anjel/Pictures/Wallpaper')

        # Save the frame as an image
        cv2.imwrite('C:/Users/anjel/Pictures/Wallpaper/frame.jpg', frame)
    else:
        print('Error reading frame')

    # Close the video file
    video.release()


root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(filetypes=[('Video files', '*.mkv *.mp4')])

save_frame(file_path)
set_wallpaper('C:/Users/anjel/Pictures/Wallpaper/frame.jpg')