# main_mouse.py
# Install the required libraries using pip:
# pip install opencv-python cvzone pynput numpy

import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
from pynput.mouse import Controller, Button as MouseButton
import time

# --- Initialization ---
# Initialize webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # Set camera width
cap.set(4, 720)   # Set camera height

# Initialize Hand Detector
detector = HandDetector(detectionCon=0.8, maxHands=1)

# Initialize Mouse Controller
mouse = Controller()

# --- Configuration ---
SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 1080 # Change this to your screen resolution
FRAME_REDUCTION = 100 # A border to keep the cursor from hitting the screen edges
SMOOTHENING = 7 # Factor to smooth out cursor movement

# --- Variables ---
prev_x, prev_y = 0, 0
curr_x, curr_y = 0, 0
CLICK_COOLDOWN = 0.5  # seconds
last_click_time = 0

# --- Main Application Loop ---
while True:
    # 1. Read a frame from the webcam
    success, img = cap.read()
    if not success:
        continue

    # Flip the image horizontally for a mirror effect
    img = cv2.flip(img, 1)

    # 2. Find Hands and their landmarks
    hands, img = detector.findHands(img, flipType=False)

    # 3. Check for gestures
    if hands:
        hand = hands[0]
        lm_list = hand['lmList']

        # Ensure we have landmarks to work with
        if len(lm_list) != 0:
            # Get the coordinates of the index finger tip (landmark 8)
            # Note: lm_list provides [x, y, z], we only need x and y.
            x1, y1 = lm_list[8][:2]
            
            # --- Mouse Movement ---
            # Convert coordinates from camera space to screen space
            screen_x = np.interp(x1, (FRAME_REDUCTION, 1280 - FRAME_REDUCTION), (0, SCREEN_WIDTH))
            screen_y = np.interp(y1, (FRAME_REDUCTION, 720 - FRAME_REDUCTION), (0, SCREEN_HEIGHT))

            # Smoothen the movement
            curr_x = prev_x + (screen_x - prev_x) / SMOOTHENING
            curr_y = prev_y + (screen_y - prev_y) / SMOOTHENING

            # Move the mouse
            mouse.position = (curr_x, curr_y)
            prev_x, prev_y = curr_x, curr_y

            # Draw a circle on the index finger tip for visual feedback
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)

            # --- Mouse Click ---
            # Calculate the distance between index (8) and middle (12) finger tips
            # **FIXED LINE:** We pass only the x and y coordinates ([:2]) of each landmark
            length, _, _ = detector.findDistance(lm_list[8][:2], lm_list[12][:2], img)

            # If the distance is small, it's a click
            if length < 40:
                current_time = time.time()
                if current_time - last_click_time > CLICK_COOLDOWN:
                    # Highlight the fingertips to indicate a click
                    cv2.circle(img, (x1, y1), 15, (0, 255, 0), cv2.FILLED)
                    # Perform the click
                    mouse.click(MouseButton.left, 1)
                    last_click_time = current_time

    # 4. Display the image
    cv2.imshow("AI Virtual Mouse", img)

    # 5. Exit Condition
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# --- Cleanup ---
cap.release()
cv2.destroyAllWindows()
