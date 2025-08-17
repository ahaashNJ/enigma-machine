import pygame
pygame.init()

from keyboard import Keyboard
from plugboard import Plugboard
from rotor import Rotor
from reflector import Reflector
from enigma import Enigma

# setup pygame
pygame.init()
pygame.font.init()
pygame.display.set_caption("Enigma Simulator")

# create fonts
MONO = pygame.font.SysFont("Freemono", 25)
BOLD = pygame.font.SysFont("FreeMono", 25, bold=True)

# global variables
WIDTH = 1200
HEIGHT = 700
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# historical enigma rotors and reflectors
I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
II  = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
III = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
IV = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
V = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")
A = Reflector("EJMZALYXVBWFCRQUONTSPIKHGD")
B = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
C = Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")

# keyboards and plugboards
KB = Keyboard()
PB = Plugboard(["AB", "CD", "EF"])

# encipher a letter
ENIGMA = Enigma(B, IV, II, I, PB, KB)

# set the rings
ENIGMA.set_rings((5,26,2))

# set message key
# ENIGMA.set_key("CAT")
# ENIGMA.rotor1.show()

# message = "TESTINGTESTINGTESTINGTESTING"
# cipher_text = ""
# for letter in message:
#     cipher_text = cipher_text + ENIGMA.encipher(letter)
# print(cipher_text)
# print(ENGIMA.encipher("A"))

animating = True
while animating:

    # background
    SCREEN.fill("#333333")

    # draw enigma machine
    KB.draw(SCREEN, 1000, 100, 100, 500, BOLD)
    PB.draw(SCREEN, 800, 100, 100, 500, BOLD)

    # update screen
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            animating= False