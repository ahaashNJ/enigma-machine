import pygame

def draw(enigma, path, screen, width, height, margins, gap, font, error_message: str | None = None):

    # width and height of components
    w = (width - margins["left"] - margins["right"] - 5 * gap) / 6
    h = height - margins["top"] - margins["bottom"]

    # path coordinates
    y = [margins["top"]+(signal+1)*h/27 for signal in path]
    x = [width-margins["right"]-w/2] # keyword
    for i in [4,3,2,1,0]: # forward pass
        x.append(margins["left"]+i*(w+gap)+w*3/4)
        x.append(margins["left"]+i*(w+gap)+w*1/4)
    x.append(margins["right"]+w*3/4) #lampboard
    for i in [1,2,3,4]: # backward pass
        x.append(margins["left"]+i*(w+gap)+w*1/4)
        x.append(margins["left"]+i*(w+gap)+w*3/4)
    x.append(width-margins["right"]-w/2) #lampboard

    # daw the path
    if len(path) > 0:
        for i in range(1,21):
            if i < 10:
                color = "#43aa8b"
            elif i < 12:
                color = "#f9c74f"
            else:
                color = "#e63946"
            start = (x[i-1],y[i-1])
            end = (x[i],y[i])
            pygame.draw.line(screen, color, start, end, width=5)
    

    # base coordinates
    x = margins["left"]
    y = margins["top"]
    w = (width - margins["left"] - margins["right"] - 5 * gap) / 6
    h = height - margins["top"] - margins["bottom"]

    # draw enigma components
    for component in [enigma.reflector, enigma.rotor1, enigma.rotor2, enigma.rotor3, enigma.plugboard, enigma.keyboard]:
        component.draw(screen, x, y, w, h, font)
        x += w +gap

    # add titles
    names = ["Reflector", "Left", "Middle", "Right", "Plugboard", "Key/Lamp"]
    y = margins["top"]*0.8
    for i in range(6):
        x = margins["left"] + w/2 + i*(w+gap)
        title = font.render(names[i], True, "white")
        text_box = title.get_rect(center = (x,y))
        screen.blit(title, text_box)

    # error
    if error_message:
        banner_h = 40
        banner_w = width - margins["left"] - margins["right"]
        banner_x = margins["left"]
        banner_y = margins["top"] + 500

        banner = pygame.Surface((banner_w, banner_h), flags=pygame.SRCALPHA)
        banner.fill((30, 30, 30, 200))
        screen.blit(banner, (banner_x, banner_y))

        err_text = font.render(error_message, True, (240, 128, 128))
        err_rect = err_text.get_rect(center=(width // 2, banner_y + banner_h // 2))
        screen.blit(err_text, err_rect)



