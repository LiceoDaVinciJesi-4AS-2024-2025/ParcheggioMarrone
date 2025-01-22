#Diego Marrone
#Livello 2

import auto
import datetime

class PostoAuto:
    
    def __init__(self, numeroPosto:str):
        self.__numeroPosto = numeroPosto
        self.__tipoParcheggio = "Auto"
        self.__parcheggioOccupato = False
        self.__targaAutoParcheggiata= ""
        self.__dataFineOccupazione = ""
        
    @property
    def numeroPosto(self):
        return self.__numeroPosto
    
    @property
    def tipoParcheggio(self):
        return self.__tipoParcheggio
    
    @property
    def occupato(self):
        return self.__parcheggioOccupato
    
    @property
    def autoParcheggiata(self):
        return self.__targaAutoParcheggiata
    
    @property
    def dataTermine(self):
        return self.__dataFineOccupazione

    def occupaPosto(self, veicolo:auto.Auto, dataTermine:datetime.date):
        if self.__occupato == True:
            raise ValueError("Il posto" , self.__numeroPosto , "è già occupato dalla macchina" , self.__autoParcheggiata)          
        adesso = datetime.datetime.now()
        if dataTermine < adesso:
            raise ValueError("Non puoi inserire una data vecchia")
        self.__occupato = True
        self.__autoParcheggiata = veicolo
        self.__dataTermine = dataTermine
        return True
    
    def liberaPosto(self):
        if self.__occupato == False:
            raise ValueError("Il posto" , self.__numeroPosto , "è già libero")
        self.__occupato = False
        self.__autoParcheggiata = ""
        self.__dataTermine = ""
        return True
    
    def __str__(self):
        return "Posto: " + str(self.__dict__)
    
    def __repr__(self):
        return "Posto: " + str(self.__dict__)
    

if __name__ == "__main__":
    macchina1 = auto.Auto("AB 123 CD")
    macchina1.marca = "Fiat"
    macchina1.modello = "Panda"
    macchina1.alimentazione = "benzina"
    macchina1.colore = "nero"
    macchina1.maxPasseggeri = 5
    macchina1.passeggeri = 1
    print(macchina1)
    print()
    parcheggio1 = PostoAuto("0")
    print(parcheggio1)
    print()
    parcheggio1.occupaPosto(macchina1, datetime.datetime(2025, 2, 23, 15, 30, 0))
    print(parcheggio1)
    print()
    