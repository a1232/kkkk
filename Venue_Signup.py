import sqlite3
from tkinter import *
from tkinter import messagebox

vs = Tk()
vs.title("Venue Signup")
bckgd = PhotoImage(file='venue_portal.png')
bckgd1 = Label(vs, image=bckgd).place(x=0, y=0)
vs.maxsize(width=1240, height=720)
vs.minsize(width=1240, height=720)
def tvs():
    return tv.get() == 1
def tvs2():
    import termsandcondition2

def go():
    if oe1.get() == "" or oe2.get() == "" or oe3.get()=="" or oe4.get()=="" or oe5.get()=="":
        messagebox.showerror("Error!", "Every field must be filled!")
    elif "@gmail.com" not in oe1.get():
        messagebox.showerror("Fault!", "The E-mail must contain '@gmail.com'")
    elif tv.get() == 0:
        messagebox.showwarning("Warning!", "Terms & Condition not agreed")
    elif len(oe3.get())!=10:
        messagebox.showerror("Warning!", "Please enter a valid Phone Number (10 digits)")
    elif not oe4.get().isdigit():
     messagebox.showerror("Warning!", "Pan number must be a integer only")
    else:
        try:
            # connecting database
            con = sqlite3.connect('Venuedata.db')
            cur = con.cursor()

            # table
            cur.execute('''CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY AUTOINCREMENT, email VARCHAR(50), password VARCHAR(20), cont VARCHAR(10), pan VARCHAR(20), location VARCHAR(20) )''')

            # check if email already exists
            location=oe5.get()
            email = oe1.get()
            contact = oe3.get()
            pan = oe4.get()
            cur.execute('SELECT * FROM data WHERE email=? OR cont=? OR pan=?', (email, contact,pan))
            existing_user = cur.fetchone()

            if existing_user:
                messagebox.showerror("Error!", "Email or Contact or Pan number already exists. Please use different credentials.")
            else:
                # inserting data
                password = oe2.get()
                cur.execute('INSERT INTO data (email, password, cont, pan, location) VALUES (?, ?, ?, ?, ?)', (email, password, contact, pan, location))

                con.commit()
                con.close()
                vs.destroy()
                show_login_window()
        except sqlite3.Error as e:
            messagebox.showerror('Error', f'Failed to connect to database. Error: {e}')

def show_login_window():
    import KG_venuelog
    KG_venuelog.show_login_window()




owner_mail = Label(vs, text="E-mail:", font=('helvetica', 17, 'bold'), bg="#FFFFFF").place(x=180, y=190)
oe1 = Entry(vs, width=30, font=("helvetica", 12, 'italic'), bg="#F5EEE6")
oe1.place(x=270, y=198)
owner_pass = Label(vs, text="Password:", font=('helvetica', 17, 'bold'), bg="#FFFFFF").place(x=140, y=260)
oe2 = Entry(vs, width=30, font=("helvetica", 12, 'italic'), bg="#F5EEE6")
oe2.place(x=270, y=268)
owner_contact = Label(vs, text="Contact:", font=('helvetica', 17, 'bold'), bg="#FFFFFF").place(x=160, y=330)
oe3 = Entry(vs, width=30, font=("helvetica", 12, 'italic'), bg="#F5EEE6")
oe3.place(x=270, y=338)
owner_pan = Label(vs, text="Pan no.:", font=('helvetica', 17, 'bold'), bg="#FFFFFF").place(x=160, y=400)
oe4 = Entry(vs, width=30, font=("helvetica", 12, 'italic'), bg="#F5EEE6")
oe4.place(x=270, y=408)
owner_location= Label(vs, text="Location:", font=('helvetica', 17, 'bold'), bg="#FFFFFF").place(x=150, y=470)
oe5 = Entry(vs, width=30, font=("helvetica", 12, 'italic'), bg="#F5EEE6")
oe5.place(x=270, y=478)
t_v=Button(vs, text="Terms & Condition", width=25, font=("helvetica", 9, 'italic'),bg="#FFFFFF",fg="#0A1D56",command=tvs2)
t_v.place(x=310, y=520)
tv=IntVar()
termscon= Checkbutton(vs,text="I agree to the Terms & Conditions*", width=30, font=("helvetica", 9, 'italic'), variable=tv, onvalue=1,bg="#FFFFFF",command=tvs)
termscon.place(x=280, y=550)
si_v=Button(vs, text="Signup", width=25, font=("helvetica", 12, 'italic'),command=go)
si_v.place(x=280, y=575)










vs.mainloop()