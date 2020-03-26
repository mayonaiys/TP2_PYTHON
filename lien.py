class Lien:
    """Class Lien."""

    id=1

    def __init__(self,ext1,ext2,distance):
        """Constructeur"""

        Lien.id+=1
        self.__id=Lien.id
        self.__ext1=ext1
        self.__ext2=ext2
        self.__distance=distance

    def __str__(self):
        print(self.__id)

    def getId(self):
        return self.__id

    def getExt1(self):
        return self.__ext1

    def getExt2(self):
        return self.__ext2

    def getDistance(self):
        return self.__distance

