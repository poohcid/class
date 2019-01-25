"""Cake"""
from tkinter import *
from tkinter import ttk

def main():
    """main"""
    print("Hello world")

def yuii():
    """kuy"""
    gui = Tk()
    gui.geometry('200x200')
    bcal = ttk.Button(gui,text="calculate",command=main)
    bcal.pack()
    gui.mainloop()

main()
yuii()
