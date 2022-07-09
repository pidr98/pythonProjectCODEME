from tkinter import *
from rps import main as m1
from ttt import main as m2

# --- window ---
window = Tk()
window.title('Choose game')


def main():
    btn1 = Button(window, text="RPS", height=2, width=10, font=('arial', 20), command=m1)
    btn2 = Button(window, text="TTT", height=2, width=10, font=('arial', 20), command=m2)

    btn1.grid(column=1, row=1)
    btn2.grid(column=1, row=2)

    window.mainloop()


if __name__ == '__main__':
    main()
