# Genie_en_herbe
Projet destine a aider des enfants dans leur apprentissage scolaire  avec des jeux leur permettrant de maitriser les fondamentaux
#      ~=~=~=~Ce document n'a pas but a etre compiler ou executer elle existe juste dans un but explicatif~=~=~=~  

# Explication du code de l'application
from sqlite3 import * #Importation du module sqlite3 pour gerer la base de donnee
from random import randint #Importation du module random en fesant appel a la fonction randint qui genere un nombre aleatoire dans un intervalle defini
from datetime import datetime, date  
from time import *

#Scenario:
#    * Login-> Pour juste utiliser cette fonction de connection il vous faut acceder simplement au fichier "Exportation.sql"
#              et vous verrez les utilisateurs deja crees dans la table user avec leurs informations de connection
#    * Inscription-> Pour tester cette fonction il vous faudra necessairement un sqlite browser pour pouvoir acceder aux donnees nouvellement crees  

#PRE-REQUIS:
#-Python 3
#-Sqlite Studio ou un autre Sqlite Browser pour vous aider a recuperer les donnees en temps reel

#-CLASSES-
# Contient les classes relatifs a l'application :
#    * Date: renseigne la date
#            -iddate Primary Key
#            -jour
#            -mois
#            -annnee
#    * Session: elle contient les informations de connection propre a une session pour un utilisateur
#            -idsession Primary Key
#            -idmail Foreign Key
#            -iddate Foreign Key
#            -heureConnect -> L'heure de connection exprime en secondes
#            -heureDeconnect -> L'heure de deconnection exprime en secondes        
#    * User:
#            -idmail Primary Key
#            -password
#            -nom
#            -age
#            -niveau -> renseigne le  niveau d'un utilisateur
#            -score -> Mise a jour a chaque bonne reponse

#-GAMES-
# Deux sous parties dans lesquelles nous avons :
# `     - Une Partie mathematique pour les calculs mentaux
#            Dans cette partie nous retrouvons un seul jeu pour l'instant
#                           ~Cacul Mental~
#            Nous allons vous aider a etre un as du calcul mental prenez tous votre temps aucun delai ne vous est pose
#            Tout ce qui vous reste a faire c'est de trouver le bon resultat
#       - Une Partie Question pour un champion pour l'apprentissage des lettres
#            Dans cette partie nous retrouvons un seul jeu pour l'instant
#                           ~Chiffre a Lettre~
#            Dans ce jeu va vous etre donne un nombre au hasard et vous devez donner son equivalent en lettres
#                                Exemple : 204
#                                          deux-cent-quatre
#                                NB: N'oubliez surtout pas de preciser les ' - ' entre les lettres cela est tres important

#Je n'est pas ete en mesure d'y mettre toutes les fonctions donc j'ai fait le choix d'en expliquer certaines qui me paraissaient importantes ou implicites
dates = date(2018,6,25)
def generer_mdp(n): #retourne un mot de passe de facon aleatoire
    i = 0
    lettre = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
    motdepasse = "" #iniatialise au depart va recevoir une serie de lettre de facon aleatoire jusqu'a 10 caracteres
    while i<n:
        c = randint(0,61)#genere un chiffre de facon aleatoire
        motdepasse += lettre[c]# Ce chiffre va etre puise dans cette liste de possibilite et concatene dans la variable mot de passe
        i+=1
    return motdepasse

def conversionId(code):#retourne un id sous 10 caracteres 
    return "{0:010}".format(code)

def dateToint():#prend une date en parametre et retourne un int qui servira d'id
    temps = datetime.now()
    today = temps.date()
    iddate = today.year*10000 + today.month*100 + today.day#cette id sera forme des arguments de la date et permettra une lecture facile
    return iddate
    
    
def difDate(dates):#prend une date en parametre et retourne la difference avec la date actuelle en jours pour compter le nombre jours d'inactivite
    temps = datetime.now()
    today = temps.date()
    dif = today - dates 
    dif = dif.days
    return dif 

#---------START---------
#        ~ main() ~
# Cette classe est la base du programme a l'execution de ce code vous lancerez l'application


