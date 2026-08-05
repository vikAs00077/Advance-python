import tkinter as tk

# Create window
root = tk.Tk()
root.title("Draw Rectangle Using Mouse")

# Create canvas
canvas = tk.Canvas(root, width=600, height=400, bg="white")
canvas.pack()

# Variables
start_x = start_y = 0
rectangle = None


# Mouse button pressed
def mouse_down(event):
    global start_x, start_y, rectangle

    start_x = event.x
    start_y = event.y

    # Create a rectangle starting point
    rectangle = canvas.create_rectangle(
        start_x, start_y, start_x, start_y,
        outline="blue",
        width=3
    )


# Mouse movement
def mouse_move(event):
    global rectangle

    if rectangle:
        # Update rectangle size
        canvas.coords(
            rectangle,
            start_x,
            start_y,
            event.x,
            event.y
        )


# Mouse button released
def mouse_up(event):
    global rectangle
    rectangle = None


# Bind mouse events
canvas.bind("<Button-1>", mouse_down)
canvas.bind("<B1-Motion>", mouse_move)
canvas.bind("<ButtonRelease-1>", mouse_up)

# Run program
root.mainloop()