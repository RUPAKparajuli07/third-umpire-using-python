# Documentation for Fault Detection Application

## Overview
The Fault Detection Application is a graphical user interface (GUI) program built using the tkinter library in Python. This application allows users to play and analyze video clips (e.g., cricket match scenarios) frame by frame, and make decisions regarding a player being "out" or "not out." The program provides controls for navigating through the frames and making decisions about the gameplay.

## Requirements
To run the Fault Detection Application, you need to have the following dependencies installed:
- Python (3.6 or later)
- OpenCV (`cv2` module)
- Pillow (`PIL` module)
- Imutils (for resizing frames)
- tkinter (usually included with Python)

The application also requires the following image and video files to be present in the same directory as the Python script:
- `clip.mp4`: The video clip to be analyzed.
- `pending.jpg`: An image to display while the decision is pending.
- `sponsors.jpg`: An image to display after the pending time.
- `out.png`: An image representing the decision "out."
- `not out.png`: An image representing the decision "not out."
- `welcome.jpg`: An image displayed initially when the application starts.

## Code Explanation
The code consists of several functions and GUI elements that work together to create the Fault Detection Application. Here's an explanation of each part:

### Importing Libraries
The required libraries are imported at the beginning of the code. These include `tkinter` for GUI, `cv2` for video processing, `PIL` for image display, `functools.partial` for passing arguments to functions, `threading` for handling concurrent tasks, `time` for delays, and `imutils` for resizing frames.

### Global Variables
- `stream`: A VideoCapture object representing the video stream loaded from "clip.mp4."
- `flag`: A boolean variable used to alternate between displaying "Decision Pending" and not displaying it on the GUI.

### GUI Functions
1. `play(speed)`: This function is triggered when the user clicks on any of the "Previous" or "Next" buttons. It updates the video stream to the desired frame based on the `speed` argument (number of frames to move forward or backward). It then resizes and displays the frame on the tkinter canvas. Additionally, if the `flag` is True, it displays "Decision Pending" on the GUI. The `flag` is toggled at each call of this function.

2. `pending(decision)`: This function is responsible for showing the "Decision Pending" message, waiting for a specific time, showing the "Sponsors" image, waiting again, and then displaying the final decision (either "out" or "not out"). The `decision` argument determines which image is displayed for the final decision.

3. `out()`: This function is called when the "Give Out" button is clicked. It starts a new thread to call the `pending` function with the "out" decision.

4. `not_out()`: This function is called when the "Give Not Out" button is clicked. It starts a new thread to call the `pending` function with the "not out" decision.

### GUI Setup
The following steps configure the GUI window and display the initial image:
1. Initialize the tkinter window and set its title.
2. Load an image ("welcome.jpg") using OpenCV, convert it to RGB format, and display it on the tkinter canvas.
3. Create the button frame and pack it to the right side of the window.
4. Create buttons with different functionalities and place them in the button frame.

### Button Functionalities
The buttons in the button frame are used for the following actions:
- "<< Previous (fast)": Move backward in the video by 25 frames.
- "<< Previous (slow)": Move backward in the video by 2 frames.
- "Next (slow) >>": Move forward in the video by 2 frames.
- "Next (fast) >>": Move forward in the video by 25 frames.
- "Give Out": Trigger the "out" decision process.
- "Give Not Out": Trigger the "not out" decision process.

## How to Use the Application
1. Ensure you have all the required dependencies installed and have the necessary image and video files in the same directory as the Python script.
2. Run the Python script to start the application.
3. The GUI window will open, displaying the initial image ("welcome.jpg").
4. Use the provided buttons to navigate through the video frames. The "Previous" buttons move backward, and the "Next" buttons move forward in the video.
5. When you need to make a decision about a player being "out" or "not out," click the corresponding "Give Out" or "Give Not Out" button. The application will display "Decision Pending" for a brief time and then show the "Sponsors" image before displaying the final decision ("out" or "not out").

Please note that the application may have been designed for specific use cases (e.g., analyzing cricket match scenarios), and you can modify the code and resources to suit your own requirements.

## Additional Notes
- The GUI layout and design can be further enhanced by customizing the button appearance, adding labels, or using different image sizes and layouts.
- The video clip ("clip.mp4") used in the application can be replaced with another video for analysis.
- The timing of "Decision Pending" and "Sponsors" display can be adjusted by modifying the sleep durations in the `pending` function.
- Make sure to handle errors gracefully when using the application to ensure a smooth user experience. For example, handle cases where the video or image files are not found, or when trying to access frames beyond the video's length.

Enjoy using the Fault Detection Application to analyze video clips and make decisions about gameplay!
