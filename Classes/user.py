import sqlite3
from tkinter import messagebox as ms
from random import randint
 
class User:

    def __init__(self):
        self.idmail = ""
        self.password = ""
        self.nom = ""
        self.age = 0
        self.niveau = ""
        self.score = 0

    """ Constructeur avec argument ignore   
    def __init__(self,idmail,password,age,niveau,score):
        self._idmail = idmail
        self._password = password
        self._age = age
        self._niveau = niveau
        self._score = score
    """
    def set_niveau(self,age):
        if age >0 and age<=4:
            self.niveau = "ROOKIE"
            return self.niveau
        elif age >=5 and age<10:
            self.niveau = "AGENT"
            return self.niveau
        elif age >=10 and age<15:
             self.niveau = "COLONEL"
             return self.niveau
        elif age >=15 and age<18:
             self.niveau = "ELITE"
             return self.niveau
            
        
    def gen_password(self,n):
        i = 0
        lettre = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
        motdepasse = ""
        while i<n:
            c = randint(0,61)
            motdepasse += lettre[c]
            i+=1
        return motdepasse
        
    def __repr__(self):
        return "|Utilisateur|\n m@il: {}\n mot de passe: {}\n age: {}\n niveau: {}\n score: {}".format(self.idmail,self.password,self.age,self.niveau,self.score)
    


