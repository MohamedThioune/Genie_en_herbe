from datetime import *

class Date:

    def __init__(self):
        temps = datetime.now()
        today = temps.date()
        self._iddate = today.year*10000 + today.month*100 + today.day
        self._jour = today.day
        self._mois = today.month*100
        self._annee = today.year*10000

    def _get_iddate(self):
        return self._iddate
    def _set_iddate(self,news_values):
        self._iddate = news_values
        
    def _get_jour(self):
        return self._jour
    def _set_jour(self,news_values):
        self._jour = news_values
        
    def _get_mois(self):
        return self._mois
    def _set_mois(self,news_values):
        self._mois = news_values
        
    def _get_annee(self):
        return self._iddate
    def _set_annee(self,news_values):
        self._annee = news_values

    def __repr__(self):
        return "|Date|\n id: {}\n jour: {}\n mois: {}\n annee: {}".format(self.iddate,self.jour,self.mois,self.annee)
    iddate = property(_get_iddate,_set_iddate)
    jour = property(_get_jour,_set_jour)
    mois = property(_get_mois,_set_mois)
    annee = property(_get_annee,_set_annee)
