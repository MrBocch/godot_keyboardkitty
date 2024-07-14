# strip images from a gif
from PIL import Image
import os

def extract_frames(gif_path, output_folder):
    gif = Image.open(gif_path)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for frame in range(gif.n_frames):
        gif.seek(frame)
        frame_image = gif.copy()
        frame_image.save(os.path.join(output_folder, f"frame_{frame}.png"))

gif_path = "kitty.gif"
output_folder = "./"

extract_frames(gif_path, output_folder)
