from tkinter import*
from tkinter import messagebox
import sqlite3

vl= Tk()
vl.title("Kata Garne? Venue Login")
Backgrnd=PhotoImage(file='Templet8.png')
Backgrnd1=Label(vl,image=Backgrnd).place(x=0,y=0)
vl.maxsize(width=1240, height=720)
vl.minsize(width=1240,height=720)

def verify_venue():
    email = Entry1.get()
    password = Entry2.get()
    try:
        conI = sqlite3.connect("Venuedata.db")
        curI = conI.cursor()
        curI.execute("CREATE TABLE IF NOT EXISTS data(email TEXT, password TEXT)")
        curI.execute("SELECT email FROM data WHERE email=?", [email])
        result = curI.fetchone()
        if result:
            stored_password = curI.execute("SELECT password FROM data WHERE password=?", [password]).fetchone()
            if stored_password and stored_password[0] == password:
                messagebox.showinfo("Verification", "Login successful!")
                vl.destroy()
                import new
            else:
                messagebox.showerror("Verification", "Invalid Password")
        else:
            messagebox.showerror("Verification", "Invalid email")
        conI.commit()
        conI.close()
    except Exception as e:
        messagebox.showerror("Verification", f"Error: {e}")

v_mail= Label(vl, text="E-mail:",font=('helvetica',18,'bold'),bg='#f8f5ee')
v_mail.place(x=780,y=200)
Entry1=Entry(vl,width=25,font=("helvetica",12,'italic'))
Entry1.place(x=870,y=208)
v_password= Label(vl,text="Password:",font=('helvetica',18,'bold'),bg='#f8f5ee')
v_password.place(x=740,y=270)
Entry2= Entry(vl,width=25,font=("helvetica",12,'italic'),show="*")
Entry2.place(x=870,y=278)
def pasword_sh():
    if pH.get()==1:
        Entry2.config(show="")
    else:
        Entry2.config(show="*")
pH=IntVar()
showPH=Checkbutton(vl,text="Show Password",width=15, font=("helvetica", 12, 'italic'),command=pasword_sh, variable=pH, onvalue=1 ,bg="#f8f5ee")
showPH.place(x=900,y=330)
Update=Button(vl,text="Login",width=25,font=('helvetica',10,'bold'),command=verify_venue).place(x=870,y=380)

war=Label(vl,text="By Logging in into 'KATA GARNE?' you agree that \n You and only you are responsible for changes made to the account",font=('helvetica', 10, 'bold'), bg="#f8f5ee").place(x=750, y=450)




vl.mainloop()