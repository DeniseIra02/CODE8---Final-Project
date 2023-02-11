from tkinter import *
from tkinter import ttk

#colors
co0 = "#ffffff"
co1 = "#000000"
co2 = "#4456F0"

#window/layout
window = Tk()
window.title("Contact Book")
window.geometry('485x450')
window.configure(background = co0)
window.resizable(width = False, height = False)

#Frames/structure
frame_up = Frame(window, width = 500, height = 50, bg = co2)
frame_up.grid(row = 0, column = 0, padx = 0, pady = 1)

frame_down = Frame(window, width = 500, height = 150, bg = co0)
frame_down.grid(row = 1, column = 0, padx = 0, pady = 1)

frame_table = Frame(window, width = 500, height = 100, bg = co2)
frame_table.grid(row = 2, column = 0, columnspan = 2, padx = 0, pady = 1)

#frame_up style/widgets
app_name = Label(frame_up, text = "Contactbook", height = 1, font = ('Ivy 17 bold'), bg = co2, fg = co0)
app_name.place(x = 5, y = 5)

window.mainloop()