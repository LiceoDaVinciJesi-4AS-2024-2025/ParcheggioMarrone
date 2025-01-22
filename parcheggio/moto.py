#Diego Marrone
#moto

import veicolo

class Moto:
    
    def __init__(self , targa: list):
        super().__init__(targa)
        self.__maxPasseggeri = maxPasseggeri
        self.__passeggeri = ""
        
        if maxPasseggeri < 1 or maxPasseggeri > 2:
            raise ValueError("Non è possibile avere questo numero di passeggeri")
    @property
    def maxPasseggeri(self):
        return self.__maxPasseggeri
    @maxPasseggeri.setter
    def maxPasseggeri(self , value:str):
        self.__maxPasseggeri = value
        return
    
    @property
    def passeggeri(self):
        return self.__passeggeri
    @passeggeri.setter
    def passeggeri(self , value:str):
        self.__passeggeri = value
        return
    
    def __str__(self):
        return "moto: " + str(self.__dict__)
    
    def __repr__(self):
        return "moto: " + str(self.__dict__)
    
if __name__=="__main__":
    v = veicolo.Veicolo("AB 123 CD")
    v.marca = "Lamborghini"
    v.modello = "moto"
    v.colore = "bianco"
    v.cilindrata = 2000
    v.alimentazione = "benzina"
    print(v)
    v.maxPasseggeri = 2
    v.passeggeri = 1
    print(v)