import cv2 as cv
from tkinter import Tk, filedialog

# Hide the Tkinter root window
root = Tk()
root.withdraw()

# Open a file dialog to select a video
video_path = filedialog.askopenfilename(
    title="Select a Video File",
    filetypes=[
        ("Video Files", "*.mp4 *.avi *.mov *.mkv *.wmv"),
        ("All Files", "*.*")
    ]
)

# Check if a file was selected
if not video_path:
    print("No video file selected.")
    exit()

# Open the selected video
cap = cv.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Cannot open the selected video file.")
    exit()

# Read and display the video
while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv.imshow("Video Player", frame)

    # Press 'q' to stop playback
    if cv.waitKey(25) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv.destroyAllWindows()