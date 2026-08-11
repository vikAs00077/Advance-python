import cv2
import math

cap = cv2.VideoCapture(0)

drawing = False
start_point = None
current_point = None
first_point = None

lines = []

SNAP_DISTANCE = 30

# This becomes True when the shape is closed
shape_closed = False


def distance(p1, p2):
    return math.sqrt(
        (p1[0] - p2[0]) ** 2 +
        (p1[1] - p2[1]) ** 2
    )


def mouse_callback(event, x, y, flags, param):
    global drawing, start_point, current_point
    global first_point, lines, shape_closed

    if event == cv2.EVENT_LBUTTONDOWN:

        if shape_closed:
            return

        drawing = True

        # First point
        if first_point is None:
            first_point = (x, y)
            start_point = first_point

        current_point = (x, y)

    elif event == cv2.EVENT_MOUSEMOVE and drawing:

        current_point = (x, y)

        # Snap to first point
        if first_point is not None:
            if distance(current_point, first_point) < SNAP_DISTANCE:
                current_point = first_point

    elif event == cv2.EVENT_LBUTTONUP:

        if not drawing:
            return

        drawing = False
        current_point = (x, y)

        # Check if user reached the first point
        if first_point is not None:

            if distance(current_point, first_point) < SNAP_DISTANCE:

                # Connect exactly to first point
                current_point = first_point

                lines.append(
                    (start_point, first_point)
                )

                # Shape is now closed
                shape_closed = True

                print("Shape closed!")
                print("Closing webcam...")

                return

        # Normal line
        lines.append(
            (start_point, current_point)
        )

        # Next line starts at previous endpoint
        start_point = current_point


cv2.namedWindow("Webcam")
cv2.setMouseCallback("Webcam", mouse_callback)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # Draw red lines
    for p1, p2 in lines:
        cv2.line(
            frame,
            p1,
            p2,
            (0, 0, 255),
            3
        )

    # Draw current line
    if drawing and start_point is not None:
        cv2.line(
            frame,
            start_point,
            current_point,
            (0, 0, 255),
            3
        )

    # Draw first point
    if first_point is not None:
        cv2.circle(
            frame,
            first_point,
            10,
            (0, 0, 255),
            2
        )

    cv2.imshow("Webcam", frame)

    # If shape was closed, STOP webcam
    if shape_closed:
        cv2.waitKey(500)
        break

    # Q also closes webcam
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


# Close webcam completely
cap.release()
cv2.destroyAllWindows()