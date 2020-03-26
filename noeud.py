class Noeud:
    """Class Noeud"""

    id=1

    def __init__(self):
        Noeud.id+=1
        self.__id=Noeud.id
        self.__list= list()

    def __str__(self):
        print(self.__id)

    def affichageIdentifiantLien(self):
        for i in range (0,len(self.__list)):
            print(self.__list[i])
            print("\n")

    def getId(self):
        return self.__id

    def ajouterIdentifiantLien(self,idLien):
        self.__list.append(idLien)
