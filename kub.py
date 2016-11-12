# -*- coding: utf-8 -*-

from tkinter import *
from tkinter.ttk import *
import DB
#import menu_win


class Main:

    def __init__(self):
        self.root = Tk()

    def makewin(self):
        self.root.title('KUBATURNICK')
        self.root.geometry('240x300')
        self.root.resizable(True, True)
        return self.root

    def getroot(self):
        rt = self.root
        return rt


class Topmenu(Main):

    def __init__(self):
        super(Topmenu, self).__init__()
        try:
            self.root
        except:
            print("HUJA")
        self.winX = 0
        self.winY = 0

    def built_list(self, win):
        staff = Staff()
        staff.view(win, self.winX, self.winY)

    def kub(self, win):
        self.kub = Kub()
        self.kub.getkub()

    def makemenu(self, win):
        def position(event):
            self.winX = event.x_root
            self.winY = event.y_root

        top = Menu(win)
        win.config(menu=top)
        staff = Menu(top)
#        staff.add_command(label="Список", command=lambda: self.built_list(win))
#        staff.add_command(label="Kubaturnick", command=lambda: self.kub(win))
        staff.add_command(label="Quit", command=win.quit, underline=0)
        staff.add_separator()
#        top.add_cascade(label="Open", menu=staff, underline=0)
        top.add_cascade(label="Кубатурник", menu=staff, underline=0)
        staff.bind('<Button 1>', position)
        return


class Staff(Main):

    def __init__(self):
        self.vars = []
        self.staff = []
        self.checker = []
        self.frm = {}
        self.db = DB.DB()
        self.X = 0
        self.Y = 0
        self.SM = 0
        self.woods = 0

    def getfrm(self):
        return self.frm

    def view(self, win, X, Y):
        self.X = X
        self.Y = Y
        tk = Frame(win)
        tk.pack()
        self.frm['win'] = win
        self.frm['tk'] = tk
        self.printlist()
        return

    def replace(self):
        txt.destroy()
        self.printlist()
        return

    def printlist(self):

        def calculate(self):
            parm = []
            parm.append(cmbd.get())
            parm.append(cmbl.get())
            v = self.db.getval(parm)
            vlm = float(v)
            cnt = float(count.get())
            out = vlm * cnt
            vol.delete(1.0, END)
            vol.insert(1.0, out)

            self.SM += out
            self.woods += cnt

            sm.delete(1.0, END)
            sm.insert(1.0, self.SM)

            wds.delete(1.0, END)
            wds.insert(1.0, self.woods)

        def clearres(self):
            self.SM = 0
            sm.delete(1.0, END)
            wds.delete(1.0, END)

        dlist = []
        rows = self.db.getdiam()
        l0 = Label(self.frm['tk'], text='Диам(см)')
        l0.config(width=8, font='arial 10')
        l0.grid(row=0, column=0, padx=3, pady=6, sticky=W)
        cmbd = Combobox(self.frm['tk'], height=5, width=4)

        for row in rows:
            dlist.append(row[0])

        cmbd.config(values=dlist, font='arial 16')
        cmbd.set(rows[0])
        cmbd.grid(row=0, column=1, padx=0, pady=0, sticky=W)

        rows = self.db.getlength()
        llist = []
        l1 = Label(self.frm['tk'], text='Длина(м)')
        l1.config(width=8, font='arial 10')
        l1.grid(row=1, column=0, padx=3, pady=6, sticky=W)
        cmbl = Combobox(self.frm['tk'], height=5, width=4)

        for row in rows:
            llist.append(row[0])

        cmbl.config(values=llist, font='arial 16')
        cmbl.set(rows[0])
        cmbl.grid(row=1, column=1, padx=0, pady=0, sticky=W)

        l2 = Label(self.frm['tk'], text='Колич.')
        l2.config(width=8, font='arial 10')
        l2.grid(row=2, column=0, padx=3, pady=6, sticky=W)

        count = Entry(self.frm['tk'], width=6, font='arial 14')
        count.grid(row=2, column=1, padx=0, pady=0, sticky=W)
        count.insert(END, '1')

        l3 = Label(self.frm['tk'], text='Объем(м3)')
        l3.config(width=12, font='arial 10')
        l3.grid(row=3, column=0, padx=3, pady=6, sticky=W)

        vol = Text(self.frm['tk'], font='arial 16', width=8, height=1)
        vol.grid(row=3, column=1, padx=0, pady=0, sticky=W)

        l4 = Label(self.frm['tk'], text='**Результаты**')
        l4.config(width=20, font='arial 12')
        l4.grid(row=5, column=1, padx=3, pady=6, sticky=W)

        calc = Button(self.frm['tk'], text='Расчитать')
        calc.grid(row=4, column=1, padx=0, pady=0, sticky=W)
        calc.config(command=lambda: calculate(self))

        l5 = Label(self.frm['tk'], text='Сумма (м3)')
        l5.config(width=12, font='arial 10')
        l5.grid(row=7, column=0, padx=3, pady=6, sticky=W)

        sm = Text(self.frm['tk'], font='arial 16', width=8, height=1)
        sm.grid(row=7, column=1, padx=0, pady=0, sticky=W)

        l8 = Label(self.frm['tk'], text='Бревен (шт)')
        l8.config(width=12, font='arial 10')
        l8.grid(row=8, column=0, padx=3, pady=6, sticky=W)

        wds = Text(self.frm['tk'], font='arial 16', width=8, height=1)
        wds.grid(row=8, column=1, padx=0, pady=0, sticky=W)

#        l6 = Label(self.frm['tk'], text='')
#        l6.config(width=12, font='arial 10')
#        l6.grid(row=9, column=0, padx=3, pady=6, sticky=W)

        l7 = Label(self.frm['tk'], text='Очистить')
        l7.config(width=12, font='arial 10')
        l7.grid(row=10, column=0, padx=3, pady=6, sticky=W)

        clear = Button(self.frm['tk'], text='Очистить')
        clear.grid(row=10, column=1, padx=0, pady=0, sticky=W)
        clear.config(command=lambda: clearres(self))


main = Topmenu()
win = main.makewin()
menu = main.makemenu(win)
main.built_list(win)
#main.makemenu()
win.mainloop()


