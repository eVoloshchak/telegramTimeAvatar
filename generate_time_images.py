from utils import *
from config import *
import cv2
import os.path
import numpy as np
from datetime import datetime, timedelta

def get_black_background():
    return np.zeros((500, 500))

start_time = datetime.strptime("2019-01-01", "%Y-%m-%d")
end_time = start_time + timedelta(days=1)

def generate_image_with_text(text):
    image = get_black_background()
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(image, text, (int(image.shape[0]*0.15), int(image.shape[1]*0.5)), font, 4, (255, 255, 0), 20, cv2.LINE_AA)
    return image

while start_time < end_time:
    if not os.path.exists(images_dir):
        os.mkdir(images_dir)
    text = convert_time_to_string(start_time)
    image = generate_image_with_text(text)
    cv2.imwrite(f"{images_dir}/{text.replace(':', '-')}.jpg", image)
    start_time += timedelta(minutes=1)
