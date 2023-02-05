#!/usr/bin/env python
import tkinter as tk
import requests


def get_quote():
    quote = requests.get(url="https://api.kanye.rest/")
    canvas.itemconfig(quote_text, text=quote.json()["quote"])


root = tk.Tk()
root.title("Kanye Quotes")
root.config(width=400, height=550, bg="#ffff99")
root.resizable(False, False)

canvas = tk.Canvas(root, width=300, height=414, background="#ffff99", highlightthickness=0)
quote_img = tk.PhotoImage(file="background.png", width=300, height=414)
canvas.create_image(150, 207, image=quote_img)
canvas.pack(padx=30, pady=30)

quote_text = canvas.create_text(150, 207,
                                justify="center",
                                width=260,
                                font=("URW Bookman", 16, "italic")
                                )

k_img = tk.PhotoImage(file="./kanye.png")

k_but = tk.Button(command=get_quote,
                  image=k_img,
                  background="#ffff99",
                  activebackground="#ffff99",
                  highlightthickness=0,
                  overrelief="flat",
                  relief="flat"
                  )

k_but.pack(pady=10)


get_quote()


root.mainloop()
