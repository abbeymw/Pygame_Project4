import pygame
 
white = (255, 255, 255)
blue = (190,190,190)
green = (0,250,154)
red = (255, 0, 0)
black = (0,0,0)
blue2 = (0,191,255)
gold = (255, 215, 0)
 
class player_(pygame.sprite.Sprite):
    x_pos = 0
    y_pos = 0
 
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([25, 25])
        self.image.fill(blue2)
        self.rect = self.image.get_rect()
        self.score = 0
        self.rect.x = x
        self.rect.y = y

    def change_speed(self, x, y):
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
            
    # def move(self, dx, dy):
    #     # Move each axis separately. Note that this checks for collisions both times.
    #     if dx != 0:
    #         self.move_single_axis(dx, 0)
    #     if dy != 0:
    #         self.move_single_axis(0, dy)
    # def move_single_axis(self, dx, dy):
    #     # Move the rect
    #     self.rect.x += dx
    #     self.rect.y += dy
    #     # If you collide with a wall, move out based on velocity
    #     for wall in Maze.wall_list:
    #         if self.rect.colliderect(wall.rect):
    #             if dx > 0: # Moving right; Hit the left side of the wall
    #                 self.rect.right = wall.rect.left
    #             if dx < 0: # Moving left; Hit the right side of the wall
    #                 self.rect.left = wall.rect.right
    #             if dy > 0: # Moving down; Hit the top side of the wall
    #                 self.rect.bottom = wall.rect.top
    #             if dy < 0: # Moving up; Hit the bottom side of the wall
    #                 self.rect.top = wall.rect.bottom

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
                           # ,[400, 350, 20, 20, black]
                          ]
        for b in bonus_creation:
            bonus = Bonus(b[0], b[1], b[2], b[3], b[4])
            self.bonus_sprites.add(bonus)
 
class Maze(Setting):
    def __init__(self):
        super().__init__()
        self.wall_list = pygame.sprite.Group()
        #[x, y, width, height]
        walls_creation = [[0, 0, 20, 600, blue],
                 [780, 0, 20, 250, blue],
                 [780, 350, 20, 350, blue],
                 [20, 0, 760, 20, blue],
                 [20, 580, 760, 20, blue],
                 [310, 20, 20, 40, blue],
                 [310, 120, 20, 100, blue],
                 [310, 250, 20, 220, blue],
                 [310, 150, 80, 20, blue],
                 [310, 470, 200, 20, blue],
                 [320, 535, 20, 45, blue],
                 [480, 535, 20, 45, blue],
                 [400, 480, 20, 60, blue],
                 [100, 200, 20, 100, blue], 
                 [100, 200, 220, 20, blue],
                 [370, 200, 20, 200, blue],
                 [370, 55, 20, 100, blue],
                 [430, 20, 20, 140, blue],
                 [430, 140, 85, 20, blue],
                 [495, 45, 20, 105, blue],
                 [370, 200, 200, 20, blue],
                 [60, 20, 20, 145, blue],
                 [250, 20, 20, 145, blue],
                 [120, 145, 130, 20, blue],
                 [120, 60, 20, 90, blue],
                 [120, 50, 80, 20, blue],
                 [200, 50, 20, 50, blue],
                 [170, 100, 50, 20, blue],
                 [550, 20, 20, 130, blue],
                 [550, 130, 50, 20, blue],
                 [560, 400, 20, 180, blue],
                 [440, 400, 120, 20, blue],
                 [450, 250, 20, 110, blue],
                 [450, 340, 90, 20, blue],
                 [515, 200, 20, 95, blue],
                 [570, 200, 20, 115, blue],
                 [610, 50, 110, 20, blue],
                 [720, 50, 20, 300, blue],
                 [740, 145, 40, 20, blue],
                 [650, 110, 20, 205, blue],
                 [590, 245, 60, 20, blue],
                 [20, 230, 35, 20, blue],
                 [610, 350, 130, 20, blue],
                 [630, 370, 20, 180, blue],
                 [650, 530, 60, 20, blue],
                 [710, 490, 20, 60, blue],
                 [685, 470, 45, 20, blue],
                 [685, 405, 95, 20, blue],
                 [20, 520, 70, 20, blue],
                 [125, 405, 20, 175, blue],
                 [180, 480, 20, 100, blue],
                 [180, 525, 100, 20, blue],
                 [150, 220, 20, 130, blue],
                 [150, 350, 110, 20, blue],
                 [255, 260, 20, 110, blue],
                 [200, 255, 75, 20, blue],
                 [200, 255, 20, 70, blue],
                 [180, 460, 60, 20, blue],
                 [240, 410, 20, 70, blue],
                 [180, 410, 70, 20, blue],
                 [20, 330, 95, 20, blue],
                 [60, 380, 20, 105, blue],
                 [80, 440, 60, 20, blue]
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
    movingsprites = pygame.sprite.Group()
    movingsprites.add(player)
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
        player.move(maze.wall_list)
        # player.handle_keys()
        color = white
        disp.fill(color)

        tot_secs = start_time - (f_count//f_rate)
        if tot_secs < 0:
            game_over = True
            print("You ran out of time!")
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

 
        movingsprites.draw(disp)
        maze.wall_list.draw(disp)
        bonus_pts.bonus_sprites.draw(disp)
 
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.change_speed(-2, 0)
                if event.key == pygame.K_RIGHT:
                    player.change_speed(2, 0)
                if event.key == pygame.K_UP:
                    player.change_speed(0, -2)
                if event.key == pygame.K_DOWN:
                    player.change_speed(0, 2)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.change_speed(2, 0)
                if event.key == pygame.K_RIGHT:
                    player.change_speed(-2, 0)
                if event.key == pygame.K_UP:
                    player.change_speed(0,2)
                if event.key == pygame.K_DOWN:
                    player.change_speed(0, -2)
        # key = pygame.key.get_pressed()
        # if key[pygame.K_LEFT]:
        #     player.move(-2, 0)
        # if key[pygame.K_RIGHT]:
        #     player.move(2, 0)
        # if key[pygame.K_UP]:
        #     player.move(0, -2)
        # if key[pygame.K_DOWN]:
        #     player.move(0, 2)
        # key = pygame.key.get_pressed()
        # if key[pygame.K_LEFT]:
        #     player.x_pos -= 2
        # if key[pygame.K_RIGHT]:
        #     player.x_pos += 2
        # if key[pygame.K_UP]:
        #     player.y_pos -= 2
        # if key[pygame.K_DOWN]:
        #     player.y_pos += 2

        for b in bonus_pts.bonus_sprites:
            if player.rect.colliderect(b.rect):
                bonus_pts.bonus_sprites.remove(b)
                coin.play()
                if b.color == green:
                    player.score += 1
                elif b.color == gold:
                    player.score += 5
                # elif b.color == black:
                #     color = black
                #     disp.update()

        if player.rect.x > 801:
            game_over = True
            print("You Won!")
            print("Your Score: " + str(player.score))

    pygame.quit()
 
if __name__ == "__main__":
    main()




# create a rank, so like if you got between this and this score, 
# you are a cub, this and this you are a mama bear, etc












