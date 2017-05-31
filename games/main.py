#!/usr/local/bin/python
import Tkinter as tki

import rockpaperscissors

root = tki.Tk()
root.title("Mega game collection")

mainframe = tki.Frame(root, height=200, width=500)
mainframe.pack_propagate(0)
mainframe.pack(padx=5, pady=5)

intro = tki.Label(mainframe, text="Welcome to the Mega game collection")
intro.pack(side=tki.TOP)

rps_button = tki.Button(
        mainframe, text="Rock, Paper, Scissors", command=rockpaperscissors.gui)
rps_button.pack()

root.mainloop()
