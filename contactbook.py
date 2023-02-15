from tkinter import *
from tkinter import ttk
from views import *
from tkinter import messagebox

#set colors/ color value reference
color1 = "#ffffff"
color2 = "#000000"
color3 = "#EEEEDF"
color4 = "#47473C"
color5 = "#8B8B22"

#set font/font size
font1 = ("Roboto", 20, "bold")
font2 = ("Ivy", 10, "bold")
font3 = ("Ivy", 8, "bold")
font4 = ("Century Gothic", 12, "bold")

#login window layout
window_login = Tk()

height = 230
width = 450
x = (window_login.winfo_screenwidth()//2)-(width//2)
y = (window_login.winfo_screenheight()//2)-(height//2)

window_login.title('Login - Contact Information Book')
window_login.geometry('{}x{}+{}+{}'.format(width, height, x, y))
window_login.resizable(width = False, height = False)
window_login.config(background = color3)

#------------------------------------------------------------------------#
#set contents/widgets of the log in window

#login image
img = PhotoImage(file = 'img_login.png')
lab_img = Label(window_login, image = img, bg = color3)
lab_img.place(x = 20, y = 60)

#login title frame
log_frame = Frame(window_login, width = 250, height = 200, bg = color3)
log_frame.place(x = 160, y = 25)

#login title/heading
lab_heading = Label(log_frame, text = 'Log In', font = font4, fg = color2, bg = color3)
lab_heading.place(x = 100, y = 5)

#log in username label and entry
lab_user = Label(log_frame, text = 'Username:', font = font2, fg = color2, bg = color3)
lab_user.place(x = 10, y = 50)
ent_user = Entry(log_frame, width = 20, fg = color2, bg = color3, font = font2)
ent_user.place(x = 90, y = 50)

#log in password label and entry
lab_code = Label(log_frame, text = 'Password:', font = font2, fg = color2, bg = color3)
lab_code.place(x = 10, y = 90)
ent_code = Entry(log_frame, width = 20, fg = color2, bg = color3, font = font2, show = "*")
ent_code.place(x = 90, y = 90)


#run of login window 
window_login.mainloop()

















# #window/layout
# window = Tk()
# window.title("Contact Book")
# window.geometry('485x450')
# window.configure(background = co0)
# window.resizable(width = False, height = False)

# #Frames/structure
# frame_up = Frame(window, width = 500, height = 50, bg = co2)
# frame_up.grid(row = 0, column = 0, padx = 0, pady = 1)

# frame_down = Frame(window, width = 500, height = 150, bg = co0)
# frame_down.grid(row = 1, column = 0, padx = 0, pady = 1)

# frame_table = Frame(window, width = 500, height = 100, bg = co0, relief = "flat")
# frame_table.grid(row = 2, column = 0, columnspan = 2, padx = 10, pady = 1, sticky = NW)

# #functions
# def show():
#     global tree
#     #header of the table
#     listheader = ['Name', 'Gender', 'Telephone', 'Email']
    
#     demo_list = view()
    
#     tree = ttk.Treeview(frame_table, selectmode = "extended", columns = listheader, show = "headings" )
    
#     #scrollbar
#     vsb = ttk.Scrollbar(frame_table, orient = "vertical", command = tree.yview)
#     hsb = ttk.Scrollbar(frame_table, orient = "horizontal", command = tree.xview)
    
#     tree.configure(yscrollcommand = vsb.set, xscrollcommand = hsb.set)
    
#     tree.grid(column = 0, row = 0, sticky = 'nsew')
#     vsb.grid(column = 1, row = 0, sticky =  'ns')
#     hsb.grid(column = 0, row = 1, sticky = 'ew')
    
#     #tree head
#     tree.heading(0, text = ' Name', anchor = NW)
#     tree.heading(1, text = 'Gender', anchor = NW)
#     tree.heading(2, text = 'Telephone', anchor = NW)
#     tree.heading(3, text = 'Email', anchor = NW)
    
#     #tree columns
#     tree.column(0, width = 120, anchor = NW)
#     tree.column(1, width = 50, anchor = NW)
#     tree.column(2, width = 100, anchor = NW)
#     tree.column(3, width = 180, anchor = NW)
    
#     for item in demo_list:
#         tree.insert ('', 'end', values = item)
       
# show()

# #codings
# #to add
# def insert():
#     Name = e_name.get()
#     Gender = c_gender.get()
#     Telephone = e_telephone.get()
#     Email = e_email.get()
    
#     data = [Name, Gender, Telephone, Email]
    
#     if Name == '' or Gender == '' or Telephone == '' or Email == '':
#         messagebox.showwarning('data', 'Please fill all fields')
    
#     else:
#         add(data)
#         messagebox.showinfo('data', 'Data added successfully.')
        
#         e_name.delete(0, 'end')
#         c_gender.delete(0, 'end')
#         e_telephone.delete(0, 'end')
#         e_email.delete(0, 'end')
        
#         show()

# #to update 
# def to_update():
#     try:
#         tree_data = tree.focus()
#         tree_dictionary = tree.item(tree_data)
#         tree_list = tree_dictionary['values']
        
#         Name = str(tree_list[0])
#         Gender = str(tree_list[1])
#         Telephone = str(tree_list[2])
#         Email = str(tree_list[3])
        
#         e_name.insert (0, Name)
#         c_gender.insert(0, Gender)
#         e_telephone.insert(0, Telephone)
#         e_email.insert(0, Email)
        
#         #to save updated data
#         def confirm():
#             new_name = e_name.get()
#             new_gender = c_gender.get()
#             new_telephone = e_telephone.get()
#             new_email = e_email.get()
            
#             data = [new_telephone, new_name, new_gender, new_telephone, new_email]
            
#             update(data)
            
#             messagebox.showinfo('Success', 'Data updated successfully.')
            
#             e_name.delete(0, 'end')
#             c_gender.delete(0, 'end')
#             e_telephone.delete(0, 'end')
#             e_email.delete(0, 'end')
            
#             for widget in frame_table.winfo_children():
#                 widget.destroy()
                
#             b_confirm.destroy()
            
#             show()
#         b_confirm = Button(frame_down, text = "Confirm", width = 10,  height = 1, bg = co2, fg = co0, font = ('Ivy 8 bold'), command = confirm)
#         b_confirm.place(x = 290, y = 110)
    
#     except IndexError:
#         messagebox.showerror('Error', 'Select one from the table.')

# #to remove
# def to_remove():
#     try:
#         tree_data = tree.focus()
#         tree_dictionary = tree.item(tree_data)
#         tree_list = tree_dictionary['values']
#         tree_telephone = str(tree_list[2])
        
#         remove(tree_telephone)
        
#         messagebox.showinfo('Success', 'Data has been deleted.')
        
#         for widget in frame_table.winfo_children():
#             widget.destroy()
        
#         show()
        
#     except IndexError:
#         messagebox.showerror('Error', 'Select one from the table.')

# #to search
# def to_search():
#     telephone = e_search.get()
    
#     data = search(telephone)
    
#     def delete_command():
#         tree.delete(*tree.get_children())
        
#     delete_command()
    
#     for item in data:
#         tree.insert('', 'end', values = item)
        
#     e_search.delete(0, 'end')
        
# #frame_up style/widgets
# app_name = Label(frame_up, text = "Contactbook", height = 1, font = ('Verdana 17 bold'), bg = co2, fg = co0)
# app_name.place(x = 5, y = 5)

# #frame_down style/widgets
# #name
# l_name = Label(frame_down, text = "Name *", width = 20, height = 1, font = ('Ivy 10'), bg = co0, anchor = NW)
# l_name.place(x = 10, y = 20)    
# e_name = Entry(frame_down, width = 25, justify = "left", highlightthickness = 1, relief = "solid")
# e_name.place(x = 80, y = 20)

# #gender
# l_gender = Label(frame_down, text = "Gender *", width = 20, height = 1, font = ('Ivy 10'), bg = co0, anchor = NW)
# l_gender.place(x = 10, y = 50)
# c_gender = ttk.Combobox(frame_down, width = 27)
# c_gender['values'] = ['', 'F', 'M']
# c_gender.place(x = 80, y = 50)

# #telephone
# l_telephone = Label(frame_down, text = "Telephone*", height = 1, font = ('Ivy 10'), bg = co0, anchor = NW)
# l_telephone.place(x = 10, y = 80)
# e_telephone = Entry(frame_down, width = 25, justify = "left", highlightthickness = 1, relief = "solid")
# e_telephone.place(x = 80, y = 80)

# #email
# l_email = Label(frame_down, text = "Email *", height = 1, font = ('Ivy 10'), bg = co0, anchor = NW)
# l_email.place(x = 10, y = 110)
# e_email = Entry(frame_down, width = 25, justify = "left", highlightthickness = 1, relief = "solid")
# e_email.place(x = 80, y = 110)

# #search button/entry
# b_search = Button(frame_down, text = "Search", height = 1, bg = co2, fg = co0, font = ('Ivy 8 bold'), command = to_search)
# b_search.place(x = 290, y = 20)
# e_search = Entry(frame_down, width = 16, justify = "left", font = ('Ivy', 11), highlightthickness = 1, relief = "solid")
# e_search.place(x = 347, y = 20)

# #view button
# b_view = Button(frame_down, text = "View", width = 10,  height = 1, bg = co2, fg = co0, font = ('Ivy 8 bold'), command = show)
# b_view.place(x = 290, y = 50)

# #add
# b_add = Button(frame_down, text = "Add", width = 10,  height = 1, bg = co2, fg = co0, font = ('Ivy 8 bold'), command = insert)
# b_add.place(x = 400, y = 50)

# #update
# b_update = Button(frame_down, text = "Update", width = 10,  height = 1, bg = co2, fg = co0, font = ('Ivy 8 bold'), command = to_update)
# b_update.place(x = 400, y = 80)

# #delete
# b_delete = Button(frame_down, text = "Delete", width = 10,  height = 1, bg = co2, fg = co0, font = ('Ivy 8 bold'), command = to_remove)
# b_delete.place(x = 400, y = 110)

# window.mainloop()