import sqlite3
from tkinter import *
from tkinter import messagebox as ms
from random import randint
db = sqlite3.connect("GenieEnHerbe_BD.db")
cursur = db.cursor()
class Calcul():

    def __init__(self,master):
        self.master = master
        self.idmail = IntVar()
        self.number1 = 0
        self.number2 = 0
        self.reponse = StringVar()
        self.acceuil = Frame(self.master, padx = 30, pady = 30)
        self.g2f = Frame(self.master, padx = 30, pady = 30)
        self.g2f1 = Frame(self.master, padx = 30, pady = 30)
        self.g2f2 = Frame(self.master, padx = 30, pady = 30)
        self.g2f3 = Frame(self.master, padx = 30, pady = 30)
        self.g2f4 = Frame(self.master, padx = 30, pady = 30)

    def score(self,value):
        find_user = ("UPDATE user SET score = score + ? WHERE  idmail = ? ")
        cursur.execute(find_user,[(value),(self.idmail)])
        db.commit()

    def num_gen(self):
        self.number1 = randint(0,21)
        self.number2 = randint(0,21)

    def function1(self):
        res = self.number1 + self.number2
        if self.reponse.get() == str(res):
            ms.showinfo("0_0 Success","BRAVO vous avez gagne 15 pts ")
            self.score(10)
        else:
            concat = str(self.number1) +" + "+ str(self.number2) +" = "+ str(res)
            ms.showerror("x_x Error",concat)
        self.reponse.set("")
        self.g2f1.pack_forget()
        self.widget1()

    def function2(self):
        if self.number1 > self.number2:
            res = self.number1 - self.number2
            concat = str(self.number1) + " - " + str(self.number2) + " = " + str(res)
        else:
            res = self.number2 - self.number1
            concat = str(self.number2) + " - " + str(self.number1) + " = " + str(res)

        if self.reponse.get() == str(res):
            ms.showinfo("0_0 Success","BRAVO vous avez gagne 15 pts ")
            self.score(10)
        else:
            ms.showerror("x_x Error",concat)
        self.reponse.set("")
        self.g2f2.pack_forget()
        self.widget2()

    def function3(self):
        res = self.number1 * self.number2
        if self.reponse.get() == str(res):
            ms.showinfo("0_0 Success","BRAVO vous avez gagne 15 pts ")
            self.score(50)
        else:
            concat = str(self.number1) + " X " + str(self.number2) + " = " + str(res)
            ms.showerror("x_x Error",concat)
        self.reponse.set("")
        self.g2f3.pack_forget()
        self.widget3()
            
    def function4(self):
        while(self.number1 == 0 or self.number2 == 0):
            self.widget4()
        if self.number1 > self.number2:
            res = self.number1 // self.number2
            concat = str(self.number1) + " / " + str(self.number2) + " = " + str(res)
        else:
            res = self.number2 // self.number1
            concat = str(self.number2) + " / " + str(self.number1) + " = " + str(res)
        if self.reponse.get() == str(res):
            ms.showinfo("0_0 Success","BRAVO vous avez gagne 15 pts ")
            self.score(50)
        else:
            ms.showerror("x_x Error",concat)
        self.reponse.set("")
        self.g2f4.pack_forget()
        self.widget4()
        
    def retour_acceuil(self):
        self.g2f.pack_forget()
        self.acceuil.pack()
        
    def retour(self):
        self.reponse.set("")
        self.g2f1.pack_forget()
        self.g2f2.pack_forget()
        self.g2f3.pack_forget()
        self.g2f4.pack_forget()
        self.widgets()
            
    def widget1(self):
        self.num_gen()
        text1 = str(self.number1)
        text2 = str(self.number2)
        concat = text1 + "    +   " + text2 
        self.g2f.pack_forget()
        self.g2f1 = Frame(self.master, padx = 30, pady = 30)
        Label(self.g2f1, text = concat ,width=10,font = ('bold',16),padx = 10 , pady = 10).grid(row=1,column = 1)
        Label(self.g2f1, text = "Reponse : ",width=10,font = ('bold',13),padx = 15 , pady = 15).grid(row=2,column=0)
        Entry(self.g2f1, textvariable = self.reponse, width=20,font = ('calibri',13)).grid(row=2,column=1)
        Button(self.g2f1, text=" Valider ",width=15, bg = 'white',fg = "green",font = ('calibri',14),command=self.function1).grid(row=3,column=2,sticky=W)
        Button(self.g2f1, text=" Retour -> ",width=15, bg = 'white',fg = "red",font = ('calibri',14),command=self.retour).grid(row=3,column=0,sticky=E)
        self.g2f1.pack()
        
    def widget2(self):
        self.num_gen()
        text1 = str(self.number1)
        text2 = str(self.number2)
        if self.number1 > self.number2:
            concat = text1 + "    -   " + text2 
        else:
            concat = text2 + "    -    " + text1 
        self.g2f.pack_forget()  
        Label(self.g2f2, text = concat ,width=10,font = ('bold',16),padx = 10 , pady = 10).grid(row=1,column = 1)
        Label(self.g2f2, text = "Reponse : ",width=10,font = ('bold',13),padx = 15 , pady = 15).grid(row=2,column=0)
        Entry(self.g2f2, textvariable = self.reponse, width=20,font = ('calibri',13)).grid(row=2,column=1)
        Button(self.g2f2, text=" Valider ",width=15, bg = 'white',fg = "green",font = ('calibri',14),command=self.function2).grid(row=3,column=2,sticky=W)
        Button(self.g2f2, text=" Retour -> ",width=15, bg = 'white',fg = "red",font = ('calibri',14),command=self.retour).grid(row=3,column=0,sticky=E)
        self.g2f2.pack()

    def widget3(self):
        self.num_gen()
        text1 = str(self.number1)
        text2 = str(self.number2)
        concat = text1 + "    x    " + text2
        self.g2f.pack_forget()
        Label(self.g2f3, text = concat ,width=10,font = ('bold',16),padx = 10 , pady = 10).grid(row=1,column = 1)
        Label(self.g2f3, text = "Reponse : ",width=10,font = ('bold',13),padx = 15 , pady = 15).grid(row=2,column=0)
        Entry(self.g2f3, textvariable = self.reponse, width=20,font = ('calibri',13)).grid(row=2,column=1)
        Button(self.g2f3, text=" Valider ",width=15, bg = 'white',fg = "green",font = ('calibri',14),command=self.function3).grid(row=3,column=2,sticky=W)
        Button(self.g2f3, text=" Retour -> ",width=15, bg = 'white',fg = "red",font = ('calibri',14),command=self.retour).grid(row=3,column=0,sticky=E)
        self.g2f3.pack()

    def widget4(self):
        self.num_gen()
        text1 = str(self.number1)
        text2 = str(self.number2)
        if self.number1 > self.number2:
            concat = text1 + "    /  " + text2 
        else:
            concat = text2 + "    /    " + text1 
        self.g2f.pack_forget()
        Label(self.g2f4, text = concat ,width=10,font = ('bold',16),padx = 10 , pady = 10).grid(row=1,column = 1)
        Label(self.g2f4, text = "Reponse : ",width=10,font = ('bold',13),padx = 15 , pady = 15).grid(row=2,column=0)
        Entry(self.g2f4, textvariable = self.reponse, width=20,font = ('calibri',13)).grid(row=2,column=1)
        Button(self.g2f4, text=" Valider ",width=15, bg = 'white',fg = "green",font = ('calibri',14),command=self.function4).grid(row=3,column=2,sticky=W)
        Button(self.g2f4, text=" Retour -> ",width=15, bg = 'white',fg = "red",font = ('calibri',14),command=self.retour).grid(row=3,column=0,sticky=E)
        Label(self.g2f4, text = "* Uniquement le quotient", padx = 10 , pady = 10,fg ='red', font = ('cambria',10)).grid(row=4)
        self.g2f4.pack()
    
        
    def widgets(self):
        self.reponse.set("")
        self.g2f = Frame(self.master, padx = 30, pady = 30) 
        Button(self.g2f, text=" Addition ",width=20, bg = 'white',fg = "blue", pady = 15, font = ('calibri',14),command=self.widget1).grid(row=1,column=0)
        Button(self.g2f, text=" Soustraction ",width=20, bg = 'white',fg = "red",pady = 15,font = ('calibri',14),command=self.widget2).grid(row=1,column=1)
        Button(self.g2f, text=" Multiplication ",width=20, bg = 'white',fg = "green",pady = 15,font = ('calibri',14),command=self.widget3).grid(row=2,column=0)
        Button(self.g2f, text=" Division",width=20, bg = 'white',fg = "black",pady = 15,font = ('calibri',14),command=self.widget4).grid(row=2,column=1)
        Button(self.g2f, text=" Retour a l'acceuil ",width=15, bg = 'white',fg = "grey",pady = 15,font = ('calibri',14),command=self.retour_acceuil).grid(row=4,column=1)
        Label(self.g2f, text = "* Tous les niveaux sont autorises", padx = 10 , pady = 10,fg ='red', font = ('cambria',10)).grid(row=3)
        self.g2f.pack()
                    
