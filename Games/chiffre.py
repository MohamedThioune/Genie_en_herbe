import sqlite3
from tkinter import *
from tkinter import messagebox as ms
from random import randint
db = sqlite3.connect("GenieEnHerbe_BD.db")
cursur = db.cursor()
class Chiffre():

    def __init__(self,master):
        self.master = master
        self.chiffre = 0
        self.reponse = StringVar()
        self.idmail = IntVar()
        self.g1f = Frame(self.master,padx = 30,pady = 30)
        self.g1fcar =  Frame(self.master,padx = 30,pady = 30)
        self.acceuil = Frame(master, padx = 30, pady = 30)
        self.time = 51
        self.valid = False
        self.retr = False

    def score(self,value):
        find_user = ("UPDATE user SET score = score + ? WHERE  idmail = ? ")
        cursur.execute(find_user,[(value),(self.idmail)])
        db.commit()
        
    def function(self):
        self.valid = True
        first = 0
        second = 0
        third = 0
        lettre = ""
        entry = self.chiffre
        reponse = self.reponse.get()
        try:
            listdix = ['un','deux','trois','quatre','cinq','six','sept','huit','neuf']
            listexcept = ['onze','douze','treize','quatorze','quinze','seize']
            listcentaines = ['dix','vingt','trente','quarante','cinquante','soixante','soixante-dix','quatre-vingt','quatre-vingt-dix']
            if entry == 0:
                if reponse == "zero":
                    ms.showinfo("0_0 Success","BRAVO vous avez gagne 5 pts ")
                    self.score(5)
                else:
                    ms.showinfo("0_0 Error","zero")
            elif entry > 0 and entry < 10:
                if reponse == listdix[entry-1]:
                    ms.showinfo("0_0 Success","BRAVO vous avez gagne 10 pts ")
                    self.score(10)
                else:
                    ms.showinfo("0_0 Error",listdix[entry-1])
            elif entry >= 10 and entry < 100:
                if entry == 10:
                    if reponse == "dix":
                        ms.showinfo("0_0 Success","BRAVO vous avez gagne 12 pts ")
                        self.score(12)
                    else:        
                        ms.showinfo("0_0 Error","dix")
                else:
                    if entry > 10 and entry <= 16:
                        lettre = listexcept[entry-11]
                        if reponse == lettre:
                            ms.showinfo("0_0 Success","BRAVO vous avez gagne 30 pts ")
                            self.score(30)
                        else:
                            ms.showinfo("0_0 Error",lettre)
                    else:   
                        first = entry // 10
                        second = entry % 10
                        if second != 0:
                            lettre = listcentaines[first-1] + "-" + listdix[second-1]
                        else:
                            lettre = listcentaines[first-1]
                        if reponse == lettre:
                            ms.showinfo("0_0 Success","BRAVO vous avez gagne 50pts")
                            self.score(50)
                        else:
                            ms.showinfo("0_0 Error",lettre)
            elif entry >= 100 and entry < 1000:
                if entry == 100:
                    if reponse == "cent":
                        ms.showinfo("0_0 Success","BRAVO vous avez gagne 200 pts")
                        self.score(200)
                    else:        
                        ms.showinfo("0_0 Error","cent")
                else:
                    first = entry // 100
                    second = (entry % 100)//10
                    third =  (entry % 100)%10
                    concat1 = listdix[first-1] + "-"
                    concat2 =  "-" + listcentaines[second-1]
                    concat3 =  "-" + listdix[third-1]
                    if first == 1:
                        concat1 = ""
                    if second == 0:
                        concat2 =  ""
                    if third == 0:
                        concat3 =  "" 
                
                    lettre = concat1 + "cent" + concat2 + concat3
                          
                    if second == 1:
                        if third == 1:
                             lettre = concat1 + "cent" + "onze"
                        if third == 2:
                             lettre = concat1 + "cent-" + "douze"
                        if third == 3:
                             lettre = concat1 + "cent-" + "treize"
                        if third == 4:
                             lettre = concat1 + "cent-" + "quatorze"
                        if third == 5:
                             lettre = concat1 + "cent-" + "quinze"
                        if third == 6:
                             lettre = concat1 + "cent-" + "seize"
                    if reponse == lettre:
                        ms.showinfo("0_0 Success","BRAVO vous avez gagne 250 pts ")
                        self.score(250)
                    else:        
                        ms.showinfo("0_0 Error",lettre)
            elif entry == 1000:
                if reponse == "mille":
                    ms.showinfo("0_0 Success","BRAVO vous avez gagne 300 pts")
                    self.score(300)
                else:        
                    ms.showinfo("0_0 Error","cent")
        except:
            ms.showerror("Oops!!","Nous avons rencontre une erreur dans l'execution")
        reponse = self.reponse.set("")

    def retour(self):
        self.g1f.pack_forget()
        self.acceuil.pack()
        self.retr = True 
        

    def genererc(self):
        self.chiffre = randint(0,1001)
        self.times()
        textc = str(self.chiffre)
        Label(self.g1f, text = "Nombre : ",width=20,font = ('bold',14)).grid(row=1,column=0)
        Label(self.g1f, text = textc ,width=20,font = ('bold',18)).grid(row=1,column=1)
        Label(self.g1f, text = "Equivalent en lettre : ",width=20,font = ('bold',14)).grid(row=2,column=0)
        Entry(self.g1f, textvariable = self.reponse, width=35,font = ('calibri',13)).grid(row=2,column=1)
        Label(self.g1f, text = "/!\ Ex 204: deux-cent-quatre ",width=25,font = ('calibri',10)).grid(row=3,column=0)
        Button(self.g1f, text=" Valider ",width=15, bg = 'white',fg = "green",font = ('calibri',14),command=self.function).grid(row=4,column=1)
        Button(self.g1f, text=" Retour a l'acceuil ",width=15, bg = 'white',fg = "grey",font = ('calibri',14),command=self.retour).grid(row=5,column=1)
        Label(self.g1f, text = "/!\ Delai de 50 secondes accordées ",width=25,fg = "green",font = ('calibri',10)).grid(row=6,column=0)
         
    def times(self):
        if self.time == 0: 
            ms.showinfo("Perdu (x_x)","Delai depasse")
            self.time = 51
            self.genererc()
        else:
            if self.valid:
                self.valid = False
                self.genererc()
                self.time = 51
            elif self.retr:
                pass
            else:
                self.time -=1
                textc = str(self.time)
                Label(self.g1f, text = textc, width=25, font = ('agency fb',45),fg = "red",padx = 4 , pady = 4).grid(row=0,column=1)
                self.g1fcar.pack()
                self.g1fcar.after(500,self.times)

    def widgets(self):
        Button(self.g1f, text=" Generer un chiffre",width=15, bg = 'white',fg = "blue", font = ('calibri',14),command=self.genererc).grid(row=4,column=0)
        self.g1f.pack()
    
        
    
