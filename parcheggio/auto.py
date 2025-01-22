#Diego Marrone
#auto

import veicolo

class Auto(veicolo.Veicolo):
    
    def __init__(self , targa: str):
        super().__init__(targa)
        self.__maxPasseggeri = 5
        self.__passeggeri = 0
        
    @property
    def maxPasseggeri(self):
        return self.__maxPasseggeri
    @maxPasseggeri.setter
    def maxPasseggeri(self , value:int):
        self.__maxPasseggeri = value
        return
    
    @property
    def passeggeri(self):
        return self.__passeggeri
    @passeggeri.setter
    def passeggeri(self , value:int):
        self.__passeggeri = value
        return
    
    def __str__(self):
        return "auto: " + str(self.__dict__)
    
    def __repr__(self):
        return "auto: " + str(self.__dict__)
    
if __name__=="__main__":
    v = veicolo.Veicolo("AB 123 CD")
    v.marca = "Lamborghini"
    v.modello = "modello sconosciuto"
    v.colore = "bianco"
    v.cilindrata = 2000
    v.alimentazione = "benzina"
    print(v)
    v.passeggeri = 3
    print(v)
  
    
    
    
    
    
        
        