import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [[None for _ in range(3)] for _ in range(3)]

        self.create_buttons()

    def create_buttons(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.window, text=" ", font=("Arial", 20), height=2, width=5,
                                   command=lambda r=row, c=col: self.click_box(r, c))
                button.grid(row=row, column=col)
                self.board[row][col] = button

    def click_box(self, row, col):
        button = self.board[row][col]
        if button["text"] == " ":
            button["text"] = self.current_player
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.is_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
        else:
            messagebox.showwarning("Invalid Move", "Box already taken!")

    def check_winner(self):
        for row in range(3):
            if all(self.board[row][col]["text"] == self.current_player for col in range(3)):
                return True

        for col in range(3):
            if all(self.board[row][col]["text"] == self.current_player for row in range(3)):
                return True

        if all(self.board[i][i]["text"] == self.current_player for i in range(3)) or \
           all(self.board[i][2 - i]["text"] == self.current_player for i in range(3)):
            return True

        return False

    def is_draw(self):
        return all(self.board[row][col]["text"] != " " for row in range(3) for col in range(3))

    def reset_game(self):
        for row in range(3):
            for col in range(3):
                self.board[row][col]["text"] = " "
        self.current_player = "X"

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()