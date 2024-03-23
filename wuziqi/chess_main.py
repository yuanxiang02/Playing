import tkinter as tk
from board_chess import FiveChessGame


def main():
    root = tk.Tk()
    game = FiveChessGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()