import tkinter, random

def enter_generate(lemon):
    generate_password()

def generate_password():
    global amount_symb
    try:
        amount_symb = int(entry.get())
    except ValueError:
        amount_symb = 6
    entry_result["width"]=amount_symb + 1
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "g", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    special_symb = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', "'", '"', '[', ']', '{', '}', '.', ',', '/', '?', '<', '>', ':', ';', '|', '~', '`']
    password = []
    for i in range(amount_symb):
        rand_choice = random.randint(1,2)
        if rand_choice == 1:
            rand_choice_upper = random.randint(1,2)
            if rand_choice_upper == 1:
                password.append(random.choice(letters))
            elif rand_choice_upper == 2:
                password.append(random.choice(letters).upper())
        elif rand_choice == 2:
            rand_choice_upper = random.randint(1, 2)
            if rand_choice_upper == 1:
                password.append(random.choice(numbers))
            elif rand_choice_upper == 2:
                password.append(random.choice(special_symb))
    result = "".join(password)
    entry_result.delete(0, "end")
    entry_result.insert(0, result)


amount_symb = 6

window = tkinter.Tk()
window.geometry("600x500")
window["bg"] = "green"
label = tkinter.Label(window,
                      text="Password Generator Lemon_013",
                      background="#19bf35",
                      width=30,
                      height=2,
                      font="arial 18")
label.pack()
label_2 = tkinter.Label(window,
                        text="Enter the amount of symbols",
                        background="#19bf35",
                        height=2,
                        font="arial 14"
                        )
label_2.pack()
entry = tkinter.Entry(window,
                      width=7,
                      font="arial 25"
                      )
entry.pack()
generate = tkinter.Button(window,
                          text="GENERATE",
                          command=generate_password,
                          background="orange",
                          height=2,
                          font="arial 22"
                          )
generate.pack(expand=1)
entry_result = tkinter.Entry(window,
                             width=amount_symb + 1,
                             font="arial 25"
                             )
entry_result.pack(expand=1)

window.bind("<Return>", enter_generate)
window.mainloop()