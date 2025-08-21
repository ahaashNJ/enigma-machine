import pygame

def draw(enigma, path, screen, width, height, margins, gap, font):

    # base coordinates
    x = margins["left"]
    y = margins["top"]
    w = (width - margins["left"] - margins["right"] - 5 * gap) / 6
    h = height - margins["top"] - margins["bottom"]

    # enigma components
    for component in [enigma.reflector, enigma.rotor1, enigma.rotor2, enigma.rotor3, enigma.plugboard, enigma.keyboard]:
        component.draw(screen, x, y, w, h, font)
        x += w +gap



