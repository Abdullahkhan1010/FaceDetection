# Face Detection Project

A real-time computer vision project using OpenCV and Python for face detection with performance optimizations and robust error handling.

## Features

- **Real-time Face Detection** - Detects faces in live video stream from webcam
- **Performance Optimized** - Frame skipping and resolution scaling for smooth performance
- **Visual Feedback** - Blue rectangles around detected faces with face count display
- **Error Handling** - Comprehensive error checking for camera access and frame capture
- **macOS Compatible** - Proper handling of macOS camera permissions
- **Resource Management** - Automatic cleanup of camera and window resources

## Requirements

- Python 3.x
- OpenCV (cv2) >= 4.0
- NumPy
- macOS/Linux/Windows with webcam access

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd facedetection
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install opencv-python numpy
```

## Usage

### Basic Usage
```bash
python3 main.py
```

### Controls
- **Press 'q'** to quit the application
- Position yourself in front of the camera to see face detection in action

### macOS Setup
If you encounter camera permission errors:
1. Go to **System Preferences** → **Security & Privacy** → **Privacy** → **Camera**
2. Enable **Terminal** or your IDE to access the camera
3. Restart Terminal after granting permissions

## Technical Details

### Performance Optimizations
- **Frame Skipping**: Processes every 3rd frame to reduce CPU load
- **Resolution Scaling**: Resizes frames to 640x480 for faster processing
- **Efficient Detection**: Uses Haar Cascade classifier for balanced speed/accuracy

### Error Handling
- Camera availability checking
- Frame capture validation
- Cascade classifier loading verification
- Graceful error messages with troubleshooting tips

## Code Structure

```
facedetection/
├── main.py              # Main face detection script
├── requirements.txt     # Python dependencies
├── README.md           # Project documentation
└── .gitignore          # Git ignore rules
```

## Troubleshooting

### Camera Not Working
- Ensure no other applications are using the camera
- Check camera permissions in System Preferences (macOS)
- Try different camera indices (0, 1, 2) if you have multiple cameras

### Performance Issues
- Increase `skip_frames` value in the code for lower-end hardware
- Reduce frame resolution by modifying the resize parameters
- Close other resource-intensive applications

## Customization

### Adjust Detection Sensitivity
Modify the `detectMultiScale` parameters in `main.py`:
```python
faces = face_cascade.detectMultiScale(
    gray, 
    scaleFactor=1.3,    # Decrease for more detections
    minNeighbors=5,     # Decrease for more detections
    minSize=(30, 30)    # Minimum face size
)
```

### Change Detection Colors
Modify the rectangle and text colors:
```python
cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Blue rectangle
cv2.putText(frame, f"Faces Detected: {len(faces)}", (10, 30), 
           cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)        # Green text
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- OpenCV community for the excellent computer vision library
- Haar Cascade classifiers for face detection algorithms
