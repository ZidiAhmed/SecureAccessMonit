import cv2
import face_recognition
import numpy as np
import os
from datetime import datetime

def load_known_faces(folder_path):
    known_faces = []
    known_names = []

    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(folder_path, filename)
            face_image = face_recognition.load_image_file(image_path)
            face_encoding = face_recognition.face_encodings(face_image)[0]

            known_faces.append(face_encoding)
            known_names.append(os.path.splitext(filename)[0])

    return known_faces, known_names

def recognize_faces(video_capture, known_faces, known_names):
    while True:
        ret, frame = video_capture.read()
        if not ret:
            print("Error reading frame from the camera.")
            break

        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        is_known_person = False  # Flag to check if the person is recognized

        for face_encoding, (top, right, bottom, left) in zip(face_encodings, face_locations):
            matches = face_recognition.compare_faces(known_faces, face_encoding)

            # Check if any matches are found
            if any(matches):
                is_known_person = True
                first_match_index = matches.index(True)
                name = known_names[first_match_index]

                # Display the person's name on the first line
                cv2.putText(frame, f"Person: {name}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

                # Display the time, date, and day on the second line
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                current_date = now.strftime("%Y-%m-%d")
                current_day = now.strftime("%A")

                second_line_text = f"Time: {current_time} | Date: {current_date} | Day: {current_day}"
                cv2.putText(frame, second_line_text, (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2, cv2.LINE_AA)

                # Display "Welcome" in green at the bottom
                cv2.putText(frame, "Welcome", (50, frame.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2, cv2.LINE_AA)

                # Draw a green rectangle around the face
                cv2.rectangle(frame, (left * 4, top * 4), (right * 4, bottom * 4), (0, 255, 0), 2)
            else:
                # If no matches are found, display "Unknown Person" along with time, date, and day
                # Display "Sorry" in red at the bottom
                cv2.putText(frame, "Sorry", (50, frame.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2, cv2.LINE_AA)

                # Draw a red rectangle around the face
                cv2.rectangle(frame, (left * 4, top * 4), (right * 4, bottom * 4), (0, 0, 255), 2)

        # If no faces are detected, show a yellow square
        if not face_locations:
            cv2.rectangle(frame, (50, frame.shape[0] - 20), (200, frame.shape[0]), (0, 255, 255), -1)
            cv2.putText(frame, "No Face Detected", (50, frame.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

        # Display the resulting frame
        cv2.imshow('Video', frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

def main():
    stuff_image_folder = "stuff_image"
    known_faces, known_names = load_known_faces(stuff_image_folder)

    video_capture = cv2.VideoCapture(0)  # Use 0 for default camera, change if needed
    if not video_capture.isOpened():
        print("Error opening video camera.")
        return

    recognize_faces(video_capture, known_faces, known_names)

if __name__ == "__main__":
    main()
