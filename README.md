# Play Video in ASCII

This Python project allows you to play videos directly in the terminal as **ASCII art**. Each frame of the video is converted into ASCII characters based on brightness, giving a fun text-based video effect.

---

## Features

- Convert any video to ASCII art in real-time.
- Automatically scales to your terminal size.
- Cross-platform (Windows, Linux, macOS).

---

## Requirements

- Python 3.7 or higher
- Libraries:
  - `opencv-python`
  - `shutil` (standard library)
  - `time` (standard library)
  - `os` (standard library)
  - `sys` (standard library)

---

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/anjulanadeeshan/play-video-in-ascii.git
cd play-video-in-ascii
```
2. **Create a virtual environment (optional but recommended)**
```bash
python -m venv venv
# Activate the environment
# Windows:
venv\Scripts\activate
# Linux / macOS:
source venv/bin/activate
```
3. **Install required Python libraries**
```bash
pip install opencv-python
```
4. **Add your video file**
    Place your video (e.g., video.mp4) in the project folder.