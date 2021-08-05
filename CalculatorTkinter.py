# OOPs
from tkinter import *
import tkinter.messagebox as tmsg


class Calculator(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("450x450")
        self.title("Calculator")
        self.wm_iconbitmap("CalculatorIcon.ico")

    def typer(self):
        self.scvalue = StringVar()
        self.scvalue.set("")
        self.screen = Entry(self, textvar=self.scvalue, font="chiller 35 bold italic")
        self.screen.pack(fill=X, ipadx=5, ipady=7, padx=10, pady=10)

    def btns(self):
        rowk = [3, 3, 3, 2, 2, 2, 1, 1, 1]
        colk = [3, 2, 1, 3, 2, 1, 3, 2, 1]
        self.f = Frame(self, bg='grey')
        for i in range(0, 9):
            self.btn = Button(self.f, text=f"{i+1}", font="chiller 25 bold italic", width=4, height=1, relief=SUNKEN, borderwidth=3)
            self.btn.grid(row=rowk[i], column=colk[i], sticky=NSEW, padx=5, pady=5)
            self.btn.bind('<Button-1>', self.click)

        self.btn0 = Button(self.f, text="0", font="chiller 25 bold italic", width=4, height=1, relief=SUNKEN, borderwidth=3)
        self.btn0.grid(row=4, column=1, sticky=NSEW, padx=5, pady=5)
        self.btn0.bind('<Button-1>', self.click)
        self.btne = Button(self.f, text="=", font="chiller 25 bold italic", width=4, height=1, relief=SUNKEN, borderwidth=3)
        self.btne.grid(row=4, column=2, columnspan=2, sticky=NSEW, padx=5, pady=5)
        self.btne.bind('<Button-1>', self.click)
        self.btns1 = ['+', '-', '*', '/', '.', 'C', 'AC']
        self.row2 = [1, 1, 2, 2, 3, 3]
        self.col2 = [4, 5, 4, 5, 4, 5]
        # for i in range(0, 6):
        for i in range(len(self.btns1)-1):
            self.btn1 = Button(self.f, text=f"{self.btns1[i]}", font="chiller 25 bold italic", width=4, height=1, relief=SUNKEN, borderwidth=3)
            self.btn1.grid(row=self.row2[i], column=self.col2[i], sticky=NSEW, padx=5, pady=5)
            self.btn1.bind('<Button-1>', self.click)
            self.btn2 = Button(self.f, text=f"{self.btns1[i]}", font="chiller 25 bold italic", width=4, height=1, relief=SUNKEN, borderwidth=3)
            self.btn2.grid(row=self.row2[i], column=self.col2[i], sticky=NSEW, padx=5, pady=5)
            self.btn2.bind('<Button-1>', self.click)
        self.btnac = Button(self.f, text="AC", font="chiller 25 bold italic", width=4, height=1, relief=SUNKEN, borderwidth=3)
        self.btnac.grid(row=4, column=4, columnspan=2, sticky=NSEW, padx=5, pady=5)
        self.btnac.bind('<Button-1>', self.click)
        self.f.pack(anchor=CENTER)

    def click(self, event):
        global scvalue
        self.text = event.widget.cget("text")

        if self.text == '=':
            if self.scvalue.get().isdigit():
                self.operators = ['+', '-', '*', '/', '.']
                self.temp1 = str(self.scvalue.get())
                if self.temp1.endswith(tuple(self.operators)):
                    self.aa = tmsg.showinfo("Error", "Can't do this operation")
                    self.c = str(self.scvalue.get())
                    self.temp = len(self.c) - 1
                    self.c = self.c[0:self.temp]
                    self.scvalue.set(self.c)
                    self.screen.update()
                else:
                    self.val = int(self.scvalue.get())
                    self.scvalue.set(self.val)
                    self.screen.update()
            else:
                self.operators = ['+', '-', '*', '/', '.']
                self.temp1 = str(self.scvalue.get())
                if self.temp1.endswith(tuple(self.operators)):
                    self.aa = tmsg.showinfo("Error", "Can't do this operation")
                    self.c = str(self.scvalue.get())
                    self.temp = len(self.c) - 1
                    self.c = self.c[0:self.temp]
                    self.scvalue.set(self.c)
                    self.screen.update()
                else:
                    self.val = eval(self.scvalue.get())
                    # for whole numbers as ouput use this: self.scvalue.set(int(self.val))
                    self.scvalue.set(self.val)
                    self.screen.update()

        elif self.text == 'C' or self.text == 'AC':
            if self.text == 'AC':
                self.scvalue.set("")
                self.screen.update()
            else:
                self.c = str(self.scvalue.get())
                self.temp = len(self.c)-1
                self.c = self.c[0:self.temp]
                self.scvalue.set(self.c)
                self.screen.update()

        else:
            self.scvalue.set(self.scvalue.get() + self.text)
            self.screen.update()


if __name__ == '__main__':
    window = Calculator()
    window.typer()
    window.btns()
    window.mainloop()
exit()
