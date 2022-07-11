import random
from tkinter import *

# --- window ---
window = Tk()
window.resizable(0,0)
window.title("Rock Paper Scisors")


# --- player choice ---
def choice_to_number(choice):
    rps = {'rock': 0, 'paper': 1, 'scissor': 2}
    return rps[choice]

# --- cpu rng ---
def random_computer_choice():
    return random.choice(['rock', 'paper', 'scissor'])

# --- result ---
def result(human_choice, comp_choice):
    global user_score
    global comp_score

    user = choice_to_number(human_choice)
    comp = choice_to_number(comp_choice)

    if user == comp:
        pr_res = "Tie"
    elif (user - comp) % 3 == 1:
        user_score += 1
        pr_res = "USER won"
    else:
        comp_score += 1
        pr_res = "CPU won"
    # --- result output window(area) ---
    text_area = Text(window, height=10, width=30)
    text_area.grid(column=2, row=1, rowspan=3)

    uc = user_choice
    cc = comp_choice
    u = user_score
    c = comp_score

    answer = f" Your Choice: {uc} \n Computer's Choice : {cc} \n Result: {pr_res}\n Your Score : {u} \n Computer Score : {c}"
    text_area.insert(END, answer)

# --- choices ---
def rock():
    global user_choice
    global comp_choice

    user_choice = 'rock'
    comp_choice = random_computer_choice()
    result(user_choice, comp_choice)


def paper():
    global user_choice
    global comp_choice

    user_choice = 'paper'
    comp_choice = random_computer_choice()
    result(user_choice, comp_choice)


def scissor():
    global user_choice
    global comp_choice

    user_choice = 'scissor'
    comp_choice = random_computer_choice()
    result(user_choice, comp_choice)

# --- reset game ---
def reset():
    global btn1, btn2, btn3, user_score, comp_score, user_choice, comp_choice
    global text_area

    user_score = 0
    comp_score = 0
    user_choice = ""
    comp_choice = ""

    text_area = Text(window, height=10, width=30)
    text_area.grid(column=2, row=1, rowspan=3)

    btn1 = Button(text="ROCK", height=1, width=10, font=('arial', 20), command=rock)
    btn2 = Button(text="PAPER", height=1, width=10, font=('arial', 20), command=paper)
    btn3 = Button(text="SCISSOR", height=1, width=10, font=('arial', 20), command=scissor)

    btn1.grid(column=1, row=1)
    btn2.grid(column=1, row=2)
    btn3.grid(column=1, row=3)


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