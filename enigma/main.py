import pygame
pygame.init()

from keyboard import Keyboard
from plugboard import Plugboard
from rotor import Rotor
from reflector import Reflector
from enigma import Enigma
from draw import draw

# setup pygame
pygame.init()
pygame.font.init()
pygame.display.set_caption("Enigma Simulator")

# create fonts
MONO = pygame.font.SysFont("Freemono", 25)
BOLD = pygame.font.SysFont("FreeMono", 25, bold=True)

# global variables
WIDTH = 1400
HEIGHT = 700
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
MARGINS = {"top":150, "bottom":80, "left":100, "right":100}
GAP = 70

INPUT = ""
OUTPUT = ""
PATH = []

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
ENIGMA = Enigma(B, I, II, III, PB, KB)

# set the rings
ENIGMA.set_rings((1,1,1))

# set message key
ENIGMA.set_key("CAT")
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

    # input text
    text = BOLD.render(INPUT, True, "white")
    text_box = text.get_rect(center = (WIDTH/2, MARGINS["top"]/4))
    SCREEN.blit(text, text_box)

    # output
    text = MONO.render(OUTPUT, True, "white")
    text_box = text.get_rect(center = (WIDTH/2, MARGINS["top"]/4+25))
    SCREEN.blit(text, text_box)

    # draw engima machine
    draw(ENIGMA, PATH, SCREEN, WIDTH, HEIGHT, MARGINS, GAP, BOLD)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            animating= False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                III.rotate()
            elif event.key == pygame.K_SPACE:
                INPUT = INPUT + " "
                OUTPUT = OUTPUT + " "
            else:
                key = event.unicode
                if key in "abcdefghiklmnopqrstuvwxyz":
                    letter = key.upper()
                    INPUT = INPUT + letter
                    PATH, cipher = ENIGMA.encipher(letter)
                    OUTPUT = OUTPUT + cipher

