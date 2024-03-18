# Head Gesture Detection Application

This application is designed to detect simple head gestures ("Yes" for nodding and "No" for shaking) using a webcam feed in real-time. It employs OpenCV for video capture and facial recognition, alongside basic motion detection algorithms to interpret head movements as responses to a displayed question.

## Setup Instructions

### Prerequisites

- Python 3.x installed on your system.
- A working webcam connected to your computer.
- Basic familiarity with running Python scripts and command-line operations.

### Installation

1. **Clone the repository or download the source code** to your local machine.

2. **Install required Python libraries** by navigating to the directory containing the `requirements.txt` file in your terminal or command prompt, and run the following command:

    ```bash
    pip install -r requirements.txt
    ```

    This command installs all necessary libraries, including OpenCV, which is essential for the application to run.

### Running the Application

To start the application, navigate to the directory containing the Python script (`your_script_name.py`) and run:

```bash
python your_script_name.py
```
### Replace your_script_name.py with the actual name of the Python script if it's different.

### Operation
Upon launching, the application activates your webcam and begins the video feed. A predefined question is displayed at the top of the video feed, and the application starts detecting head movements:

- Nodding (vertical movement) is interpreted as a "Yes" response.
- Shaking (horizontal movement) is interpreted as a "No" response.

Detected gestures are logged in a file named gesture_logs.txt along with a timestamp and the displayed question.

To exit the application, press the 'q' key while the video window is active.

### Customization
To customize the question displayed by the application, open the Python script in a text editor and locate the following line:

```python
question = "Can technology solve all of humanity's problems?"
```

Replace the default question with your desired question, ensuring to keep the quotation marks. Save the changes and rerun the application.

### Troubleshooting
Webcam not detected: Ensure your webcam is properly connected and recognized by your operating system. Try restarting the application or your computer if necessary.
Dependency installation issues: Verify that you have Python and pip correctly installed and accessible from your command line. You may need to update pip (pip install --upgrade pip) or set environment variables correctly.
For more assistance or to report issues, please check the repository's issues section or submit a new issue.





