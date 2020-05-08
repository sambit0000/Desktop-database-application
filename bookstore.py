# Importing the required libraries
from tkinter import *
import bookstore1

# Function to get the row when it is selected
def get_selected_row(event):
    try:
        global selected_tuple
        # To get the index of the row
        index = lb1.curselection()[0]
        # Get the exact row item of the given index
        selected_tuple = lb1.get(index)
        e1.delete(0,END)
        # Insert the title in entry box
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        # Insert the author in entry box
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        # Insert the year in entry box
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        # Insert the isbn in entry box
        e4.insert(END,selected_tuple[4])
    # Error handling when the Listbox is empty
    except IndexError:
        pass
        
# Function to view all the books
def view_command():
    lb1.delete(0,END)
    for row in bookstore1.view():
        lb1.insert(END,row)

# Function to search for a specific book
def search_command():
    lb1.delete(0,END)
    for row in bookstore1.search(e1_value.get(),e2_value.get(),e3_value.get(),e4_value.get()):
        lb1.insert(END,row)

# Function to add a new book
def add_command():
    bookstore1.insert(e1_value.get(),e2_value.get(),e3_value.get(),e4_value.get())
    lb1.delete(0,END)
    lb1.insert(END,(e1_value.get(),e2_value.get(),e3_value.get(),e4_value.get()))

# Function to delete a book
def delete_command():
    bookstore1.delete(selected_tuple[0])

# Function to update a book
def update_command():
    bookstore1.update(selected_tuple[0],e1_value.get(),e2_value.get(),e3_value.get(),e4_value.get())

# Basic GUI architecture    
window = Tk()
window.wm_title("BookStore")
b1 = Button(window, text='View all',width=15,command = view_command)
b1.grid(row=2,column=3)

b2 = Button(window, text='Search entry',width=15,command = search_command)
b2.grid(row=3,column=3)

b3 = Button(window, text='Add entry',width=15,command = add_command)
b3.grid(row=4,column=3)

b4 = Button(window, text='Update',width=15,command = update_command)
b4.grid(row=5,column=3)

b5 = Button(window, text='Delete',width=15,command = delete_command)
b5.grid(row=6,column=3)

b6 = Button(window, text='Close',width=15,command = window.destroy)
b6.grid(row=7,column=3)

e1_value = StringVar()
e1 = Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

e2_value = StringVar()
e2 = Entry(window,textvariable=e2_value)
e2.grid(row=1,column=1)

e3_value = StringVar()
e3 = Entry(window,textvariable=e3_value)
e3.grid(row=0,column=3)

e4_value = StringVar()
e4 = Entry(window,textvariable=e4_value)
e4.grid(row=1,column=3)

l1 = Label(window, text="Title")
l1.grid(row=0,column=0)

l2 = Label(window, text="Author")
l2.grid(row=1,column=0)

l3 = Label(window, text="Year")
l3.grid(row=0,column=2)

l4 = Label(window, text="ISBN")
l4.grid(row=1,column=2)

# Creating a Listbox
lb1=Listbox(window,height=10,width=60)
lb1.grid(row=2,column=0,rowspan=6,columnspan=2)

# Creating a scrollbar
s1 = Scrollbar(window)
s1.grid(row=2,column=2,rowspan=6)

# Connecting scrollbar with Listbox
lb1.configure(yscrollcommand=s1.set)
s1.configure(command=lb1.yview)

# Feature to select a row in Listbox
lb1.bind('<<ListboxSelect>>',get_selected_row)

window.mainloop()
