import cv2
import numpy as np
import pyautogui

# Open camera
cap = cv2.VideoCapture(0)

while True:
    # Read each frame from the camera
    ret, frame = cap.read()

    # Convert the frame to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the range of skin color in HSV
    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)

    # Extract skin color using the defined range
    mask = cv2.inRange(hsv, lower_skin, upper_skin)

    # Blur the mask to reduce noise
    mask = cv2.GaussianBlur(mask, (5, 5), 0)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Check if any contours are found
    if contours:
        # Find the contour with the maximum area
        max_contour = max(contours, key=cv2.contourArea)

        # Find the centroid of the contour
        M = cv2.moments(max_contour)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])

            # Move the mouse to the centroid position
            screenWidth, screenHeight = pyautogui.size()
            pyautogui.moveTo(cx * screenWidth / 640, cy * screenHeight / 480)

    # Display the frame
    cv2.imshow("Gesture Control", frame)

    # Break the loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the OpenCV window
cap.release()
cv2.destroyAllWindows()