from tkinter import *
########## CREATE WINDOW ##########
window = Tk() 
window.geometry('300x200')
window.title('Test')

########## HANDLE EVENTS ##########
def btnHello_clicked():
    name = txtName.get()    # get the text from the text box txtName
    lblHello.configure(text='Hello ' + name) # set the text of lblHello

########## CREATE WIDGETS ##########
# create a label
lblHello = Label(window, text='Hello')
lblHello.grid(column=0, row=1, rowspan=2)

# create a button
btnHello = Button(window, text='Say hello', command=btnHello_clicked)
btnHello.grid(column=1, row=0)

# create a text box
txtName = Entry(window, width=10)
txtName.grid(column=0, row=0)

########## START GUI ##########
window.mainloop()