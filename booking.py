from tkinter import *
root = Tk()
root.geometry("500x400")
root.title("Booking Details")
root.configure(bg='white')




    
Label(root, text="Booking Details",bg="black",fg="white" ,font="ar 15 bold",pady=10).grid(row=0,column=3)

mobile = Label(root, text="Mobile No." ,padx=80,pady=5)
From = Label(root, text="FROM" ,padx=80 ,pady=5)
To = Label(root, text="TO",pady=5)
Fare = Label(root, text="Fare" ,pady=5)
day = Label(root, text="Day" ,pady=5)
time = Label(root, text="Time" ,pady=5)
paymentmode = Label(root, text="Payment Mode" ,pady=5)

mobile.grid(row=1, column=2)
From.grid(row=2, column=2)
To.grid(row=3, column=2)
Fare.grid(row=4, column=2)
day.grid(row=5, column=2)
time.grid(row=6, column=2)
paymentmode.grid(row=7, column=2)


mobilevalue = StringVar
Fromvalue = StringVar
Tovalue = StringVar
Farevalue = StringVar
dayvalue = StringVar
timevalue = StringVar
paymentmodevalue = StringVar
clicked = StringVar()
clicked.set("Pickup")
clicked2 = StringVar()
clicked2.set("Drop")
clicked3 = StringVar()
clicked3.set("choose payment option")

options1 = ["Main Gate ", 
           "ComputerscienceBlock",
           "BH-1",
           "BH-2",
           "BH-3",
           "BH-4",
           "Admission block",
           "Unihospital",
           "UniMall"
]
options2 = ["Main Gate ",
           "ComputerscienceBlock",
           "BH-1",
           "BH-2",
           "BH-3",
           "BH-4",
           "Admission block",
           "Unihospital",
           "UniMall"
]

#creating entry field
mobileentry = Entry(root, textvariable =mobilevalue)
drop = OptionMenu(root, clicked, *options1) 
drop1 = OptionMenu(root, clicked2, *options2)
Fareentry = Entry(root, textvariable =Farevalue)
dayentry = Entry(root, textvariable =dayvalue)
timeentry = Entry(root, textvariable =timevalue)
drop2 = OptionMenu(root, clicked3, "Cash","Onine payment")

#packing entry field
mobileentry.grid(row=1, column=3)
drop.grid(row=2, column=3)
drop1.grid(row=3, column=3)
Fareentry.grid(row=4, column=3)
dayentry.grid(row=5, column=3)
timeentry.grid(row=6, column=3)
drop2.grid(row=7, column=3)

#book button
def confirm():
    messagebox.showinfo(title='Booking status',message="Booking successful.")
b1=Button(command=confirm,text="Confirm Booking",pady=5)

def cancel():
    status=messagebox.askyesno(title="Question",message='Do you want to cancel the booking?')
    if status==True:
        root.destroy()
b2=Button(command=cancel,text="Cancel",pady=5)
b1.grid(row=9,column=3,sticky=W)
b2.grid(row=9,column=3,sticky=E)





root.mainloop()

