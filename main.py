import cv2
import numpy as np
import datetime

# Initialize the video capture object
cap = cv2.VideoCapture(0)

# Load the Haar cascade file for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Parameters for gesture detection
gesture_threshold = 20
frame_counter = 0
cumulative_movement_threshold = 50  # Adjust based on testing

# Question to be displayed
#You can replace the question here
question = "Can technology solve all of humanity's problems?"

# Initialize variables for gesture detection
x_movement = 0
y_movement = 0
prev_face_center = None
gesture_display_counter = 0  # Counter to display the gesture for 2 seconds
display_duration_frames = 60  # Approx 2 seconds at 30 fps
last_gesture = None  # Store the last detected gesture

# Path to the output log file
output_log_path = "gesture_logs.txt"

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) > 0:
        x, y, w, h = faces[0]  # Consider only the first detected face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        face_center = (x + w//2, y + h//2)
        
        if prev_face_center is not None:
            x_movement += abs(face_center[0] - prev_face_center[0])
            y_movement += abs(face_center[1] - prev_face_center[1])
        
        prev_face_center = face_center

    # Display the question on the video stream
    cv2.putText(frame, question, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    if gesture_display_counter > 0:
        gesture_display_counter -= 1
    else:
        if frame_counter >= 10:
            if x_movement > cumulative_movement_threshold and x_movement > y_movement:
                last_gesture = "No"
            elif y_movement > cumulative_movement_threshold and y_movement > x_movement:
                last_gesture = "Yes"

            # Reset variables for the next gesture detection
            x_movement, y_movement, frame_counter = 0, 0, 0
            gesture_display_counter = display_duration_frames  # Reset the display counter
            
            # Log the interaction to the file
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(output_log_path, "a") as log_file:
                log_file.write(f"{timestamp} - Question: '{question}', Answer: '{last_gesture}'\n")
        else:
            frame_counter += 1

    # Display the last detected gesture if the counter is active
    if gesture_display_counter > 0 and last_gesture is not None:
        cv2.putText(frame, f"Gesture Detected: {last_gesture}", (50, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
