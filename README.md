AI Virtual Mouse using Hand Gesture Recognition
This project allows you to control your computer's mouse cursor using hand gestures captured through your webcam. Move your hand to move the cursor, and pinch your fingers together to click. It's an intuitive, touch-free way to interact with your computer.

Features
Cursor Control: Move your index finger to move the mouse cursor across the screen.

Clicking: Pinch your index and middle fingers together to perform a left-click.

Real-Time Interaction: The application uses computer vision to track your hand movements in real-time.

Customizable: Easily adjust settings like screen resolution and cursor smoothing in the code.

Requirements
To run this project, you'll need to have Python installed on your system, along with the following libraries:

opencv-python: For capturing and processing video from your webcam.

cvzone: A library that simplifies hand tracking with MediaPipe.

pynput: To control the mouse.

numpy: For numerical operations, specifically for mapping coordinates.

You can install all the required libraries by running this command in your terminal:

pip install opencv-python cvzone pynput numpy

How to Use
Clone or Download the Repository:

git clone [https://github.com/YOUR_USERNAME/AI-Virtual-Mouse.git](https://github.com/YOUR_USERNAME/AI-Virtual-Mouse.git)
cd AI-Virtual-Mouse

Run the Script:
Execute the main Python script from your terminal:

python main.py

Interact:

A window will open showing your webcam feed.

Hold your hand up so the camera can see it.

Move your index finger to control the mouse pointer.

Bring your middle finger close to your index finger to simulate a click.

Exit the Application:

To stop the program, make sure the webcam window is active and press the 'q' key.