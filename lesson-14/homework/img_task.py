import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

image = np.array([Image.open("images/birds.jpg")])

def flip_image():
    return np.flip(image, axis=(0, 1))

def add_noise():
    mean = 0
    stddev = 25
    noise = np.random.normal(mean, stddev, image.shape).astype(np.uint8)
    noisy_image = np.clip(image + noise, 0, 255)
    return noisy_image
def brighten_channels():
    val = 40
    bright_img =  image.copy()
    new_img = bright_img[:,:,0]=np.clip(bright_img[:,:,0]+val,0,255)
    return new_img
def mask():
    height, width, _ = image.shape  
    mask_size = 100
    center_x, center_y = width // 2, height // 2
    x1, x2 = center_x - mask_size // 2, center_x + mask_size // 2
    y1, y2 = center_y - mask_size // 2, center_y + mask_size // 2
    image[y1:y2, x1:x2] = [0, 0, 0] 