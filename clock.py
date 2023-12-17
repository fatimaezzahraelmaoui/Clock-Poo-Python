class Temps:
    def __init__(self,h,m,s):
        self.__heures = h
        self.__minutes = m
        self.__seconds = s

    def getHours(self):
        return self.__heures
    def getMin(self) :
        return self.__minutes
    def getSec(self) :
        return self.__seconds
       
    def getTemps(self):
        print(self.__heures,"h ",self.__minutes,"min ",self.__seconds,"s")    
   

    def ajouterTemps(self,t1,t2):
        self.__seconds= t1 + t2
        self.__minutes = t1 + t2 + (int(self.__seconds/60))
        self.__heures = t1 + t2 + (int(self.__minutes/60))

t1 = Temps(4,43,59)
t2 = Temps(1,20,32)
t1.ajouterTemps(2,14)
t1.getTemps()