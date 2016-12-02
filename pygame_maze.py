import pygame
from pygame import *
from pygame.sprite import *
from random import *

white = (255, 255, 255)
gray = (190,190,190)
green = (0,250,154)
red = (255, 0, 0)
black = (0,0,0)
teal = (0,191,255)
gold = (255, 215, 0)
 
class player_(pygame.sprite.Sprite):
    x_pos = 0
    y_pos = 0
 
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([25, 25])
        self.image.fill(teal)
        self.rect = self.image.get_rect()
        self.score = 0
        self.rect.x = x
        self.rect.y = y

    def change_pos(self, x, y):
        self.x_pos += x
        self.y_pos += y
 
    def move(self, walls):
        self.rect.x += self.x_pos
        list_of_blocks = pygame.sprite.spritecollide(self, walls, False)
        for b in list_of_blocks:
            if self.x_pos > 0:
                self.rect.right = b.rect.left
            else:
                self.rect.left = b.rect.right
        self.rect.y += self.y_pos
        list_of_blocks = pygame.sprite.spritecollide(self, walls, False)
        for b in list_of_blocks:
            if self.y_pos > 0:
                self.rect.bottom = b.rect.top
            else:
                self.rect.top = b.rect.bottom

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, color):
        super().__init__()
        self.image = pygame.Surface([w, h])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y 
        
class Setting(object):
    wall_list = None
    bonus_sprites = None
 
    def __init__(self):
        self.wall_list = pygame.sprite.Group()
        self.bonus_sprites = pygame.sprite.Group()

class Bonus(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, color):
        super().__init__()
        self.image = pygame.Surface([w, h])
        self.color = color
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y 

class bonus_placement(Setting):
    def __init__(self):
        super().__init__()
        self.bonus_sprites = pygame.sprite.Group()
        bonus_creation = [[35, 283, 20, 20, green],
                            [342, 110, 20, 20, green], 
                            [170, 75, 20, 20, gold],
                          [460, 105, 20, 20, gold],
                          [685, 505, 20, 20, gold],
                          [400, 230, 20, 20, green],
                          [225, 285, 20, 20, gold],
                          [215, 555, 20, 20, gold],
                          [365, 555, 20, 20, green],
                          [435, 505, 20, 20, green],
                          [155, 555, 20, 20, gold],
                          [90, 410, 20, 20, green],
                          [751, 120, 20, 20, gold],
                          [30, 30, 20, 20, green],
                          [125, 230, 20, 20, green],
                          [210, 490, 20, 20, green],
                          [210, 435, 20, 20, green],
                          [340, 435, 20, 20, green],
                          [542, 230, 20, 20, green],
                          [610, 270, 20, 20, gold],
                          [595, 555, 20, 20, green],
                          [751, 175, 20, 20, green],
                          [751, 435, 20, 20, green],
                          [680, 80, 20, 20, green],
                          [680, 310, 20, 20, green],
                          [610, 215, 20, 20, green],
                          [280, 35, 20, 20, green]
                          #[400, 350, 20, 20, black]
                          ]
        for b in bonus_creation:
            bonus = Bonus(b[0], b[1], b[2], b[3], b[4])
            self.bonus_sprites.add(bonus)
 
class Maze(Setting):
    def __init__(self):
        super().__init__()
        self.wall_list = pygame.sprite.Group()
        #[x, y, width, height]
        walls_creation = [[0, 0, 20, 600, gray],
                 [780, 0, 20, 250, gray],
                 [780, 350, 20, 350, gray],
                 [20, 0, 760, 20, gray],
                 [20, 580, 760, 20, gray],
                 [310, 20, 20, 40, gray],
                 [310, 120, 20, 100, gray],
                 [310, 250, 20, 220, gray],
                 [310, 150, 80, 20, gray],
                 [310, 470, 200, 20, gray],
                 [320, 535, 20, 45, gray],
                 [480, 535, 20, 45, gray],
                 [400, 480, 20, 60, gray],
                 [100, 200, 20, 100, gray], 
                 [100, 200, 220, 20, gray],
                 [370, 200, 20, 200, gray],
                 [370, 55, 20, 100, gray],
                 [430, 20, 20, 140, gray],
                 [430, 140, 85, 20, gray],
                 [495, 45, 20, 105, gray],
                 [370, 200, 200, 20, gray],
                 [60, 20, 20, 145, gray],
                 [250, 20, 20, 145, gray],
                 [120, 145, 130, 20, gray],
                 [120, 60, 20, 90, gray],
                 [120, 50, 80, 20, gray],
                 [200, 50, 20, 50, gray],
                 [170, 100, 50, 20, gray],
                 [550, 20, 20, 130, gray],
                 [550, 130, 50, 20, gray],
                 [560, 400, 20, 180, gray],
                 [440, 400, 120, 20, gray],
                 [450, 250, 20, 110, gray],
                 [450, 340, 90, 20, gray],
                 [515, 200, 20, 95, gray],
                 [570, 200, 20, 115, gray],
                 [610, 50, 110, 20, gray],
                 [720, 50, 20, 300, gray],
                 [740, 145, 40, 20, gray],
                 [650, 110, 20, 205, gray],
                 [590, 245, 60, 20, gray],
                 [20, 230, 35, 20, gray],
                 [610, 350, 130, 20, gray],
                 [630, 370, 20, 180, gray],
                 [650, 530, 60, 20, gray],
                 [710, 490, 20, 60, gray],
                 [685, 470, 45, 20, gray],
                 [685, 405, 95, 20, gray],
                 [20, 520, 70, 20, gray],
                 [125, 405, 20, 175, gray],
                 [180, 480, 20, 100, gray],
                 [180, 525, 100, 20, gray],
                 [150, 220, 20, 130, gray],
                 [150, 350, 110, 20, gray],
                 [255, 260, 20, 110, gray],
                 [200, 255, 75, 20, gray],
                 [200, 255, 20, 70, gray],
                 [180, 460, 60, 20, gray],
                 [240, 410, 20, 70, gray],
                 [180, 410, 70, 20, gray],
                 [20, 330, 95, 20, gray],
                 [60, 380, 20, 105, gray],
                 [80, 440, 60, 20, gray]
                ]
        for w in walls_creation:
            wall = Wall(w[0], w[1], w[2], w[3], w[4])
            self.wall_list.add(wall)

def main():
    #game stuff
    pygame.init()
    disp = pygame.display.set_mode([800, 600])
    pygame.display.set_caption("Abbey's Maze Game for Project 4")
    player = player_(20, 548)
    moving_sprites = pygame.sprite.Group()
    moving_sprites.add(player)
    maze = Maze()
    bonus_pts = bonus_placement()

    #time clock
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 25)
    f_count = 0
    f_rate = 60
    start_time = 60

    #music/sound
    pygame.mixer.init()
    pygame.mixer.music.load('ElTech_-_Techno_Background_Music.wav')
    pygame.mixer.music.play()
    # pygame.mixer.fadeout(1000)
    coin = pygame.mixer.Sound('Super_Mario_Bros.wav')

    game_over = False
    while not game_over: 
        color = white
        disp.fill(color)
        player.move(maze.wall_list)

        tot_secs = start_time - (f_count//f_rate)
        if tot_secs < 1:
            game_over = True
            print("You ran out of time!")
            print("Your Score: " + str(player.score))
        secs = tot_secs%60
        mins = (tot_secs//60)
        time_shown = "Time: {0:02}:{1:02}".format(mins, secs)
        text = font.render(time_shown, True, black)
        disp.blit(text, [650, 20])
        f_count += 1
        clock.tick(f_rate)

        score = "Score: {0}".format(str(player.score))
        text1 = font.render(score, True, black)
        disp.blit(text1, [650, 35])

 
        moving_sprites.draw(disp)
        maze.wall_list.draw(disp)
        bonus_pts.bonus_sprites.draw(disp)
 
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.change_pos(-2, 0)
                if event.key == pygame.K_RIGHT:
                    player.change_pos(2, 0)
                if event.key == pygame.K_UP:
                    player.change_pos(0, -2)
                if event.key == pygame.K_DOWN:
                    player.change_pos(0, 2)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.change_pos(2, 0)
                if event.key == pygame.K_RIGHT:
                    player.change_pos(-2, 0)
                if event.key == pygame.K_UP:
                    player.change_pos(0,2)
                if event.key == pygame.K_DOWN:
                    player.change_pos(0, -2)

        for b in bonus_pts.bonus_sprites:
            if player.rect.colliderect(b.rect):
                bonus_pts.bonus_sprites.remove(b)
                coin.play()
                if b.color == gold:
                    player.score += 5
                elif b.color == green:
                    player.score += 1

        if player.rect.x > 801:
            game_over = True
            print("You Won!")
            print("Your Score: " + str(player.score))

    pygame.quit()
 
if __name__ == "__main__":
    main()

