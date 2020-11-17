# Sureveillance-using-Retina-Inspired-Cameras-Object-Detection
This code is for the Design and Innovation Project (group E008) at Nanyang Technological University, Singapore.

**Based on the theory described in https://arxiv.org/abs/1910.01851**

This project aims to use data captured from a Neuromorphic, or Retina Inspired, camera to perform object detection. I implemented an algorithm that uses the images captured by the neuromorphic camera to perform object tracking with low power consumption, low computational cost, and low memory usage. The efficiency of the neuromorphic camera is two-pronged. The first advantage is that an event-based camera image only captures pixels which change value. Additionally, these pixels have a single channel since they are grayscale. Due to this reason, these images take up relatively less memory space as compared to a regular color image which has 3 color channels and way more pixels. The second advantage is that a smaller image size requires less computational power to process. We used an algorithmic approach for object detection instead of more advance techniques like Convolutional Neural Networks to save computational cost. This makes our algorithm ideal for the problem we set out to solve, which is surveillance in remote areas where electric and computational power are hard to get.

This project is split into three major parts:
1) Forming the individual frames
2) Creating bounding boxes
3) Combining frames into an output video.

In order to view frames as with a typical camera, the data from the neuromorphic camera will be transformed from individual events to frames. Next, bounding boxes are created to locate each object (vehicles) individually. After saving each plot as an image file, these images are then stitched together to output a video file. This project is made with Python along with libraries such as Matplotlib, OpenCV, and NumPy.

The project contains the following files:

1) bounding_box.py: This file contains functions to draw the X and Y-historgams for a given frame. It also contains a function that takes in compressed histograms and returns bounding box coordinates for the given frame.
2) compression.py: This file has functions to compress and decompress the X and Y-histograms.
3) draw_boxes.py: This file returns a list of bounding boxes for a given frame.
4) form_frame.py: This frame has the form_frame function which can form a frame based on the given file name, start time and frame time.
5) form_video.py: This file simply takes in a set of images and stitches them into a video.
6) main.py: This is the main file that calls all the functions and saves each frame as an image so that form_video can stitch them together to form a video.

A sample output is as follows: 

![220](https://user-images.githubusercontent.com/55581038/99142689-6f573900-2692-11eb-8f93-a4378a9dfc9a.jpg)


