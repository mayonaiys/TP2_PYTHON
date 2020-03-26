from noeud import Noeud

class Graphe:
    """Classe Graphe."""
    id = 1

    def __init__(self):
        Graphe.id+=1
        self._id=Graphe.id
        self._dictNoeuds = {}
        self._nbrNoeuds = 0
        self._dictLiens = {}

    def getNbrNoeuds(self):
        return self._nbrNoeuds

    def ajouterNoeud(self,Noeud):
        self._nbrNoeuds+=1
        self._dictNoeuds[Noeud.getId()]=Noeud

    def ajouterLien(self,Lien):
        self._dictNoeuds[Lien.getId()]=Lien

    def obtenirProchainsNoeuds(self,id):


