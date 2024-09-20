


# ____________________________ETAPE 1 : Création du deck + mélange deck____________________________

valeurs = list(range(1,14)) #génération des valeurs de 1 à 13 (1 à 10 et 11=V ; 12= D; 13= R )
couleurs = ["trefle", "pique", "carreau", "coeur"] #génération des couleurs

hauteurs = { #dictionnaire de traduction 11,12,13 en valeurs hautes V ; D et R
    11: "V",
    12: "D",
    13: "R",
    "V": "11",
    "D": "12",
    "R": "13",
}

class createDeck:
    def __init__ (self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur
                
def generateur_cartes(valeurs, couleurs):
    cartes_decks = []
    for valeur in valeurs:
        for couleur in couleurs:
            # Vérification si la valeur est une carte haute alors traductionen Valet, Dame ou Roi
            if valeur in hauteurs:
                carte_valeur = hauteurs[valeur]
            else:
                carte_valeur = valeur
            # Création d'une nouvelle carte et ajout au deck
            cartes_decks.append(createDeck(carte_valeur, couleur))
    return cartes_decks
generateur_cartes(valeurs, couleurs)
#Création du deck
cartes_decks = generateur_cartes(valeurs, couleurs)

#Mise au format liste de deck
deck = list(f"{carte.valeur} {carte.couleur}" for carte in cartes_decks)


#Création de la fonction qui mélange le deck
import random  #import pour utiliser la propriété random
def shuffle_deck(deck):
    random.shuffle(deck)
   
    return deck

# ____________________________ETAPE 2 : Var deck + fonction deal pour 2 joueurs ____________________________
deck = shuffle_deck(deck)
# for x in deck :
#     print(x)
#print(deck)
#print(type(deck)) #deck est bien une liste

def deal(nombre_cartes: int):
    cartes_retiree = []
    for x in range(nombre_cartes):
        cartes_retiree.append(deck.pop(0))
    return cartes_retiree

#print(deal(2)) #distribue nombre_cartes // a l'index 0 de la liste deck (en donnant toujours la premiére carte du deck !) 

Player1 = deal(2)
Player2 = deal(2)

# print (Player1)
# print(Player2)
# ____________________________ETAPE 3 : fonction flop ____________________________

def flop():
    cartes_brulee=[]
    cartes_sortie_flop=[]
    cartes_brulee.append(deal(1))
    cartes_sortie_flop.append(deal(3))
    #return cartes_sortie_flop
    
#    # def turn():
    #carte_brulee=[]
    carte_sortie_turn=[]
    cartes_brulee.append(deal(1))
    carte_sortie_turn.append(deal(1))
    #return carte_sortie_turn
   
   # turn()
    #print(turn())
  # def river():
    #carte_brulee=[]
    carte_sortie_river=[]
    cartes_brulee.append(deal(1))
    carte_sortie_river.append(deal(1))
    cards= cartes_sortie_flop + carte_sortie_turn + carte_sortie_river
    return cards 
  
  
print(Player1) # Main du joueur 1
print(Player2)  # Main du joueur 2
print(flop()) # Cartes sur le tapis : Flop + turn + river 