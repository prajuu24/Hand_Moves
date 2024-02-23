# Gesture_Controller.py

def calculate_gesture_action_percentages():
    # Replace this with your actual logic to calculate percentages
    left_click_percentage = 100
    right_click_percentage = 99
    scroll_up_percentage = 95
    scroll_down_percentage = 100
    no_action_percentage = 100

    return [left_click_percentage, right_click_percentage,
            scroll_up_percentage, scroll_down_percentage, no_action_percentage]

if __name__ == "__main__":
    from accuracy import plot_gesture_action_bar_graph
    plot_gesture_action_bar_graph()
