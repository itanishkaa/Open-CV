# Open CV
## Project Overview
This repository includes several exciting image processing techniques implemented using OpenCV

**1. Color Detection:** Automatically detect and extract colors from an image.

**2. Contour Detection:** Detect the shapes and boundaries of objects in an image.

**3. Edge Detection:** Apply edge-detection algorithms to highlight edges in an image.

**4. Photo Sketching:** Turn your photos into beautiful, pencil-drawn sketches.

## What's Inside
**1. Color Detection**

This section helps you automatically detect and isolate specific colors in an image.
- `color.py`: Python script to detect various colors in the image.
- `colors.csv`: A CSV containing color data used in the detection.
- `img.webp`: A sample image for testing the color detection script.

**2. Detecting Contours**

Identify the edges and boundaries of objects within an image using contour detection.
- `detecting_contours.py`: A Python script that highlights the contours of objects.

**3. Edge Detection**

Explore edge detection algorithms that help outline the sharp features in an image.

- `edge_detection.py`: Apply the famous Canny edge detection algorithm to any image.

**4. Photo Sketching**

Convert your photos into sketch-like images with the magic of OpenCV!

- `photo_sketching.py`: Main script to turn photos into sketches.
- `photo1.py`: Example of a photo being processed into a beautiful sketch.

## Prerequisites
Make sure you have Python installed and the necessary dependencies

```python
pip install opencv-python numpy
```

## How to Use
**1. Color Detection:**

Run `color.py` to detect and isolate colors from the sample image *(img.webp)*.

**2. Contour Detection:**

Use `detecting_contours.py` to detect contours within your images. This script will help you identify shapes and boundaries.

**3. Edge Detection:**

Try `edge_detection.py` to apply edge detection algorithms (like Canny) and see the edges of the objects in your image.

**4. Photo Sketching:**

Run `photo_sketching.py` to convert your photo into a pencil sketch. Customize the photo path inside the script and watch the magic happen!

## Why Open CV?
OpenCV (Open Source Computer Vision Library) is one of the most powerful libraries for real-time computer vision. It’s fast, efficient, and widely used in industry and research. With just a few lines of code, you can create awesome projects like these and more!
