from tkinter import *


class Window:
    def __init__(self, width, height, title, window):
        self.width = width
        self.height = height
        self.window = window
        self.title = title
        self.window.geometry(str(width)+'x'+str(height))
        self.window.title(self.title)

        self.lable = Label(self.window, text="Test")
        self.lable.grid(row=3, column=3)

    def runwindow(self):
        self.window.mainloop()

    def addText(self, Text, posx, posy):
        lable = self.Label(self.window, text=Text)
        lable.grid(column=posx, row=posy)


window = Tk()
Fenster1 = Window(800, 600, "Test", window)
Fenster1.window.mainloop()
Fenster1.addText("Hallo Welt", 3, 3)
