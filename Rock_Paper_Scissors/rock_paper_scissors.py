import tkinter as tk
import random


# ---------------- GAME LOGIC ----------------

choices = ["Rock", "Paper", "Scissors"]

user_score = 0
computer_score = 0
round_no = 0


def play(user_choice):

    global user_score, computer_score, round_no

    computer_choice = random.choice(choices)
    round_no += 1

    user_label.config(text=f"You chose: {user_choice}")
    computer_label.config(text=f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        result = "It's a Tie 🤝"

    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win 🎉"
        user_score += 1

    else:
        result = "Computer Wins 🤖"
        computer_score += 1


    result_label.config(text=result)

    score_label.config(
        text=f"Score  You: {user_score}  |  Computer: {computer_score}"
    )

    round_label.config(
        text=f"Round: {round_no}"
    )


def reset_game():

    global user_score, computer_score, round_no

    user_score = 0
    computer_score = 0
    round_no = 0

    user_label.config(text="You chose:")
    computer_label.config(text="Computer chose:")
    result_label.config(text="Make your move!")

    score_label.config(
        text="Score  You: 0 | Computer: 0"
    )

    round_label.config(
        text="Round: 0"
    )



# ---------------- GUI DESIGN ----------------

root = tk.Tk()

root.title("Rock Paper Scissors Game")
root.geometry("500x600")
root.resizable(False,False)

root.configure(bg="#121212")


title = tk.Label(
    root,
    text="🪨 ROCK  PAPER  SCISSORS ✂️",
    font=("Arial",18,"bold"),
    bg="#121212",
    fg="white"
)

title.pack(pady=20)



round_label = tk.Label(
    root,
    text="Round: 0",
    font=("Arial",13),
    bg="#121212",
    fg="#00ff99"
)

round_label.pack()



score_label = tk.Label(
    root,
    text="Score  You: 0 | Computer: 0",
    font=("Arial",14,"bold"),
    bg="#121212",
    fg="white"
)

score_label.pack(pady=15)



user_label = tk.Label(
    root,
    text="You chose:",
    font=("Arial",13),
    bg="#121212",
    fg="white"
)

user_label.pack()



computer_label = tk.Label(
    root,
    text="Computer chose:",
    font=("Arial",13),
    bg="#121212",
    fg="white"
)

computer_label.pack(pady=5)



result_label = tk.Label(
    root,
    text="Make your move!",
    font=("Arial",20,"bold"),
    bg="#121212",
    fg="#00ff99"
)

result_label.pack(pady=30)



# BUTTON FRAME

button_frame = tk.Frame(
    root,
    bg="#121212"
)

button_frame.pack()



rock_btn = tk.Button(
    button_frame,
    text="🪨\nRock",
    width=10,
    height=3,
    font=("Arial",14),
    command=lambda: play("Rock")
)

rock_btn.grid(row=0,column=0,padx=10)



paper_btn = tk.Button(
    button_frame,
    text="📄\nPaper",
    width=10,
    height=3,
    font=("Arial",14),
    command=lambda: play("Paper")
)

paper_btn.grid(row=0,column=1,padx=10)



scissors_btn = tk.Button(
    button_frame,
    text="✂️\nScissors",
    width=10,
    height=3,
    font=("Arial",14),
    command=lambda: play("Scissors")
)

scissors_btn.grid(row=0,column=2,padx=10)




reset_btn = tk.Button(
    root,
    text="Reset Game 🔄",
    font=("Arial",13,"bold"),
    bg="#ff4444",
    fg="white",
    width=15,
    command=reset_game
)

reset_btn.pack(pady=40)



footer = tk.Label(
    root,
    text="Python GUI Project | CODSOFT",
    font=("Arial",10),
    bg="#121212",
    fg="gray"
)

footer.pack(side="bottom", pady=15)



root.mainloop()