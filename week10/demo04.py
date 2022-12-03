from tkinter import *
from tkinter.ttk import *

#### CREATE THE WINDOW ####
window = Tk()
window.title("Demo Combo Box")
window.geometry("400x200")

#### HANDLE EVENTS ####
def cbMovies_clicked(event):
    # get movie name
    movie_name= cbMovies.get()
    # get info
    info = movies[movie_name][0]
    # get IMDB score
    imdb_score = movies[movie_name][1]
    # display info
    lblInfo.config(text='Movie info: ' + str(info))
    # display IMDB score
    lblIMDB.config(text='IMDB score: ' + str(imdb_score))

def btnBuy_clicked():
    n_tickets = int(txtTickets.get())
    payment = 5 * n_tickets
    lblPayment.config(text='Payment: $' + str(payment))

#### CREATE THE WIDGETS ####
# Create a label for movie list
lblMovie = Label(window, text="Select a movie", justify=LEFT)
lblMovie.grid(column=0, row=0, sticky='w')
# Create a combo box for movie list
cbMovies = Combobox(window)
cbMovies.bind("<<ComboboxSelected>>", cbMovies_clicked)
cbMovies['values'] = ["The Shawshank Redemption", 
                      "The Godfather", 
                      "The Godfather: Part II", 
                      "The Dark Knight"]
movies = {'The Shawshank Redemption': ('Directed by  Frank Darabont', 9.2),
          'The Godfather': ('Directed by Francis Ford Coppola', 9.2),
          'The Godfather: Part II': ('Directed by Francis Ford Coppola', 9.0),
          'The Dark Knight': ('Directed by Christopher Nolan', 9.0)}

cbMovies.current(0) # set the selected item
cbMovies.grid(column=1, row=0, sticky='w')

lblInfo = Label(window, text="Movie info")
lblInfo.grid(column=0, row=1, sticky='w')
lblIMDB = Label(window, text="IMDB rating")
lblIMDB.grid(column=0, row=2, sticky='w')

lblTickets = Label(window, text="Number of tickets")
lblTickets.grid(column=0, row=3, sticky='w')
txtTickets = Entry(window, width=10)
txtTickets.grid(column=1, row=3, sticky='w')
btnBuy = Button(window, text="Buy", command=btnBuy_clicked)
btnBuy.grid(column=0, row=4, sticky='w')

lblPayment = Label(window, text="Payment: $0")
lblPayment.grid(column=0, row=5, sticky='w')

#### START THE GUI ####
window.mainloop()