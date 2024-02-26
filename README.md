# SecureAccessMonit - Face Recognition Access Monitoring System

## Created by: Ahmed Alzeidi
## Software Engineering
## GitHub: [ZidiAhmed](https://github.com/ZidiAhmed)

## Overview

SecureAccessMonit is a Python-based project that utilizes face recognition technology to monitor and control access to a secure environment. The system captures video input from a camera, detects faces, and matches them against a database of known faces. Based on the recognition results, it provides real-time feedback, displaying the names of recognized individuals along with additional information such as date, time, and day.

## Features

- **Face Recognition:** Utilizes the face_recognition library to identify faces in real-time.
- **Access Control:** Displays the names of recognized individuals and additional information.
- **User Database:** Loads known faces and corresponding names from a specified folder.
- **Real-time Feedback:** Provides immediate feedback on recognized and unrecognized individuals.

## Dependencies

- OpenCV (cv2)
- face_recognition
- NumPy
- os
- datetime

## Usage

1. Ensure you have all the required dependencies installed.

   ```bash
   pip install opencv-python face_recognition numpy
   ```

2. Organize known faces in the "stuff_image" folder. Each image should be in either JPG or PNG format.

3. Run the `SecureAccessMonit.py` script.

   ```bash
   python SecureAccessMonit.py
   ```

4. The system will start capturing video from the default camera (change the camera index if needed). Recognized individuals will be displayed with their names, and additional information will be shown at the top of the video feed.

5. Press 'q' to exit the application.

## Notes

- Ensure that the camera is properly connected and accessible.
- The system displays "Welcome" in green for recognized individuals and "Sorry" in red for unrecognized individuals.
- If no faces are detected, a yellow square with "No Face Detected" will be displayed.

Feel free to customize the project according to your specific requirements or integrate it into a larger security monitoring system.