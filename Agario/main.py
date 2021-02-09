from Agario.Bille import Bille
from Agario.Creep import Creep
from Agario.Player import Player


#Attention variables globales
from p5 import core

player1 = None
creep1 = Creep()
bille1 = Bille()

def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [400, 400]

    global player1
    player1 = Player()

    print("Setup END-----------")

def run():
    print("run")
    player1.afficher(core)

if __name__ == "__main__":
    core.main(setup, run)