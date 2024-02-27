from tkinter import*

trscon = Tk()

trscon.configure(bg="#F5EEE6")
trscon.maxsize(width=1240, height=720)
trscon.minsize(width=1240, height=720)

trs=Label(trscon,text="TERMS & CONDITIONS:", font=('helvetica', 35, 'bold'), bg="#F5EEE6").place(x=360, y=70)
trs2=Label(trscon,text="By checking the Terms & Condition I agree to:",  font=('helvetica', 11, 'bold'), bg="#F5EEE6").place(x=450, y=190)
trs3=Label(trscon,text="1. I understand and agree to share my details with the app. \n 2. I understand and allow developers to delete my data in case of suspicious activites. \n 3. I understand and agree to go through legal actions in case of any inappropriate behavious. \n 4. I understand and agree to not be refunded in case of change of mind."
           ,  font=('helvetica', 10, 'bold'), bg="#F5EEE6").place(x=320, y=250)




trscon.mainloop()