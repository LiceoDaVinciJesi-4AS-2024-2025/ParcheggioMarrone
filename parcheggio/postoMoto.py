#Diego Marrone
#postoMoto

import moto
import datetime

class Postomoto(moto.Moto):
    
    def __init__(self, numeroPosto:str):
        self.__numeroPosto = numeroPosto
        self.__tipoParcheggio = "Moto"
        self.__parcheggioOccupato = False
        self.__targaMotoParcheggiata= ""
        self.__dataFineOccupazione = ""
        
    #definisco tutte le caratteristiche per un parcheggio di una moto
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
    def motoParcheggiata(self):
        return self.__targaMotoParcheggiata
    
    @property
    def dataFineOccupazione(self):
        return self.__dataFineOccupazione

    def occupaPosto(self, veicolo: moto.Moto , dataFineOccupazione:datetime.date):
        #se il parcheggio è occupato ritorna errore
        if self.__parcheggioOccupato == True:
            raise ValueError("Il posto" , self.__numeroPosto , "è già occupato dalla macchina" , self.__targaMotoParcheggiata)          
        adesso = datetime.datetime.now()
        #se la data è vecchia ritorna errore
        if dataFineOccupazione < adesso:
            raise ValueError("Non puoi inserire una data vecchia")
        self.__parcheggioOccupato = True
        self.__targaMotoParcheggiata = veicolo
        self.__dataFineOccupazione = dataFineOccupazione
        return True
    
    def liberaPosto(self):
        #se il parcheggio non è occupato parcheggia la moto
        if self.__parcheggioOccupato == False:
            raise ValueError("Il posto" , self.__numeroPosto , "è già libero")
        self.__parcheggioOccupato = False
        self.__targaMotoParcheggiata = ""
        self.__dataFineOccupazione = ""
        return True
    
    def __str__(self):
        return "Parcheggio: " + str(self.__dict__)
    
    def __repr__(self):
        return "Parcheggio: " + str(self.__dict__)
    

if __name__ == "__main__":
    v = moto.Moto("AB 123 CD")
    v.marca = "Lamborghini"
    v.modello = "moto"
    v.colore = "bianco"
    v.cilindrata = 2000
    v.alimentazione = "benzina"
    v.maxPasseggeri = 2
    v.passeggeri = 1
    print(v)
    parcheggiomoto = Postomoto("14")
    print(parcheggiomoto)
    parcheggiomoto.occupaPosto(v, datetime.datetime(2025, 2, 23, 15, 30, 0))
    print(parcheggiomoto)