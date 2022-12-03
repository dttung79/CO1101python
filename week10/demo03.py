from tkinter import *

########## CREATE WINDOW ##########
window = Tk()
window.geometry('300x200')
window.title('Demo checkboxes')

########## HANDLE EVENTS ##########
def chkEnglish_clicked():
    calculate_payment()

def chkFrench_clicked():
    calculate_payment()

def calculate_payment():
    payment = 0
    if english_selected.get() == True:
        payment += 200
    if french_selected.get() == True:
        payment += 300
    if student_type.get() == 1:     # old student
        payment -= payment * 0.1    # 10% discount

    lblPayment.configure(text='Payment: $' + str(payment))

def radStudentType_clicked():
    calculate_payment()

########## CREATE WIDGETS ##########
lblLanguages = Label(window, text='Select language courses')
lblLanguages.grid(column=0, row=0)

english_selected = BooleanVar()
english_selected.set(False)
chkEnglish = Checkbutton(window, text='English ($200)', \
                        var=english_selected, command=chkEnglish_clicked)
chkEnglish.grid(column=0, row=1)

french_selected = BooleanVar()
french_selected.set(False)
chkFrench = Checkbutton(window, text='French ($300)', \
                        var=french_selected, command=chkFrench_clicked)
chkFrench.grid(column=0, row=2)

lblStudentType = Label(window, text='Select student type')
lblStudentType.grid(column=0, row=3)

student_type = IntVar()
student_type.set(0)

radNewStudent = Radiobutton(window, text='New student', variable=student_type, value=0, \
                            command=radStudentType_clicked)
radNewStudent.grid(column=0, row=4)

radOldStudent = Radiobutton(window, text='Old student (-10%)', variable=student_type, value=1, \
                            command=radStudentType_clicked)
radOldStudent.grid(column=0, row=5)

lblPayment = Label(window, text='Payment: $0')
lblPayment.grid(column=0, row=6)

window.mainloop()