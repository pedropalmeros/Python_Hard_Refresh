import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

#label

my_label = tkinter.Label(text="Im A a Label")
my_label.pack()
