# Gesture_Controller.py
import matplotlib.pyplot as plt
from acc_tracker import calculate_gesture_action_percentages

def plot_gesture_action_bar_graph(): 
    action_labels = ['Left Click', 'Right Click', 'Scroll Up', 'Scroll Down', 'No Action']
    action_percentages = calculate_gesture_action_percentages()

    fig, ax = plt.subplots()
    bars = ax.bar(action_labels, action_percentages, color='blue') 

    ax.set_ylabel('Percentage (%)')
    ax.set_title('Gesture Controller Actions')

    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}%', xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3), textcoords="offset points",
                    ha='center', va='bottom')

    plt.show()

if __name__ == "__main__":
    plot_gesture_action_bar_graph()
