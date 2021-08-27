from tkinter import *
from tkinter import ttk
import random
from sortAlgos import bubble_sort, merge_sort

# Global Variables
data = []

# Functions
def display_data(data, color_list):
    """
    This function will clear the old data from canvas and display the new data
    data is normalized to allow bars to be sized relative to one another

    :param data: list that contains the generated data
    :param color_list: list of colors. green indicates the data point being checked
    :return: None
    """
    data_canvas.delete("all")
    canvas_width = 600
    canvas_height = 380
    # Calculate the width of the bars
    bar_width = canvas_width / (len(data) + 1)
    # Offset and Spacing will space out each bar from border and one another
    offset = 30
    spacing = 10
    # Must normalize the data so bars are sized relative to one another
    normalized_data = [i/max(data) for i in data]
    for i, ht in enumerate(normalized_data):
        x0 = i * bar_width + offset + spacing
        y0 = canvas_height - ht * 340  # Multiplied by 340 to allow 40 pixels above the largest bar
        x1 = (i+1) * bar_width + offset
        y1 = canvas_height
        data_canvas.create_rectangle(x0, y0, x1, y1, fill=color_list[i])
        data_canvas.create_text(x0 + 2, y0, anchor=SW, text=str(data[i]))

    root.update()

def generate():
    """
    This function is called to generate a random set of data
    The function gets the values put in by the user scales/sliders

    :return: None
    """
    global data
    data = []
    # Generate a random data set
    for _ in range(usr_size.get()):
        data.append(random.randrange(usr_min.get(), usr_max.get()+1))
    display_data(data, ['red' for x in range(len(data))])

# Setup of root window
root = Tk()
root.title("Sorting Visualizer")
root.maxsize(900, 600)
root.config(bg="black")

def start_sort():
    """
    Function determines which sort to use, then calls the function

    :return: None
    """
    global data
    if algo_box.get() == "Bubble Sort":
        bubble_sort(data, display_data, speed_scale.get())
    elif algo_box.get() == "Merge Sort":
        merge_sort(data, display_data, speed_scale.get())

#######
# UI
#######
# Setup Frame for UI

UI_frame = Frame(root, width=600, height=200, bg="grey")
UI_frame.grid(row=0, column=0, padx=10, pady=5)

user_algo = StringVar()  # StringVar for saving the sort algo to use

# Label amd Combobox to use dropdown menu selector for algorithm
algo_selection = Label(UI_frame, text="Select Algorithm: ", bg="grey")
algo_selection.grid(row=0, column=0, padx=5, pady=5, sticky=W)
algo_box = ttk.Combobox(UI_frame, textvariable=user_algo, width="10", values=["Bubble Sort", "Merge Sort"])
algo_box.grid(row=0, column=1, padx=5, pady=5)
algo_box.current(0)

# Speed Scale
speed_scale = Scale(UI_frame, from_=0.1, to=2.0, length=200, digits=2, resolution=0.2, orient=HORIZONTAL,
                    label="Speed")
speed_scale.grid(row=1, column=0, padx=5, pady=5)

# Size Scale
usr_size = Scale(UI_frame, from_=3, to=30, resolution=1, length=150, orient=HORIZONTAL, label="Size of Data")
usr_size.grid(row=1, column=1, padx=5, pady=5, sticky=W)

# Min Value Scale
usr_min = Scale(UI_frame, from_=1, to=30, resolution=1, length=150, orient=HORIZONTAL, label="Min Value")
usr_min.grid(row=1, column=2, padx=5, pady=5, sticky=W)

# Max Value Scale
usr_max = Scale(UI_frame, from_=1, to=30, resolution=1, length=150, orient=HORIZONTAL, label="Max Value")
usr_max.grid(row=1, column=3, padx=5, pady=5, sticky=W)

# Generate Button
gen_button = Button(UI_frame, text="Generate", command=generate, bg='white')
gen_button.grid(row=2, column=0, padx=5, pady=5)

# Start Button
start = Button(UI_frame, text="Start", command=start_sort)
start.grid(row=2, column=1, padx=5, pady=5)


########
# CANVAS
########
# Setup canvas for displaying data

data_canvas = Canvas(root, width=600, height=380, bg="white")
data_canvas.grid(row=1, column=0, padx=10, pady=5)

root.mainloop()
