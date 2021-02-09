from Agario.Bille import Bille
from Agario.Creep import Creep
from Agario.Player import Player


#Attention variables globales
from p5 import core

player1 = None
creep1 = Creep()
bille1 = Bille()
creeps = []

def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [400, 400]

    global player1, creeps
    player1 = Player()

    for i in range(0, 1000):
        creeps.append(Creep())

    print("Setup END-----------")

def run():
    player1.afficher(core)
    if core.getMouseLeftClick() is not None:
        player1.deplacer(core.getMouseLeftClick())
    creep1.afficher(core)

    for c in creeps:
        c.afficher(core)
        #if (player1.position.x == creep1.position.x):
            #player1.manger()
#essai


if __name__ == "__main__":
    core.main(setup, run)