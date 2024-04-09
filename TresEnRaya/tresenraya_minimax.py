import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tres En Raya")

        # self.master.geometry("400x400")

        self.master.eval('tk::PlaceWindow . center')
        
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        
        self.create_board()
        
    def create_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.master, text="", font=("Helvetica", 24),
                                               width=5, height=2, command=lambda i=i, j=j: self.button_click(i, j))
                self.buttons[i][j].grid(row=i, column=j, sticky="nsew")
                
        self.status_label = tk.Label(self.master, font=("Helvetica", 16))
        self.status_label.grid(row=3, columnspan=3)
        
    def button_click(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            
            if self.check_winner():
                messagebox.showinfo("Ganador!", f"Jugador {self.current_player} gana!")
                self.reset_game()
            elif self.check_draw():
                messagebox.showinfo("Empate!", "Empate!")
                self.reset_game()
            else:
                if self.current_player == "X":
                    self.current_player = "O"
                    # self.status_label.config(text="Turno de O")
                    self.computer_move()
                else:
                    self.current_player = "X"
                    # self.status_label.config(text="Turno de X")
        else:
            messagebox.showerror("Movimiento inválido", "Esa celda ya está ocupada.")

    
    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False
    
    def check_draw(self):
        for row in self.board:
            for cell in row:
                if cell == "":
                    return False
        return True
    
    def reset_game(self):
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="")
        # self.status_label.config(text="Turno de X")
        
    def computer_move(self):
    # Implementar el algoritmo Minimax para el movimiento de la computadora
        best_score = float('-inf')
        best_move = None
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    self.board[i][j] = "O"
                    score = self.minimax(self.board, False)
                    self.board[i][j] = ""
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)

        row, col = best_move
        self.board[row][col] = "O"
        self.buttons[row][col].config(text="O")

        if self.check_winner():
            messagebox.showinfo("Ganador!", "Computadora gana!")
            self.reset_game()
        elif self.check_draw():
            messagebox.showinfo("Empate!", "Empate!")
            self.reset_game()
        else:
            self.current_player = "X"
            # self.status_label.config(text="Turno de X")

        
    def minimax(self, board, is_maximizing):
        if self.check_winner():
            if is_maximizing:
                return -1
            else:
                return 1
        elif self.check_draw():
            return 0
        
        if is_maximizing:
            best_score = float('-inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == "":
                        board[i][j] = "O"
                        score = self.minimax(board, False)
                        board[i][j] = ""
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == "":
                        board[i][j] = "X"
                        score = self.minimax(board, True)
                        board[i][j] = ""
                        best_score = min(score, best_score)
            return best_score
        
def main():
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

if __name__ == "__main__":
    main()
