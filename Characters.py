import pygame

class Character():

    def __init__(self, _x, _y, _w, _h, _health, _fighter):
        self._x = _x
        self._y = _y
        self._w = _w
        self._h = _h
        self._health = _health


class Player1(Character):

    def __init__(self,x,y, w, h, health,fighter):
        super().__init__(x,y,w,h,health,fighter)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.health = 3

    def update(self):
        if self.health == 0:
            print('Player 2 has met their timely end! Player two is the winner!')
            pygame.quit()
            quit()

    def bite(self, block_bite):
        print('p1 bite!')
        if block_bite:
            print('p2 blocked the bite!')
        else:
            self.health -= 1
    def punch(self, block_punch):
        print('p1 punch!')
        if block_punch:
            print('p2 blocked the punch!')
        else:
            self.health -= 1

    def kick(self, block_kick):
        print('p1 kick!')
        if block_kick:
            print('p2 blocked the kick!')
        else:
            self.health -= 1

    def biteprep(self):
        print('p1 gonna bite!')

    def punchprep(self):
        print('p1 gonna punch!')

    def kickprep(self):
        print('p1 gonna kick!')

    def animate_bite(self):
        return NotImplementedError

    def animate_punch(self):
        return NotImplementedError

    def animate_kick(self):
        return NotImplementedError


class Player2(Character):

    def __init__(self, x, y, w, h, health, fighter):
        super().__init__(x, y,w,h,health,fighter)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.health = health
        self.fighter = fighter

    def update(self):
        if self.health == 0:
            print('Player 1 has met their timely end! Player 2 is the winner!')
            pygame.quit()
            quit()

    def bite(self, block_bite):
        print('p2 bite!')
        if block_bite:
            print('p1 blocked the bite!')
        else:
            self.health -= 1

    def punch(self, block_punch):
        print('p2 punch!')
        if block_punch:
            print('p1 blocked the punch!')
        else:
            self.health -= 1

    def kick(self, block_kick):
        print('p2 kick!')
        if block_kick:
            print('p1 blocked the kick!')
        else:
            self.health -= 1

    def biteprep(self):
        print('p2 gonna bite!')

    def punchprep(self):
        print('p2 gonna punch!')

    def kickprep(self):
        print('p2 gonna kick!')

    def animate_bite(self):
        return NotImplementedError

    def animate_punch(self):
        return NotImplementedError

    def animate_kick(self):
        return NotImplementedError
