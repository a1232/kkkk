import tkinter as tk
from tkinter import Label, Button, Entry
from datetime import datetime
from tkcalendar import Calendar
import subprocess

def update_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    time_label.config(text="Current Time: " + current_time)
    rs.after(1000, update_time) 

def grad_date():
    selected_date = cal.get_date()
    date_label.config(text="Selected Date is: " + selected_date)
    entry_value = venue_entry.get()  # Retrieve value from Entry widget
    write_to_file(entry_value)  # Write the value to file
    subprocess.run(["python", "DATE.py"])

def write_to_file(selected_value):
    with open("", "w") as file:  # Writing to a file named selected_date.txt
        file.write(selected_value)

rs = tk.Tk()
rs.title("Bill")
rs.geometry("400x400")

# Add Calendar
cal = Calendar(rs, selectmode='day', year=2020, month=5, day=22)
cal.pack(pady=20)

# Create Entry widget
venue_entry = Entry(rs)
venue_entry.pack(pady=5)

# Add Button and Label for selected date
Button(rs, text="Get Date", command=grad_date).pack(pady=5)
date_label = Label(rs, text="")
date_label.pack(pady=10)

# Add label for current time
time_label = Label(rs, font=("Helvetica", 12))
time_label.pack(pady=10)

# Initial update of the time label
update_time()

rs.maxsize(width=1240, height=720)
rs.minsize(width=720, height=720)

rs.mainloop()
