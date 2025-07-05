import numpy as np
import cv2
import sys

# Initialize video capture
cap = cv2.VideoCapture(0)

# Set frame rate to 15 FPS for better performance
cap.set(cv2.CAP_PROP_FPS, 15)

# Check if camera is opened
if not cap.isOpened():
    print("Error: Could not open camera")
    print("Make sure:")
    print("1. Camera is not being used by another application")
    print("2. Terminal has camera permissions in System Preferences")
    sys.exit(1)

# Load face cascade classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Check if cascade loaded successfully
if face_cascade.empty():
    print("Error: Could not load face cascade classifier")
    sys.exit(1)

print("Face detection started. Press 'q' to quit.")

frame_counter = 0
skip_frames = 3  # Process every 3rd frame

while True:
    ret, frame = cap.read()
    
    # Check if frame was captured successfully
    if not ret or frame is None:
        print("Error: Failed to capture frame")
        break
    
    # Resize the frame to 640x480 (reduce resolution)
    frame = cv2.resize(frame, (640, 480))

    # Skip frames to reduce load
    if frame_counter % skip_frames == 0:
        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the grayscale image
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        # Draw rectangles around the detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Display the number of faces detected
        cv2.putText(frame, f"Faces Detected: {len(faces)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    frame_counter += 1

    # Display the frame
    cv2.imshow('Face Detection', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
