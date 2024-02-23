import time
import pyautogui

# Constants for screen resolution (adjust based on your screen)
SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()

# Initialize variables for accuracy calculation
total_distance = 0
total_frames = 0

# Function to calculate Euclidean distance
def calculate_distance(actual_position, predicted_position):
    return ((actual_position[0] - predicted_position[0]) ** 2 + (actual_position[1] - predicted_position[1]) ** 2) ** 0.5

# Store the initial mouse position
initial_mouse_position = pyautogui.position()

try:
    while True:
        # Get the current mouse position
        current_mouse_position = pyautogui.position()

        # Calculate distance and update variables
        distance = calculate_distance(initial_mouse_position, current_mouse_position)
        total_distance += distance
        total_frames += 1

        # Update the initial mouse position for the next iteration
        initial_mouse_position = current_mouse_position

        # Add a delay to control the loop frequency
        time.sleep(0.1)  # Adjust as needed

except KeyboardInterrupt:
    pass

# Calculate and print the average accuracy
if total_frames > 0:
    average_accuracy = total_distance / total_frames
    print("Average Accuracy:", average_accuracy)