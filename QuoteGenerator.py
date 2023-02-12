from tkinter import *

import random

root = Tk()
root.title("Quote Generator @Tinu") 
root.geometry("500x400")

q = ["Life is what happens when you're busy making other plans.","The future belongs to those who believe in the beauty of their dreams.","Whoever is happy will make others happy too.","Tell me and I forget. Teach me and I remember. Involve me and I learn.","Always remember that you are absolutely unique. Just like everyone else.","The way to get started is to quit talking and begin doing.","The greatest glory in living lies not in never falling, but in rising every time we fall.","Sometimes later becomes never.", "Dream it. Do it.", "Never take the easy way out", "Learn as if you will live forever, live like you will die tomorrow.", "When you change your thoughts, remember to also change your world.", "It is better to fail in originality than to succeed in imitation.", "The road to success and the road to failure are almost exactly the same.", "Don’t let yesterday take up too much of today.", "Setting goals is the first step in turning the invisible into the visible.", "We don’t just sit around and wait for other people. We just make, and we do.", "He who conquers himself is the mightiest warrior.", "One man with courage makes a majority.", "The successful man will profit from his mistakes and try again in a different way.", "The most difficult thing is the decision to act, the rest is merely tenacity."]

lbl = Label(root, text="This is a quote generator.\n Press the button to generate new quotes.\n Maximize this window for optimum experience.", font=('', 12))
lbl.place(relx=0.5, rely=0.1, anchor=N)

quote = Label(root, text="Work before glory", font=('', 22))
quote.place(relx=0.5, rely=0.5, anchor=CENTER)


def generate():
    quote.configure(text=random.choice(q))

 
submit = Button(root, text="Generate", bg="black", fg="white", command=generate, height=3, width=7)
submit.place(relx=0.5, rely=0.9, anchor=S)

root.mainloop()
