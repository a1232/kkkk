import sqlite3
from tkinter import *
from tkinter import messagebox

def chec():
    if en1.get() == "" or en2.get() == "" or en3.get()=="":
        messagebox.showerror("Error!", "Every field must be filled!")
    elif "@gmail.com" not in en1.get():
        messagebox.showerror("Fault!", "The E-mail must contain '@gmail.com'")
    elif tc.get() == 0:
        messagebox.showwarning("Warning!", "Terms & Condition not agreed")
    else:
        try:
            # connecting database
            con = sqlite3.connect('DataEntry.db')
            cur = con.cursor()

            # table
            cur.execute('''CREATE TABLE IF NOT EXISTS data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email VARCHAR(50) UNIQUE,
                password VARCHAR(20),
                cont VARCHAR(10)
            )''')

            # check if email already exists
            email = en1.get()
            contact = en3.get()
            cur.execute('SELECT * FROM data WHERE email=? OR cont=?', (email, contact))
            existing_user = cur.fetchone()

            if existing_user:
                messagebox.showerror("Error!", "Email or Contact number already exists. Please use different credentials.")
            else:
                # inserting data
                password = en2.get()
                cur.execute('INSERT INTO data (email, password, cont) VALUES (?, ?, ?)', (email, password, contact))

                con.commit()
                con.close()
                Kg2.destroy()
                show_login_window()
        except sqlite3.Error as e:
            messagebox.showerror('Error', f'Failed to connect to database. Error: {e}')


def show_login_window():
    import KG_Login
    KG_Login.show_login_window()

def show_pass():
    if Cv.get() == 1:
        en2.config(show='')
    else:
        en2.config(show='*')

def tac():
    return tc.get() == 1

def tcd2():
    import termsandcondition

Kg2 = Tk()
Kg2.title("Kata Garne? Signup")
bckgd = PhotoImage(file='Kgsignup3.png')
bckgd1 = Label(Kg2, image=bckgd).place(x=0, y=0)
Kg2.maxsize(width=1240, height=720)
Kg2.minsize(width=1240, height=720)

Reg_mail = Label(Kg2, text="E-mail:", font=('helvetica', 17, 'bold'), bg="#FFFFFF").place(x=295, y=260)
en1 = Entry(Kg2, width=30, font=("helvetica", 12, 'italic'), bg="#F5EEE6")
en1.place(x=390, y=268)

Reg_pass = Label(Kg2, text="Password:", font=('helvetica', 17, 'bold'), bg="#FFFFFF").place(x=255, y=320)
en2 = Entry(Kg2, width=30, font=("helvetica", 12, 'italic'), bg="#F5EEE6", show='*')
en2.place(x=390, y=328)

Reg_con = Label(Kg2, text="Contact:",font=('helvetica', 17, 'bold'), bg="#FFFFFF").place(x=275, y=380)
en3 = Entry(Kg2, width=30, font=("helvetica", 12, 'italic'), bg="#F5EEE6")
en3.place(x=390, y=388)

Cv = IntVar()
show_p = Checkbutton(Kg2, text="Show Password", width=15, font=("helvetica", 12, 'italic'),command=show_pass, variable=Cv, onvalue=1,bg="#FFFFFF")
show_p.place(x=400, y=430)

tc=IntVar()
termscon= Checkbutton(Kg2,text="I agree to the Terms & Conditions*", width=30, font=("helvetica", 12, 'italic'),command=tac, variable=tc, onvalue=1,bg="#FFFFFF")
termscon.place(x=340, y=460)

U = Button(Kg2, text="Signup", width=25, font=("helvetica", 12, 'italic'), command=chec)
U.place(x=360, y=530)

tcd=IntVar()
tcd1= Button(Kg2,text="Read terms & condition", font=('helvetica',7,'italic'),bg="#FFFFFF",fg="#0A1D56",command=tcd2)
tcd1.place(x=430,y=490)

label = Label(Kg2, text='')
label.pack()

Kg2.mainloop()