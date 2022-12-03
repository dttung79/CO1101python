from tkinter import *
from tkinter import messagebox as msgbox
########## CREATE WINDOW ##########
window = Tk()
window.geometry('300x200')
window.title('Arithmetic operations')

########## HANDLE EVENTS ##########
def btnAdd_clicked():
    perform('+')
    
def btnSub_clicked():
    perform('-')

def btnMul_clicked():
    perform('*')

def btnDiv_clicked():
    try:
        perform('/')
    except ZeroDivisionError:
        msgbox.showerror('Error', 'Cannot divide by zero')

def perform(operation):
    a = int(txtA.get()) if txtA.get() != '' else 0
    b = int(txtB.get()) if txtB.get() != '' else 0
    if operation == '+':
        result = a + b
    elif operation == '-':
        result = a - b
    elif operation == '*':
        result = a * b
    elif operation == '/':
        result = a / b
    # set the text of txtResult
    txtResult.delete(0, END)            # clear current text
    txtResult.insert(0, str(result))    # insert new text
########## CREATE WIDGETS ##########
# create a label for number a
lblA = Label(window, text='a')
lblA.grid(column=0, row=0)
# create a text box for number a
txtA = Entry(window, width=10)
txtA.grid(column=1, row=0, columnspan=4)

# create a label for number b
lblB = Label(window, text='b')
lblB.grid(column=0, row=1)
# create a text box for number b
txtB = Entry(window, width=10)
txtB.grid(column=1, row=1, columnspan=4)

# label & text for the result
lblResult = Label(window, text='a+b')
lblResult.grid(column=0, row=3)
# textResult should be read-only
txtResult = Entry(window, width=10)
txtResult.grid(column=1, row=3, columnspan=4)

# create 4 buttons for 4 arithmetic operations
btnAdd = Button(window, text='+', command=btnAdd_clicked)
btnAdd.grid(column=1, row=2)
btnSub = Button(window, text='-', command=btnSub_clicked)
btnSub.grid(column=2, row=2)
btnMul = Button(window, text='x', command=btnMul_clicked)
btnMul.grid(column=3, row=2)
btnDiv = Button(window, text='/', command=btnDiv_clicked)
btnDiv.grid(column=4, row=2)

########## START GUI ##########
window.mainloop()
