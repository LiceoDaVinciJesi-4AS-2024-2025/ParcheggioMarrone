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

    def occupaPosto(self, dataTermine:datetime.date):
        if self.__occupato == True:
            raise ValueError("Il posto" , self.__numeroPosto , "è già occupato dalla macchina" , self.__autoParcheggiata)          
        adesso = datetime.datetime.now()
        if dataTermine < adesso:
            raise ValueError("Non puoi inserire una data vecchia")
        self.__occupato = True
        self.__targaAutoParcheggiata = veicolo
        self.__dataFineOccupazione = dataFineOccupazione
        return True
    
    def liberaPosto(self):
        if self.__occupato == False:
            raise ValueError("Il posto" , self.__numeroPosto , "è già libero")
        self.__occupato = False
        self.__targaAutoParcheggiata = ""
        self.__dataFineOccupazione = ""
        return True
    
    def __str__(self):
        return "Posto: " + str(self.__dict__)
    
    def __repr__(self):
        return "Posto: " + str(self.__dict__)
    

if __name__ == "__main__":
    macchina = auto.Auto("AB 123 CD")
    macchina.marca = "Lamborghini"
    macchina.modello = "modello sconosciuto"
    macchina.colore = "bianco"
    macchina.cilindrata = 2000
    macchina.alimentazione = "benzina"
    print(v)
    macchina.maxPasseggeri = 5
    macchina.passeggeri = 1
    print(macchina)
    print()
    parcheggio1 = PostoAuto("0")
    print(parcheggio1)
    print()
    parcheggio1.occupaPosto(macchina1, datetime.datetime(2025, 2, 23, 15, 30, 0))
    print(parcheggio1)
    print()
    