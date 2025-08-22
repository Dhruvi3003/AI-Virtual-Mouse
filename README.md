# 🖱️ AI Virtual Mouse using Hand Gesture Recognition  

Control your computer’s mouse cursor using **hand gestures** captured through your webcam!  
Move your hand to move the cursor, and pinch your fingers together to click.  
It’s an **intuitive, touch-free way** to interact with your computer.  

---

## 🚀 Features  
- 🎯 **Cursor Control** – Move your **index finger** to move the mouse cursor.  
- 🖐️ **Clicking** – Pinch your **index + middle fingers** together to perform a left-click.  
- ⚡ **Real-Time Tracking** – Uses computer vision to track hand gestures instantly.  
- ⚙️ **Customizable** – Adjust screen resolution, cursor smoothing, and sensitivity.  

---

## 🛠️ Requirements  

Make sure you have **Python 3.x** installed, then install the dependencies:  

```bash
pip install opencv-python cvzone pynput numpy
```

### Libraries Used
- **OpenCV (opencv-python)** – Webcam capture & image processing  
- **cvzone** – Simplifies hand tracking with MediaPipe  
- **pynput** – Mouse control  
- **NumPy** – Coordinate mapping & calculations  

---

## ▶️ How to Run  

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/YOUR_USERNAME/AI-Virtual-Mouse.git
   cd AI-Virtual-Mouse
   ```

2. **Run the Script**  
   ```bash
   python main.py
   ```

3. **Interact with the Mouse**  
   - A webcam window will appear.  
   - Show your **hand to the camera**.  
   - Move your **index finger** → control the mouse pointer.  
   - Bring your **index & middle finger together** → left-click.  

4. **Exit**  
   - Press **`q`** while the webcam window is active to close the program.  

---

## 📂 Project Structure  
```
AI-Virtual-Mouse/
│── main.py          # Main script to run the project
│── README.md        # Project documentation
```

---

## 📌 Future Improvements  
- ✨ Right-click & double-click gestures  
- ✨ Scroll functionality  
- ✨ Multi-hand support  
- ✨ Gesture customization via config file  

---

## 🙌 Acknowledgements  
- [OpenCV](https://opencv.org/)  
- [cvzone](https://pypi.org/project/cvzone/)  
- [pynput](https://pypi.org/project/pynput/)  
- [NumPy](https://numpy.org/)  
