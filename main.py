from PIL import ImageGrab
import numpy as np
import cv2
import tkinter as tk

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# print(screen_width, screen_height)

force = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
capture_video = cv2.VideoWriter("my_file.mp4", force, 20.0, (screen_width, screen_height))

while True:
    img = ImageGrab.grab(bbox=(0, 0, screen_width, screen_height))
    img_np = np.array(img)
    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    cv2.imshow("Final Video", img_final)
    capture_video.write(img_final)
    if cv2.waitKey(3) == ord('q'):
        break