# Documentation for "Let's find fault of the game (Third Umpire)" Application

## Description:
"Let's find fault of the game" is a Python application built using the Tkinter library for creating graphical user interfaces, and OpenCV (cv2) for handling video processing. The application allows users to watch a video clip and make decisions about specific moments in the video. The user can play the video at different speeds, move frame by frame, and make decisions whether a player is "out" or "not out" at certain points in the video. The application displays images with text overlays to indicate the decision status.  

## Requirements:
- Python 3.x
- Tkinter
- OpenCV (cv2)
- PIL (Python Imaging Library)
- imutils
- NumPy

Ensure you have the necessary libraries installed before running the application.

## Usage:
1. Save the video file "clip.mp4" in the same directory as the script.
2. Place the image files "pending.jpg", "sponsors.jpg", "out.png", and "not out.png" in the same directory as the script.
3. Make sure the image "welcome.jpg" is present in the same directory as well.
4. Run the script.

## Functionality:
1. **play(speed):**
   - This function is called when the user clicks on any of the "Previous" or "Next" buttons to play the video at different speeds.
   - The `speed` parameter determines the number of frames to move forward or backward from the current frame.
   - It reads a frame from the video stream and displays it on the Tkinter canvas.
   - The frame is resized to the dimensions defined by `SET_WIDTH` and `SET_HEIGHT`.
   - It alternates the "Decision Pending" text on the canvas.
   - The function also updates the `flag` variable to alternate between displaying "Decision Pending" and no text.

2. **pending(decision):**
   - This function is called when the user clicks on either the "Give Out" or "Give Not Out" buttons to make a decision.
   - The `decision` parameter should be either "out" or "not out" based on the user's decision.
   - The function displays intermediate images on the canvas with a delay to mimic a decision-making process.
   - The intermediate images displayed are "pending.jpg" and "sponsors.jpg".
   - It then displays the final decision image based on the user's input, either "out.png" or "not out.png".

3. **out():**
   - This function is called when the user clicks on the "Give Out" button.
   - It creates a new thread to run the `pending()` function with the parameter "out" to indicate that the player is out.
   - It prints "Player is out" to the console.

4. **not_out():**
   - This function is called when the user clicks on the "Give Not Out" button.
   - It creates a new thread to run the `pending()` function with the parameter "not out" to indicate that the player is not out.
   - It prints "Player is not out" to the console.

5. **Constants:**
   - `SET_WIDTH` and `SET_HEIGHT`: These constants define the dimensions to which the video frames and images are resized for display on the Tkinter canvas.
   - `stream`: A video capture object that reads the "clip.mp4" video file.
   - `flag`: A boolean variable used to alternate between displaying "Decision Pending" and no text on the canvas.

6. **Tkinter GUI Setup:**
   - The script creates a Tkinter window titled "Let's find fault of the game" and maximizes it (zoomed state).
   - The video and images are loaded using OpenCV and PIL, respectively, and displayed on the Tkinter canvas.
   - The buttons for various functionalities are arranged in a right-aligned frame on the window.

## Buttons Functionality:
- "<< Previous (fast)": Clicking this button plays the video backward at a faster speed (25 frames per click).
- "<< Previous (slow)": Clicking this button plays the video backward at a slower speed (2 frames per click).
- "Next (slow) >>": Clicking this button plays the video forward at a slower speed (2 frames per click).
- "Next (fast) >>": Clicking this button plays the video forward at a faster speed (25 frames per click).
- "Give Out": Clicking this button indicates that the player is out. The application displays intermediate images before showing the final decision.
- "Give Not Out": Clicking this button indicates that the player is not out. The application displays intermediate images before showing the final decision.

## Note:
- The application may not work correctly without the required video and image files in the specified paths.
- Ensure that you have the necessary video codecs installed to read the video file.
