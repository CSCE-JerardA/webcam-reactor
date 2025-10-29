Webcam Reactor: Real-Time Hand Tracking

This project is a live webcam feed to perform real-time hand detection. It uses OpenCV for video handling and MediaPipe for advanced machine learning-based hand landmark detection. 
This was actually really fun learning and creating. I created this with the help of Google Gemini to outline the steps for making this project, and YouTube videos to give me the idea. 
I debugged everything else along the way. 



* Features

Live Video Processing: Opens a window displaying your live webcam feed.

Real-Time Hand Tracking: Detects hands in the frame using the MediaPipe model.

Visual Landmarks: Overlays key landmarks and connections on detected hands.

Reactor Logic: Displays a text "reaction" on the screen based on the number of hands currently visible.

* Setup and Installation

This project requires a specific Python environment where the dependencies are correctly installed. Based on your successful setup, we will use Python 3.11.

1. Requirements

Make sure you have a working Python 3.11 installation.

2. Install Dependencies

In your PowerShell terminal, run the following command to install opencv-python and mediapipe directly into your Python 3.11 environment:

py -3.11 -m pip install opencv-python mediapipe


* How to Run the Application

Once the dependencies are installed, you must execute the script using the correct Python environment to avoid the ModuleNotFoundError for cv2.

Save your Python file

Navigate to your project folder in PowerShell.

Execute the script using the following command:

py -3.11 webcam_reactor.py


* Controls

Press the "q" key while the application window is focused to exit the program.

* Next Steps & Customization

If you decide to return to the facial recognition idea with the images, remember these steps:

Install the dlib library (which requires cmake):

py -3.11 -m pip install cmake
py -3.11 -m pip install dlib
