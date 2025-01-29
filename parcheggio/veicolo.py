#Diego Marrone
#Livello 0

class Veicolo:
    def __init__(self , targa: str):
        
        alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numeri = "0123456789"
        self.__marca = ""
        self.__modello = ""
        self.__colore = ""
        self.__cilindrata = 0
        self.__alimentazione = ""
        self.__targa = targa
        
        #verifico che la targa sia corretta
        if targa[0] not in alfabeto and targa[1] not in alfabeto and targa[7] not in alfabeto and targa[8] not in alfabeto:
            raise ValueError("La targa è sbagliata")
        
        if targa[2] != " " and targa[6] != " ":
            raise ValueError("La targa è sbagliata")
        
        if targa[3] not in numeri and targa[4] not in numeri and targa[5] not in numeri:
            raise ValueError("La targa è sbagliata")
        
        if len(targa) != 9:
            raise ValueError("La targa è sbagliata")
    
    #definisco la marca
    @property
    def marca(self):
        return self.__marca  
    @marca.setter
    def marca(self , value:str):
        marche = ["lamborghini" , "ferrari" , "tesla" , "fiat"]    
        if value.lower() not in marche:
            raise ValueError("Non è possibilie avere questa marca")  
        self.__marca = value
        return
    
    #definisco il modello
    @property
    def modello(self):
        return self.__modello   
    @modello.setter
    def modello(self  , value:str):
        self.__modello = value
        return
    
    #definisco il colore
    @property
    def colore(self):
        return self.__colore
    @colore.setter
    def colore(self , value:str):
        colori = ["giallo" , "blu" , "rosso" , "verde" , "nero" , "bianco" , "grigio"]
        
        if value.lower() not in colori:
            raise ValueError("Non è possibile avere questo colore")
        self.__colore = value
        return
    
    #definisco la cilindrata
    @property
    def cilindrata(self):
        return self.__cilindrata
    @cilindrata.setter
    def cilindrata(self , value:int):
        if value % 100 != 0:
            raise ValueError("La cilindrata deve essere maggiore di 0 e un multiplo di 100")
        self.__cilindrata = value
        return 
    
    #definisco l'alimentazione
    @property
    def alimentazione(self):
        return self.__alimentazione
    @alimentazione.setter
    def alimentazione(self , value:str):
        carburanti = ["benzina" , "diesel" , "elettrica" , "metano"]
        if value.lower() not in carburanti:
            raise ValueError("Non è possibile avere questo carburante")
        self.__alimentazione = value
        return
    
    #definisco la targa
    @property
    def targa(self):
        return self.__targa
        
   
    def __str__(self):
        return "Veicolo:" + str(self.__dict__)
    
    def __repr__(self):
        return "Veicolo:" + str(self.__dict__)
    
if __name__=="__main__":
    
    v = Veicolo("AB 123 CD")
    v.marca = "Lamborghini"
    v.modello = "modello sconosciuto"
    v.colore = "bianco"
    v.cilindrata = 2000
    v.alimentazione = "benzina"
    print(v)
    