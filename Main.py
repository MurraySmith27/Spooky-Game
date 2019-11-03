import pygame
from BeatHandler import *
from Characters import Player1, Player2
from Constants import *


pygame.init()

clock = pygame.time.Clock()

bps = BEATS_PER_SECOND

font = pygame.font.Font(None, 30)



def action_beat_p1(window, Char, biting, punching, kicking, block_bite, block_punch, block_kick):

    global p1_sprite_name
    if biting:
        Char.bite(block_bite)
        global p1_dobite
        p1_dobite = False
        p1_sprite_name = p1_fighter + '_bite'
    elif punching:
        Char.punch(block_punch)
        global p1_dopunch
        p1_dopunch = False
        p1_sprite_name = p1_fighter + '_punch'
    elif kicking:
        Char.kick(block_kick)
        global p1_dokick
        p1_dokick = False
        p1_sprite_name = p1_fighter + '_kick'

    pygame.draw.rect(window, (255, 0, 0), (200,200, 70, 70))

def prep_beat_p1(window, Char, p1_bite, p1_punch, p1_kick):

    global p1_sprite_name
    if p1_bite:
        Char.biteprep()
        global p1_dobite
        p1_dobite = True
        p1_sprite_name = p1_fighter + '_bite_prep'
    elif p1_punch:
        Char.punchprep()
        global p1_dopunch
        p1_dopunch = True
        p1_sprite_name = p1_fighter + '_punch_prep'
    elif p1_kick:
        Char.kickprep()
        global p1_dokick
        p1_dokick = True
        p1_sprite_name = p1_fighter + '_kick_prep'

    pygame.draw.rect(window, (0, 255, 0), (200, 200, 70, 70))

def action_beat_p2(window, Char, biting, punching, kicking, block_bite, block_punch, block_kick):


    global p2_sprite_name
    if biting:
        Char.bite(block_bite)
        global p2_dobite
        p2_dobite = False
        p2_sprite_name = p2_fighter + '_bite'

    elif punching:
        Char.punch(block_punch)
        global p2_dopunch
        p2_dopunch = False
        p2_sprite_name = p2_fighter + '_punch'

    elif kicking:
        Char.kick(block_kick)
        global p2_dokick
        p2_dokick = False
        p2_sprite_name = p2_fighter + '_kick'

    pygame.draw.rect(window, (255, 0, 0), (370,200, 70, 70))
def prep_beat_p2(window, Char, p2_bite, p2_punch, p2_kick):

    global p2_sprite_name
    if p2_bite:
        Char.biteprep()
        global p2_dobite
        p2_dobite = True
        p2_sprite_name = p2_fighter + '_bite_prep'
    elif p2_punch:
        Char.punchprep()
        global p2_dopunch
        p2_dopunch = True
        p2_sprite_name = p2_fighter + '_punch_prep'
    elif p2_kick:
        Char.kickprep()
        global p2_dokick
        p2_dokick = True
        p2_sprite_name = p2_fighter + '_kick_prep'

    pygame.draw.rect(window, (0, 255, 0), (370, 200, 70, 70))


foreground = pygame.display.set_mode(DISPLAY_SIZE)

pygame.display.set_caption("Spooooooky Game!")

beat_event = pygame.USEREVENT + 1

pygame.time.set_timer(beat_event, int((1/(bps)* 2000)))


i = True

p1_turn = True
p2_turn = False

p1_bite = False
p1_punch = False
p1_kick = False

p2_bite = False
p2_punch = False
p2_kick = False

p1_dobite = False
p1_dopunch = False
p1_dokick = False

p2_dobite = False
p2_dopunch = False
p2_dokick = False

p1_block_bite = False
p1_block_punch = False
p1_block_kick = False

p2_block_bite = False
p2_block_punch = False
p2_block_kick = False

running = True

p1_player = 'none'
p2_player = 'none'

#{'String': (Image, Image height)
p1Dracula = pygame.image.load('p1Dracula.png')
p1Dracula_bite_prep = pygame.image.load('p1Dracula_bite_prep.png')
p1Dracula_bite = pygame.image.load('p1Dracula_bite.png')
p1Dracula_punch_prep = pygame.image.load('p1Dracula_punch_prep.png')
p1Dracula_punch = pygame.image.load('p1Dracula_punch.png')
p1Dracula_kick_prep = pygame.image.load('p1Dracula_kick_prep.png')
p1Dracula_kick = pygame.image.load('p1Dracula_kick.png')
p2Dracula = pygame.image.load('p2Dracula.png')
p2Dracula_bite_prep = pygame.image.load('p2Dracula_bite_prep.png')
p2Dracula_bite = pygame.image.load('p2Dracula_bite.png')
p2Dracula_punch_prep = pygame.image.load('p2Dracula_punch_prep.png')
p2Dracula_punch = pygame.image.load('p2Dracula_punch.png')
p2Dracula_kick_prep = pygame.image.load('p2Dracula_kick_prep.png')
p2Dracula_kick = pygame.image.load('p2Dracula_kick.png')

p1Sprites= {'p1Dracula': (p1Dracula, 40), 'p1Dracula_bite_prep': (p1Dracula_bite_prep, 43),
            'p1Dracula_bite': (p1Dracula_bite, 43),'p1Dracula_punch_prep': (p1Dracula_punch_prep, 40),
            'p1Dracula_punch': (p1Dracula_punch, 38), 'p1Dracula_kick_prep': (p1Dracula_kick_prep, 40),
            'p1Dracula_kick': (p1Dracula_kick, 40)}

p2Sprites= {'p2Dracula': (p2Dracula, 40), 'p2Dracula_bite_prep': (p2Dracula_bite_prep, 43),
            'p2Dracula_bite': (p2Dracula_bite, 43),'p2Dracula_punch_prep': (p2Dracula_punch_prep, 40),
            'p2Dracula_punch': (p2Dracula_punch, 38), 'p2Dracula_kick_prep': (p2Dracula_kick_prep, 40),
            'p2Dracula_kick': (p2Dracula_kick, 40)}

p1_sprite = None

p2_sprite = None

p1_sprite_name = ''

p2_sprite_name = ''

while not(p1_sprite_name == 'p1Dracula'):
    p1_sprite_name = input("Which character would you like to be player 1? (p1Dracula, p1Horseman)")
    p1_sprite = p1Sprites[p1_sprite_name][0]
while not(p2_sprite_name == 'p2Dracula'):
    p2_sprite_name = input("Which character would you like to be player 2? (p2Dracula, p2Horseman)")
    p2_sprite = p2Sprites[p2_sprite_name][0]

p1_fighter = p1_sprite_name
p2_fighter = p2_sprite_name
p1 = Player1(0, 0, 0, 0, P2_HEALTH, 1)
p2 = Player2(0, 0, 0, 0, P1_HEALTH, p2Sprites[p2_sprite_name][0])

while running:

    pygame.draw.rect(foreground, (0,0,0), (0, 0, DISPLAY_SIZE[0], DISPLAY_SIZE[1]))

    pygame.draw.rect(foreground, (100,100,100), (0, DISPLAY_SIZE[1] - 200, DISPLAY_SIZE[0], 200))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                p1_bite = True
                b1_block_bite = True
            if event.key == pygame.K_d:
                p1_punch = True
                p1_block_punch = True
            if event.key == pygame.K_s:
                p1_kick = True
                p1_block_kick = True
            if event.key == pygame.K_UP:
                p2_bite = True
                p2_block_bite = True
            if event.key == pygame.K_LEFT:
                p2_punch = True
                p2_block_punch = True
            if event.key == pygame.K_DOWN:
                p2_kick = True
                p2_block_kick = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                p1_bite = False
                p1_block_bite = False
            if event.key == pygame.K_d:
                p1_punch = False
                p1_block_punch = False
            if event.key == pygame.K_s:
                p1_kick = False
                p1_block_kick = False
            if event.key == pygame.K_UP:
                p2_bite = False
                p2_block_bite = False
            if event.key == pygame.K_LEFT:
                p2_punch = False
                p2_block_punch = False
            if event.key == pygame.K_DOWN:
                p2_kick = False
                p2_block_kick = False

        if event.type == beat_event:
            if i:
                if p1_turn:
                    prep_beat_p1(foreground, p1, p1_bite, p1_punch, p1_kick)
                    p2_sprite_name = p2_fighter
                elif p2_turn:
                    p2_player = prep_beat_p2(foreground, p2, p2_bite, p2_punch, p2_kick)
                    p1_sprite_name = p1_fighter
                i = False
            elif not i:
                if p1_turn:
                    action_beat_p1(foreground, p1, p1_dobite, p1_dopunch, p1_dokick, p2_block_bite, p2_block_punch, p2_block_kick)
                    p1_turn = False
                    p2_turn = True
                elif p2_turn:
                    action_beat_p2(foreground, p2, p2_dobite, p2_dopunch, p2_dokick, p1_block_bite, p1_block_punch, p1_block_kick)
                    p1_turn = True
                    p2_turn = False

                i = True

    fps = font.render(str(int(clock.get_fps())), True, pygame.Color('white'))

    p1_sprite_height = p1Sprites[p1_sprite_name][1]
    P1_POSITION = (5 * (DISPLAY_SIZE[0]) // 10, DISPLAY_SIZE[1] - 200 - p1_sprite_height)
    p2_sprite_height = p2Sprites[p2_sprite_name][1]
    P2_POSITION = (6 * (DISPLAY_SIZE[0]) // 10, DISPLAY_SIZE[1] - 200 - p2_sprite_height)

    foreground.blit(p1Sprites[p1_sprite_name][0], P1_POSITION)
    foreground.blit(p2Sprites[p2_sprite_name][0], P2_POSITION)


    foreground.blit(fps, (50, 50))

    p1.update()
    p2.update()

    pygame.display.flip()
    clock.tick(60)


pygame.quit()
quit()