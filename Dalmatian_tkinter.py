import tkinter as tk



class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x500")
        self.title("Dalmatian -- A Simple Spotify Game by Maxwell Madden")
        self.resizable(0,0)

        self.topmenu = TopMenu()
        self.gameframe = GameFrame()


class TopMenu(tk.Frame):
    def __init__(self, container):
        super().__init__(container)

class GameFrame(tk.Frame):
    def __init__(self, container):
        super().__init__(container)


if __name__ == '__main__':
    app = Main()
    app.mainloop()