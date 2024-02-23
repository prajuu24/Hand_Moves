import time
import pyautogui
from pynput.mouse import Listener

# Constants for screen resolution (adjust based on your screen)
SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()

# Initialize variables for accuracy calculation
total_distance = 0
total_frames = 0

# Function to calculate Euclidean distance
def calculate_distance(actual_position, predicted_position):
    return ((actual_position[0] - predicted_position[0]) ** 2 + (actual_position[1] - predicted_position[1]) ** 2) ** 0.5

# Mouse action callback
def on_move(x, y, dx, dy):
    global total_distance
    global total_frames

    # Predicted position based on screen resolution
    predicted_position = (x * SCREEN_WIDTH / 1920, y * SCREEN_HEIGHT / 1080)

    # Calculate distance and update variables
    distance = calculate_distance((x, y), predicted_position)
    total_distance += distance
    total_frames += 1

# Mouse click callback
def on_click(x, y, button, pressed):
    if pressed:
        if button == 'Button.left':
            print("Left Click")
            pyautogui.click(x, y)
        elif button == 'Button.right':
            print("Right Click")
            pyautogui.rightClick(x, y)

# Mouse scroll callback
def on_scroll(x, y, dx, dy):
    if dy > 0:
        print("Scroll Up")
        pyautogui.scroll(1)
    else:
        print("Scroll Down")
        pyautogui.scroll(-1)

# Set up the mouse listener
with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    try:
        listener.join()
    except KeyboardInterrupt:
        pass

# Calculate and print the average accuracy
if total_frames > 0:
    average_accuracy = total_distance / total_frames
    print("Average Accuracy:", average_accuracy)