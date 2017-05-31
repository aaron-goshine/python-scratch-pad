import Tkinter as tki
import ttk


def gui():
    rock = 1
    paper = 2
    scissors = 3
    N = tki.N
    W = tki.W
    S = tki.S
    E = tki.E

    names = {rock: "Rock", paper: "Paper", scissors: "Scissors"}
    rules = {rock: scissors, paper: rock, scissors: paper}

    player_score = 0
    computer_score = 0
    rps_window = tki.Toplevel()
    rps_window.title("Rock, Paper, Scissors")
    rps_window.attributes('-topmost', 1)
    rps_window.attributes('-topmost', 0)

    player_choice = tki.IntVar()
    computer_choice = tki.StringVar()
    result_set = tki.StringVar()
    player_choice.set(1)
    player_score = tki.IntVar()
    computer_score = tki.IntVar()

    rps_frame = ttk.Frame(rps_window, padding='3 3 12 12', width=300)
    rps_frame.grid(column=0, row=0, sticky=(N, W, E, S))
    rps_frame.columnconfigure(0, weight=1)
    rps_frame.rowconfigure(0, weight=1)

    def start():
        while game(player_score, computer_score):
            pass

    ttk.Label(rps_frame, text="Player").grid(column=3, row=1, sticky=W)

    ttk.Radiobutton(
            rps_frame, text="Rock",
            variable=player_choice, value=1
            ).grid(column=1, row=2, sticky=W)

    ttk.Radiobutton(
            rps_frame, text="Paper",
            variable=player_choice, value=2
            ).grid(column=1, row=3, sticky=W)

    ttk.Radiobutton(
            rps_frame, text="Scissors",
            variable=player_choice, value=3
            ).grid(column=1, row=4, sticky=W)

    ttk.Label(
            rps_frame, text="Computer"
            ).grid(column=3, row=1, sticky=W)

    ttk.Label(
            rps_frame, textvariable=computer_choice
            ).grid(column=3, row=3, sticky=W)

    ttk.Button(
            rps_frame, text="Play", command=start
            ).grid(column=2, row=2, sticky=W)

    ttk.Label(
            rps_frame, text="Score"
            ).grid(column=1, row=5, sticky=W)

    ttk.Label(
            rps_frame, textvariable=computer_choice
            ).grid(column=3, row=6, sticky=W)

    ttk.Label(
            rps_frame, textvariable=result_set
            ).grid(column=2, row=7)

    def game(pl_score, cpu_score):
        player = player_choice.get()
        import random
        computer = random.randint(1, 3)
        computer_choice.set(names[computer])
        result(player, computer, pl_score, cpu_score)

    def result(player, computer, player_score, computer_score):
        new_score = 0
        if player == computer:
            result_set.set("Tie game.")
        else:
            if rules[player] == computer:
                result_set.set("You won")
                new_score = player_score.get()
                new_score += 1
                player_score.set(new_score)
            else:
                result_set.set("Computer won")
                new_score = player_score.get()
                new_score += 1
                computer_score.set(new_score)


if __name__ == "__main__":
    gui()
