import tkinter as tk

# Create the main application window
root = tk.Tk()

# Set the title of the window
root.title("Hello Tkinter")

# Set the size of the window
root.geometry("400x300")

# Create a label widget
label = tk.Label(root, text="Welcome to Tkinter!")
label.pack(pady=20)

# Create a button widget
button = tk.Button(root, text="Click me!", command=lambda: print("Button clicked"))
button.pack()

# Start the Tkinter event loop
root.mainloop()
