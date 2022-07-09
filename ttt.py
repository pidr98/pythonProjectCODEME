from tkinter import *
from tkinter import messagebox

# --- window ---
window = Tk()
window.resizable(0,0)
window.title('Tic-Tac-Toe')

clicked = True
count = 0

# --- check who won ---
def check_if_won():
    winner = False

    # --- X wins ---
    if btn1["text"] == "X" and btn2["text"] == "X" and btn3["text"] == "X":
        btn1.config(bg="green")
        btn2.config(bg="green")
        btn3.config(bg="green")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "X WINS")

    elif btn4["text"] == "X" and btn5["text"] == "X" and btn6["text"] == "X":
        btn4.config(bg="green")
        btn5.config(bg="green")
        btn6.config(bg="green")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "X WINS")

    elif btn7["text"] == "X" and btn8["text"] == "X" and btn9["text"] == "X":
        btn7.config(bg="green")
        btn8.config(bg="green")
        btn9.config(bg="green")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "X WINS")

    elif btn1["text"] == "X" and btn4["text"] == "X" and btn7["text"] == "X":
        btn1.config(bg="green")
        btn4.config(bg="green")
        btn7.config(bg="green")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "X WINS")

    elif btn2["text"] == "X" and btn5["text"] == "X" and btn8["text"] == "X":
        btn2.config(bg="green")
        btn5.config(bg="green")
        btn8.config(bg="green")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "X WINS")

    elif btn3["text"] == "X" and btn6["text"] == "X" and btn9["text"] == "X":
        btn3.config(bg="green")
        btn6.config(bg="green")
        btn9.config(bg="green")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "X WINS")

    elif btn1["text"] == "X" and btn5["text"] == "X" and btn9["text"] == "X":
        btn1.config(bg="green")
        btn5.config(bg="green")
        btn9.config(bg="green")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "X WINS")

    elif btn3["text"] == "X" and btn5["text"] == "X" and btn7["text"] == "X":
        btn3.config(bg="green")
        btn5.config(bg="green")
        btn7.config(bg="green")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "X WINS")

    # --- O wins ---
    elif btn1["text"] == "O" and btn2["text"] == "O" and btn3["text"] == "O":
        btn1.config(bg="green")
        btn2.config(bg="green")
        btn3.config(bg="green")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "O WINS")

    elif btn4["text"] == "O" and btn5["text"] == "O" and btn6["text"] == "O":
        btn4.config(bg="green")
        btn5.config(bg="green")
        btn6.config(bg="green")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "O WINS")

    elif btn7["text"] == "O" and btn8["text"] == "O" and btn9["text"] == "O":
        btn7.config(bg="green")
        btn8.config(bg="green")
        btn9.config(bg="green")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "O WINS")

    elif btn1["text"] == "O" and btn4["text"] == "O" and btn7["text"] == "O":
        btn1.config(bg="green")
        btn4.config(bg="green")
        btn7.config(bg="green")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "O WINS")

    elif btn2["text"] == "O" and btn5["text"] == "O" and btn8["text"] == "O":
        btn2.config(bg="green")
        btn5.config(bg="green")
        btn8.config(bg="green")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "O WINS")

    elif btn3["text"] == "O" and btn6["text"] == "O" and btn9["text"] == "O":
        btn3.config(bg="green")
        btn6.config(bg="green")
        btn9.config(bg="green")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "O WINS")

    elif btn1["text"] == "O" and btn5["text"] == "O" and btn9["text"] == "O":
        btn1.config(bg="green")
        btn5.config(bg="green")
        btn9.config(bg="green")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "O WINS")

    elif btn3["text"] == "O" and btn5["text"] == "O" and btn7["text"] == "O":
        btn3.config(bg="green")
        btn5.config(bg="green")
        btn7.config(bg="green")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "O WINS")

    # --- tie ---
    if count == 9 and winner == False:
        messagebox.showinfo("Tic-Tac-Toe", "TIE")


# --- button click ---
def button_click(b):
    global clicked, count

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_if_won()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_if_won()
    else:
        messagebox.showerror("Tic-Tac-Toe", "ALREADY PICKED")

# --- reset ---
def reset():
    global btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9
    global clicked, count
    clicked = True
    count = 0

    # --- create button ---
    btn1 = Button(window, text=" ", font=("Arial", 15), height=2, width=5, command=lambda: button_click(btn1))
    btn2 = Button(window, text=" ", font=("Arial", 15), height=2, width=5, command=lambda: button_click(btn2))
    btn3 = Button(window, text=" ", font=("Arial", 15), height=2, width=5, command=lambda: button_click(btn3))
    btn4 = Button(window, text=" ", font=("Arial", 15), height=2, width=5, command=lambda: button_click(btn4))
    btn5 = Button(window, text=" ", font=("Arial", 15), height=2, width=5, command=lambda: button_click(btn5))
    btn6 = Button(window, text=" ", font=("Arial", 15), height=2, width=5, command=lambda: button_click(btn6))
    btn7 = Button(window, text=" ", font=("Arial", 15), height=2, width=5, command=lambda: button_click(btn7))
    btn8 = Button(window, text=" ", font=("Arial", 15), height=2, width=5, command=lambda: button_click(btn8))
    btn9 = Button(window, text=" ", font=("Arial", 15), height=2, width=5, command=lambda: button_click(btn9))

    # --- button grid---
    btn1.grid(row=0, column=0)
    btn2.grid(row=0, column=1)
    btn3.grid(row=0, column=2)
    btn4.grid(row=1, column=0)
    btn5.grid(row=1, column=1)
    btn6.grid(row=1, column=2)
    btn7.grid(row=2, column=0)
    btn8.grid(row=2, column=1)
    btn9.grid(row=2, column=2)


def menu():
    # --- menu ---
    menu = Menu(window)
    window.config(menu=menu)

    # --- menu config ---
    menu.add_cascade(label="Reset", command=reset)


def main():
    menu()
    reset()
    window.mainloop()


if __name__ == '__main__':
    main()
