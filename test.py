import cv2
import os
import time
import sys
import shutil
# ASCII characters used to represent pixels (dark to light)
ASCII_CHARS = "@%#*+=-:. "

def get_terminal_size():
    size = shutil.get_terminal_size(fallback=(80, 24))
    return size.columns, size.lines  # width, height

def resize_image(image):
    term_width, term_height = get_terminal_size()
    
    # Reduce a bit so it doesn’t overflow
    new_width = term_width - 2
    aspect_ratio = image.shape[0] / image.shape[1]
    new_height = int(aspect_ratio * new_width * 0.55)
    
    if new_height > term_height - 2:
        new_height = term_height - 2
    
    resized = cv2.resize(image, (new_width, new_height))
    return resized


def gray_to_ascii(image):
    ascii_str = ""
    for row in image:
        for pixel in row:
            # ensure pixel is Python int (not uint8)
            index = int(pixel) * len(ASCII_CHARS) // 256
            ascii_str += ASCII_CHARS[index]
        ascii_str += "\n"
    return ascii_str



def play_video_ascii(video_path):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)
    delay = 1 / fps if fps > 0 else 0.03

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            resized = resize_image(gray)
            ascii_frame = gray_to_ascii(resized)

            # Clear screen (cross-platform)
            os.system("cls" if os.name == "nt" else "clear")

            print(ascii_frame)
            time.sleep(delay)

    except KeyboardInterrupt:
        print("Stopped.")
    finally:
        cap.release()

# Run with your video file
play_video_ascii("video.mp4")
