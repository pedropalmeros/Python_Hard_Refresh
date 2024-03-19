from tkinter import * 
import pandas as pd
import random
from tkinter import messagebox

card_iloc = 0
language_data = pd.DataFrame()

BACKGROUND_COLOR = "#B1DDC6"
#-------------------------------------------------------------------------
#                   GETTING THE DATA FROM THE CSV
#-------------------------------------------------------------------------
def create_next_card():
        global language_data, flip_timer
        global card_iloc
        window.after_cancel(flip_timer)
        card_iloc = random.randint(0,language_data.shape[0])
        canvas.itemconfig(card_title, text='French',fill="black")
        canvas.itemconfig(card_word, text=language_data.iloc[card_iloc]["French"],fill="black")
        canvas.itemconfig(card_background, image=card_front_image)
        flip_timer = window.after(3000, func=flip_card)




#-------------------------------------------------------------------------
#                   FLIP THE CARDS
#-------------------------------------------------------------------------

def flip_card():
    global language_data
    global card_iloc

    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=language_data.iloc[card_iloc]["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_image)


#-------------------------------------------------------------------------
#                   CREATE DATA FRAME
#-------------------------------------------------------------------------
def get_csv_data():
    try:
        global language_data 
        language_data = pd.read_csv('./data/french_words.csv')
    except FileNotFoundError:
        messagebox.showinfo(title="File Error", message="File 'french_words' is missing")
    else: 
        pass




window = Tk() 
window.title("Learning French")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)

card_front_image = PhotoImage(file=".\\images\\card_front.png")
card_back_image = PhotoImage(file=".\\images\\card_back.png")

card_background = canvas.create_image(400, 263, image=card_front_image )
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan =2 )

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=create_next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="./images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=create_next_card)
known_button.grid(row=1, column=1)

get_csv_data()
create_next_card()

window.mainloop()
