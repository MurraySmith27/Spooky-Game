import pygame
import Characters
"""
def action_beat_p1(window, Char, biting, punching, kicking):

    if biting:
        Char.bite()
        global p1_dobite
        p1_dobite = False
    elif punching:
        Char.punch()
        global p1_dopunch
        p1_dopunch = False
    elif kicking:
        Char.kick()
        global p1_dokick
        p1_dokick = False

    pygame.draw.rect(window, (255, 0, 0), (200,200, 70, 70))


def prep_beat_p1(window, Char, p1_bite, p1_punch, p1_kick):

    if p1_bite:
        Char.biteprep()
        global p1_dobite
        p1_dobite = True
    elif p1_punch:
        Char.punchprep()
        global p1_dopunch
        p1_dopunch = True
    elif p1_kick:
        Char.kickprep()
        global p1_dokick
        p1_dokick = True

    pygame.draw.rect(window, (0, 255, 0), (200, 200, 70, 70))

"""
def action_beat_p2(window, Char, biting, punching, kicking):

    if biting:
        Char.bite()
        global p2_dobite
        p2_dobite = False
    elif punching:
        Char.punch()
        global p2_dopunch
        p2_dopunch = False
    elif kicking:
        Char.kick()
        global p2_dokick
        p2_dokick = False

    pygame.draw.rect(window, (255, 0, 0), (370,200, 70, 70))

def prep_beat_p2(window, Char, p2_bite, p2_punch, p2_kick):

    if p2_bite:
        Char.biteprep()
        global p2_dobite
        p2_dobite = True
    elif p2_punch:
        Char.punchprep()
        global p2_dopunch
        p2_dopunch = True
    elif p2_kick:
        Char.kickprep()
        global p2_dokick
        p2_dokick = True

    pygame.draw.rect(window, (0, 255, 0), (370, 200, 70, 70))