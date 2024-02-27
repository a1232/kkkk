from tkinter import*

portal = Tk() 
bckgd = PhotoImage(file='Portal1.png')
bckgd1 = Label(portal, image=bckgd).place(x=0, y=0)
portal.maxsize(width=1240, height=720)
portal.minsize(width=1240, height=720)

def u_olduser():
    portal.destroy()
    import KG_Login
def u_newuser():
    portal.destroy()
    import KG_Signup
def u_venue():
    portal.destroy()
    import Venue_Signup
def u_regvenue():
    portal.destroy()
    import KG_venuelog


u_old=Button(portal,text="Registered user",width=20,font=('helvetica',10,'bold'),command=u_olduser).place(x=100,y=520)
u_new=Button(portal,text="New User",width=20,font=('helvetica',10,'bold'),command=u_newuser).place(x=985,y=510)
u_venue=Button(portal,text="Venue",width=20,font=('helvetica',10,'bold'),command=u_venue).place(x=533,y=500)
u_rvenue=Button(portal,text="Registered Venue",width=20,font=('helvetica',10,'bold'),command=u_regvenue).place(x=533,y=535)

portal.mainloop()