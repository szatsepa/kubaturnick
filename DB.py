# -*- coding: utf-8 -*-
import sqlite3
class DB:

    def __init__(self):
        self.con = sqlite3.connect("kubdb")

    def getstaff(self):
       cur = self.con.cursor()
       cur.execute('SELECT * FROM staff ')
       return cur.fetchall()

    def getactivity(self):
       cur = self.con.cursor()
       cur.execute('SELECT id ||":"|| surname FROM staff WHERE activity = 1')
       return cur.fetchall()

    def getrange(self):
        cur = self.con.cursor()
        cur.execute('SELECT id || ":" ||range FROM range WHERE activity = 1')
        return cur.fetchall()

    def setstaff(self, parm):
        cur = self.con.cursor()
        cur.execute('insert into staff (surname, phone, address,activity)'\
        ' values(?,?,?,?)',
        (parm[0], parm[1], parm[2], 1))
        self.con.commit()
        return 1

    def updstaff(self, parm):
        cur = self.con.cursor()
        query = 'UPDATE staff SET surname = ?, phone = ?,'\
        ' address = ?, activity = ? WHERE id = ?'
        cur.execute(query, parm)
        self.con.commit()
#        print(parm)
        return 1

    def delstaff(self, parm):
        cur = self.con.cursor()
        cur.execute('UPDATE staff SET activity = 0 WHERE id = %d' % parm.get())
        self.con.commit()
        print(parm.get())
        return 1

    def getkub(self):
        cur = self.con.cursor()
        cur.execute('SELECT * FROM kub')
        self.con.commit()
        return cur.fetchall()

    def getlength(self):
        cur = self.con.cursor()
        cur.execute('SELECT l FROM kub GROUP BY l')
        self.con.commit()
        return cur.fetchall()

    def getdiam(self):
        cur = self.con.cursor()
        cur.execute('SELECT d FROM kub GROUP BY d')
        self.con.commit()
        return cur.fetchall()

    def getval(self, parm):
        cur = self.con.cursor()
        query = 'SELECT v FROM kub WHERE d=? AND l=?'
        cur.execute(query, parm)
        self.con.commit()
        volume = cur.fetchall()
        s = volume[0][0]
        vlm = s.replace(',', '.')
        return vlm

