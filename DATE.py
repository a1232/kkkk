from tkinter import *
from tkinter import messagebox
from payment import grad_date
from tkcalendar import Calendar
from payment import rs

import tkinter as tk



def create_tkinter_window(rs=tk.Tk):
    rs = tk.Tk(grad_date)
    
    rs.mainloop()

# Call the function to create a Tkinter window
create_tkinter_window()

# Create the main window
root = tk.Tk()
root.title("Venue Input")

# Load the image
image_path = "venue_portal.png"
image = tk.PhotoImage(file=image_path)

# Create a Canvas widget
canvas = tk.Canvas(root, width=image.width(), height=image.height())
canvas.pack()

# Display the image on the canvas
canvas.create_image(0, 0, anchor=tk.NW, image=image)

#Create an Entry widget
venue_entry = tk.Entry(root)
venue_entry.place(relx=0.5, rely=0.5, anchor=tk.CENTER).get(grad_date)

# Create a Button for submitting the input
# submit_button = tk.Button(root, text="Submit", command=submit)
# submit_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

# Run the Tkinter event loop
root.mainloop()
