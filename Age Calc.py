from tkinter import *
import datetime

root = Tk()
root.title("Age Calculator App")
root.geometry("400x400")

frame = Frame(master = root, height = 200, width = 360, bg = "#8ea5ba")

l1 = Label(frame, text = "Name:", bg = "#244d71", fg = "white", width = 12)
l2 = Label(frame, text = "Year:", bg = "#315f88", fg = "white", width = 12)
l3 = Label(frame, text = "Month:", bg = "#4a7499", fg = "white", width = 12)
l4 = Label(frame, text = "Date:", bg = "#5e85a7", fg = "white", width = 12)

name_ent = Entry(frame)
year_ent = Entry(frame)
month_ent = Entry(frame)
date_ent = Entry(frame)

def calculate():
    
    name = name_ent.get()
    year = int(year_ent.get())
    today = datetime.date.today()
    age = today.year - year
    
    greet = "Hey!"+name
    message = "\nYour Age is: "+str(age)
    
    textbox.insert(END, greet)
    textbox.insert(END, message)
    
textbox = Text(bg = "#dbe9f5", fg = "black")
btn = Button(text = "Calculate", command = calculate, bg = "#124571", fg = "white")

frame.place(x = 20, y = 0)
l1.place(x = 20, y = 20)
name_ent.place(x = 150, y = 20)
l2.place(x = 20, y = 50)
year_ent.place(x = 150, y = 50)
l3.place(x = 20, y = 80)
month_ent.place(x = 150, y = 80)
l4.place(x = 20, y = 110)
date_ent.place(x = 150, y = 110)
btn.place(x = 160, y = 210)
textbox.place(y = 250)

root.mainloop()



    