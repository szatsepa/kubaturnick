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
        self.root.geometry('400x300')
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
        staff.add_command(label="Список", command=lambda: self.built_list(win))
#        staff.add_command(label="Kubaturnick", command=lambda: self.kub(win))
        staff.add_command(label="Quit", command=win.quit, underline=0)
        staff.add_separator()
#        top.add_cascade(label="Open", menu=staff, underline=0)
        top.add_cascade(label="Кубатурник", menu=staff, underline=0)
        staff.bind('<Button 1>', position)
        return


class WAction:

    def __init__(self):
        super(WAction, self).__init__()
        self.vars = []
        self.staff = []
        self.db = DB.DB()

    def setvars(self, vrs, stf):
        self.vars = vrs
        self.staff = stf

    def add(self, act, x, y):
        if act == 'change':
            row = 0

            for v in self.vars:
                vv = v.get()
                if vv == 1:
                    worker = self.staff[row]
                row += 1

        winFrame = Frame()
        winADD = Toplevel(winFrame)
        winADD.title('Adding')
        winADD.geometry("600x400+%d+%d" % (x, y))
        if act == 'change':
            l0 = Label(winADD, text='ID')
            l0.config(width=12, font='arial 16')
            l0.grid(row=0, column=0, padx=3, pady=6, sticky=W)
            e0 = Entry(winADD, width=4, font='arial 16')
            e0.grid(row=0, column=1, padx=1, pady=6, sticky=W)
        l1 = Label(winADD, text='Имя', width=12, font='arial 16')
        l1.grid(row=1, column=0, padx=3, pady=6, sticky=W)
        e1 = Entry(winADD, width=32, font='arial 16')
        e1.grid(row=1, column=1, padx=1, pady=6, sticky=W)
        l2 = Label(winADD, text='Телефон', width=12, font='arial 16')
        l2.grid(row=2, column=0, padx=3, pady=6, sticky=W)
        e2 = Entry(winADD, width=32, font='arial 16')
        e2.grid(row=2, column=1, padx=1, pady=6, sticky=W)
        l3 = Label(winADD, text='Адрес', width=12, font='arial 16')
        l3.grid(row=3, column=0, padx=3, pady=6, sticky=W)
        e3 = Entry(winADD, width=32, font='arial 16')
        e3.grid(row=3, column=1, padx=1, pady=6, sticky=W)
        l4 = Label(winADD, text='Activity', width=12, font='arial 16')
        l4.grid(row=4, column=0, padx=3, pady=6, sticky=W)
        e4 = Entry(winADD, width=2, font='arial 16')
        e4.insert(END, '1')
        e4.grid(row=4, column=1, padx=1, pady=6, sticky=W)
        lblbtn = 'Додати'
        if act == 'change':
            lblbtn = 'Змінити'
            e0.insert(END, worker[0])
            e1.insert(END, worker[1])
            e2.insert(END, worker[2])
            e3.insert(END, worker[3])
            e4.delete('0', END)
            e4.insert('0', worker[4])

        btn1 = Button(winADD, text=lblbtn)
        pers = []

        def sp(self):
            pers.append(e1.get())
            pers.append(e2.get())
            pers.append(e3.get())
            pers.append(e4.get())
            pers.append(e0.get())

            if act == 'add':
                self.db.setstaff(pers)
            elif act == 'change':
                self.db.updstaff(pers)
            winFrame.destroy()
            self.replace()

        def cansel(self):
            winFrame.destroy()

        def delstaff(self):
            parm = IntVar()
            parm.set(e0.get())
            self.db.delstaff(parm)
            winFrame.destroy()
            self.replace()

        btn1.config(command=lambda: sp(self))
        btn1. grid(row=5, column=0, padx=3, pady=5, sticky=E)

        delbtn = Button(winADD, text='Видалити')
        delbtn.grid(row=5, column=1, padx=3, pady=5, sticky=W)
        delbtn.config(command=lambda: delstaff(self))

        cans = Button(winADD, text='Скасувати')
        cans.config(command=lambda: cansel(self))
        cans.grid(row=5, column=1, padx=3, pady=5, sticky=E)


class Staff(Main, WAction):

    def __init__(self):
        self.vars = []
        self.staff = []
        self.checker = []
        self.frm = {}
        self.db = DB.DB()
        self.X = 0
        self.Y = 0

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
#            volume = int(vlm)
            cnt = float(count.get())
            out = vlm*cnt
            vol.insert(1.0, out)

        dlist = []
        rows = self.db.getdiam()
        cmbd = Combobox(self.frm['tk'], height=5)

        for row in rows:
            dlist.append(row[0])

        cmbd.config(values=dlist, font='arial 16')
        cmbd.set(rows[0])
        cmbd.grid(row=0, column=0, padx=0, pady=0, sticky=E)

        rows = self.db.getlength()
        llist = []
        cmbl = Combobox(self.frm['tk'], height=5)

        for row in rows:
            llist.append(row[0])

        cmbl.config(values=llist, font='arial 16')
        cmbl.set(rows[0])
        cmbl.grid(row=1, column=0, padx=0, pady=0, sticky=E)

        count = Entry(self.frm['tk'], width=6, font='arial 14')
        count.grid(row=2, column=0, padx=0, pady=0, sticky=W)
        count.insert(END, '1')

        vol = Text(self.frm['tk'], font='arial 16', width=8, height=1)
        vol.grid(row=3, column=0, padx=0, pady=0, sticky=W)

        calc = Button(self.frm['tk'], text='Расчитать')
        calc.grid(row=4, column=0, padx=0, pady=0, sticky=W)
        calc.config(command=lambda: calculate(self))


main = Topmenu()
win = main.makewin()
menu = main.makemenu(win)
main.built_list(win)
#main.makemenu()
win.mainloop()


