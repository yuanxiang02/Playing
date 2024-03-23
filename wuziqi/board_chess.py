import tkinter as tk
class FiveChessGame:
    def __init__(self, master):
        self.master = master
        self.master.title("五子棋")

        self.canvas = tk.Canvas(master, width=450, height=450, bg="white")
        self.canvas.pack()
        self.current_player = "black"
        self.board_list = []

        self.draw_board()
        self.error_label = tk.Label(master, text="", fg="red")
        self.error_label.pack()
        self.canvas.bind("<Button-1>", self.on_click)

        self.exit_button = tk.Button(master, text="退出", command=self.exit_program)
        self.exit_button.pack()

        self.undo_onestep = tk.Button(master, text="悔棋一步", command=self.undo_onestep)
        self.undo_onestep.pack()

    def draw_board(self):
        for i in range(15):
            self.canvas.create_line(30, 30 * i + 30, 450 - 30, 30 * i + 30)
            self.canvas.create_line(30 * i + 30, 30, 30 * i + 30, 450 - 30)

    def on_click(self, event):
        x, y = event.x, event.y

        col = round((x - 15) / 30)
        row = round((y - 15) / 30)

        if not (0 < row < 14 and 0 < col < 14):
            self.error_label.config(text="错误：超出棋盘范围！")
            return
        if (row, col) not in [(r,c) for _,r,c in self.board_list]:

            if self.current_player == "black":
                place_color = "black"
                self.current_player = "white"
            else:
                place_color = "white"
                self.current_player = "black"

            piece = self.canvas.create_oval(col * 30 + 15 - 13, row * 30 + 15 - 13, col * 30 + 15 + 13,
                                            row * 30 + 15 + 13,
                                            fill=place_color)
            self.board_list.append((piece,row, col))
        else:
            self.error_label.config(text="错误：该位置已经有棋子了")
            return

    def undo_onestep(self):
        history,pre_row,pre_col = self.board_list.pop()
        self.canvas.delete(history)
        self.current_player = "black" if self.current_player == "white" else "white"
    def exit_program(self):
        self.master.destroy()

