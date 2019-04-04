import sqlite3
from tkinter import *
from tkinter import messagebox as ms
from Classes.user import User
from Games.chiffre import Chiffre
from Games.calcul import Calcul
from datetime import datetime, date

db = sqlite3.connect("GenieEnHerbe_BD.db")
cursur = db.cursor()
class main():

    def __init__(self,master):        
        self.master = master
        self.user = User()
        self.idcon = ""
        self.user.idmail = StringVar()
        self.user.password = StringVar()
        self.user.nom = StringVar()
        self.user.age = IntVar()
        self.user.niveau =  ""
        self.user.score = 0
        self.acf = Frame(self.master, padx = 30, pady = 30)
        self.qcpf = Frame(self.master, padx = 30, pady = 30)
        self.crf = Frame(self.master,padx = 30,pady = 30)
        self.widgets()

    def set_date(self):
        temps = datetime.now()
        self.times = temps.hour*360 + temps.minute*60
        self.today = temps.date()
        self.iddate = self.today.year*10000 + self.today.month*100 + self.today.day

    def difDate(self,dat):#prend une date en parametre et retourne la difference avec la date actuelle en jours pour compter le nombre jours d'inactivite
        dif = self.today - dat 
        dif = dif.days
        return dif
    
    def login(self):
        find_user = ("SELECT * FROM user WHERE idmail = ? AND password = ?")
        cursur.execute(find_user,[(self.user.idmail.get()),(self.user.password.get())])
        if cursur.fetchall():
            #Message d'acceuil
            self.set_date() #recuperer la date d'aujourd'hui
            find_niveau = ("SELECT niveau FROM user WHERE idmail = ? ") 
            cursur.execute(find_niveau,[(self.user.idmail.get())])
            niveau = cursur.fetchone() #recuperer son niveau 
            find_score = ("SELECT score FROM user WHERE idmail = ?")
            cursur.execute(find_score,[(self.user.idmail.get())])
            score = cursur.fetchone() #recuperer son score
            find_nom = ("SELECT nom FROM user WHERE idmail = ?")
            cursur.execute(find_nom,[(self.user.idmail.get())])
            nom = cursur.fetchone() #recuperer son nom
            find_dateid = ("SELECT iddate FROM session WHERE idmail = ? ORDER BY iddate DESC")
            cursur.execute(find_dateid,[(self.user.idmail.get())])
            dateid = cursur.fetchone() #recuperer l'id de sa derniere date de connection
            if dateid != None :
                find_dateid = ("SELECT * FROM date WHERE iddate = ? ")
                cursur.execute(find_dateid,[(dateid[0])])
                dates = cursur.fetchone()
                dat = date(dates[3],dates[2],dates[1])
                if score != None:
                    if self.iddate==dateid[0]:
                        concat = "Bienvenue " + nom[0] + "\nDerniere connexion : Aujourdhui\nScore actuel : " + str(score[0]) + "\nNiveau : " +str(niveau[0])
                        ms.showinfo("Bonjour",concat)
                    else:
                        inactif = self.difDate(dat)
                        if inactif == 1:
                             concat = "Bienvenue " + nom[0] + "\nDerniere connexion : Hier\n" + "Score actuel : " + str(score[0]) + "\nNiveau : " +str(niveau[0])
                        else:
                             concat = "Bienvenue " + nom[0] + "\nDerniere connexion :/!\ Il y'a " + str(inactif) +  " jour(s)\nScore actuel : " + str(score[0]) + "\nNiveau : " +str(niveau[0]) 
                        ms.showinfo("Bonjour",concat)
            else:
                concat = "Bienvenue a bord\nJe pense que c'est votre premiere fois ici\nO_0 Allez au travail !!"
                ms.showinfo("Hello !",concat)
            #Insertion des donnees de la date 
            find_date = ("SELECT * FROM date WHERE iddate = ? ")
            cursur.execute(find_date,[(self.iddate)])
            if cursur.fetchall():
                pass
            else:
                insert_date = ("INSERT INTO date(iddate,jour,mois,annee) VALUES (?,?,?,?)")
                cursur.execute(insert_date,[(self.iddate),(self.today.day),(self.today.month),(self.today.year)])
                db.commit()
            #Insertion des donnees de la session 
            insert_session = ("INSERT INTO session(idsession,idmail,iddate,heureConnect,heureDeconnect) VALUES(?,?,?,?,?)")
            cursur.execute(insert_session,[(None),(self.user.idmail.get()),(self.iddate),(self.times),(None)])
            db.commit()
            self.acceuil()
        else:
            ms.showerror("Oops!! ", "Nom d'utilisateur ou Mot de passe incorrect !")
            
        #re-initialisation a leurs valeurs par defaut
        self.user.idmail.set("")
        self.user.password.set("")
                    
    def new_user(self):
         find_user = ("SELECT * FROM user WHERE idmail = ? ")
         cursur.execute(find_user,[(self.user.idmail.get())])
         if cursur.fetchall():
            ms.showerror("Oops","Nom d'utilisateur existant")
         else:
             try:
                mypassword = self.user.gen_password(10)
                insert  = "INSERT INTO user(idmail,password,nom,age,niveau,score) VALUES (?,?,?,?,?,?)"
                cursur.execute(insert,[(self.user.idmail.get()),(mypassword),(self.user.nom.get()),(self.user.age.get()),(self.user.set_niveau(self.user.age.get())),(0)])
                db.commit()
                ms.showinfo("Success!!","Compte cree avec succes")
                concat = "Mot de passe genere : " + mypassword  + "\n/!\ A ne pas communiquer"
                ms.showinfo("Success!!",concat)
                self.log() 
             except:
                ms.showinfo("Erreurs rencontres", "Conseil:\n-L'age saisi est une valeur entiere\n-L'age est compris entre [1,18[")
         #re-initialisation a leurs valeurs par defaut 
         self.user.idmail.set("")
         self.user.password.set("")
         self.user.nom.set("")
         self.user.age.set(0)
         self.user.niveau = "" 
         self.user.score = 0

    
    def acceuil(self):
         self.idcon = self.user.idmail.get()
         self.user.password.set("")
         self.logf.pack_forget()
         self.head['text'] = " Genie en Herbe | Acceuil"
         self.acf.pack()
         
    def qpc(self):
         self.acf.pack_forget()
         self.head['text'] = " Questions pour un Champion"
         self.qcpf.pack()

    def game1qpc(self):
         age = 0
         self.chiffre = Chiffre(self.master)
         self.chiffre.idmail = self.idcon
         self.chiffre.acceuil = self.acf
         find_user = ("SELECT age FROM user WHERE idmail = ? ")
         cursur.execute(find_user,[(self.idcon)])
         age = cursur.fetchone()
         find_niveau = ("SELECT niveau FROM user WHERE idmail = ? ") 
         cursur.execute(find_niveau,[(self.idcon)])
         test_niveau = cursur.fetchone()
         if age[0] > 9:
             niveau = "Niveau : " + str(test_niveau[0])
             ms.showinfo("Acces autorise",niveau)
             self.qcpf.pack_forget()
             self.chiffre.widgets()
         else:
             niveau = "Votre niveau : "+ str(test_niveau[0]) + " ne vous permet pas d'acceder a ce jeu" 
             ms.showerror("Niveau Insuffisant",niveau)

    def math(self):
        self.acf.pack_forget()
        self.head['text'] = " Mathematiques "
        self.mathf.pack()
        
    def game2math(self):
        self.mathf.pack_forget()
        self.calcul = Calcul(self.master)
        self.calcul.acceuil = self.acf
        self.calcul.idmail = self.idcon
        self.calcul.widgets()
        
         
    def log(self):
         self.user.idmail.set("")
         self.user.password.set("")
         self.crf.pack_forget()
         self.head['text'] = " LOGIN "
         self.logf.pack()

    def cr(self):
        self.user.idmail.set("")
        self.user.password.set("")
        self.user.nom.set("")
        self.user.age.set(0)  
        self.user.niveau = "" 
        self.user.score = 0
        self.head['text'] = " CREATION DE COMPTE "
        self.logf.pack_forget()
        self.crf.pack()
                        
    def widgets(self):
        self.head = Label(root,text=" Genie En Herbe | Connection",width=30,font = ('bold',15))
        self.head.pack()
        #Debut Interface de connection
        self.logf = Frame(self.master,padx = 30 , pady = 30)
        Label(self.logf, text = "M@il: ",width=15,font = ('bold',14),padx = 10 , pady = 10).grid(row=0,sticky=W)
        Entry(self.logf, textvariable = self.user.idmail,width=25,font = ('calibri',13)).grid(row=0,column=1,sticky=E)
        
        Label(self.logf, text = "Password: ",width=15, font = ('bold',14),padx = 10 , pady = 10).grid(row=1,column=0,sticky=W)
        Entry(self.logf, textvariable = self.user.password,width=25,font = ('calibri',13),show = "*").grid(row=1,column=1,sticky=E)
        
        Button(self.logf,text="  Login ",width=15, fg ='green',font = ('bold',14),command=self.login).grid(row=2,column=0,sticky=W)
        Button(self.logf,text="  Inscription ",width=15, fg = 'grey',font = ('bold',14),command=self.cr).grid(row=2,column=1,sticky=E)
        self.logf.pack()
        #Fin Interface de connection 

        #Debut Interface creation de compte
        Label(self.crf, text = "Fullname: ",width=15,font = ('bold',14),padx = 10 , pady = 10).grid(sticky=W)
        Entry(self.crf, textvariable = self.user.nom,width=25,font = ('calibri',13)).grid(row=0,column=1,sticky=E)
        
        Label(self.crf, text = "M@il: ",width=15,font = ('bold',14),padx = 10 , pady = 10).grid(row=1,column=0,sticky=W)
        Entry(self.crf, textvariable = self.user.idmail,width=25,font = ('calibri',13)).grid(row=1,column=1,sticky=E)

        Label(self.crf, text = "Age: ", width=15,font = ('bold',14),padx = 10 , pady = 10).grid(row=3,column=0,sticky=W)
        Entry(self.crf, textvar = self.user.age,width=25,font = ('calibri',13)).grid(row=3,column=1,sticky=E)
        
        Button(self.crf,text=" Retour -> ",width=15, fg = 'red',font = ('bold',14),command=self.log).grid(row=6,column=0,sticky=W)
        Button(self.crf,text=" Valider ",width=15, fg ='green',font = ('bold',14),command=self.new_user).grid(row=6,column=1,sticky=E)
        Label(self.crf, text = "/!\ NB : Mot de passe genere", padx = 10 , pady = 10,fg ='red', font = ('cambria',10)).grid(row=7)
        #Fin Interface creation de compte

        #Debut Interface d'acceuil
        Button(self.acf,text=" Mathematiques ",width=30, padx = 10, pady = 15, fg ='green',font = ('calibri',14),command=self.math).grid(sticky=W)
        Button(self.acf,text=" Questions pour un champion ",width=30, padx = 10, pady = 15, fg ='blue',font = ('calibri',14),command=self.qpc).grid(row=1,sticky=W)
        #Fin Interface d'acceuil

        #Debut Interface questions pour un champion
        Button(self.qcpf,text=" Chiffre a Lettre ",width=40, padx = 40, pady = 10,font = ('calibri',14),command=self.game1qpc).grid(sticky=W)
        #Fin Interface

        #Debut Interface Mathematiques
        self.mathf = Frame(self.master, padx = 30, pady = 30)
        Button(self.mathf,text=" Calcul Mental ",width=40, padx = 40, pady = 10,font = ('calibri',14),command=self.game2math).grid(sticky=W)
        #Fin Interface
       
        

root = Tk()
#C = Label(root,text=" Genie En Herbe | Connection",width=30,font = ('bold',15))
C = Canvas(root, height=71, width=125) 
filename = PhotoImage(file = "logo.png") 
background_label = Label(root, image=filename)
background_label.place(x=0, y=0,relwidth=1)

C.pack() 
main(root)
root.title("Genie en Herbe")
root.mainloop
    
