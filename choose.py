from tkinter import *
from rps import main as m1
from ttt import main as m2

# --- window ---

window = Tk()
window.title('Choose game')

def rps1():
    m1()

def ttt1():
    m2()

def main():
    btn1 = Button(text="RPS", height=1, width=10, font=('arial', 20), command=lambda: rps1())
    btn2 = Button(text="TTT", height=1, width=10, font=('arial', 20), command=lambda: ttt1())

    btn1.grid(column=1, row=1)
    btn2.grid(column=1, row=2)

    window.mainloop()


if __name__ == '__main__':
    main()
