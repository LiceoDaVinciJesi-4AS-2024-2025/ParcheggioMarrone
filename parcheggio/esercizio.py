#Diego Marrone
#Esercizio

import postoMoto
import postoAuto
import veicolo

class Parcheggio(postoAuto.Postoauto , postoMoto.Postomoto):
    def __init__(self):
        self.__postiAuto = 1000
        self.__postiMoto = 200        
        self.__postiLiberiAuto = 0
        self.__postiLiberiMoto = 0
        self.__tipoVeicolo = ""
        self.__targaVeicolo = ""
        self.__oreSosta = "" 
    
    @property
    def postiAuto(self):
        return self.__postiAuto
        
    @property
    def postiMoto(self):
        return self.__postiMoto
    
    @property
    def postiLiberiAuto(self):
        return self.__postiLiberiAuto
    
    @property
    def postiLiberiMoto(self):
        return self.__postiLiberiMoto

    @property
    def tipoVeicolo(self):
        return self.__tipoVeicolo
    
    @property
    def targaVeicolo(self):
        return self.__targaVeicolo
    
    @property
    def oreSosta(self):
        return self.__oreSosta
        
        
    def __str__(self):
        return "Parcheggio:" + str(self.__dict__)
    
    def __repr__(self):
        return "Parcheggio:" + str(self.__dict__)
    
    def prenotaPosto(self , veicolo:veicolo.Veicolo):
        if self.__parcheggioOccupato == False:
            self.__tipoVeicolo = tipoVeicolo
            self.__targaVeicolo = veicolo
        return True
     
    def contoGuadagno(self):
        if self.__postiLiberiAuto > 0 or self.__postiLiberiMoto > 0:
        
        return 
   
   
         
if __name__=="__main__":
      p = Parcheggio
        
        
        
        