import pygame
 
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
 
class player_(pygame.sprite.Sprite):
    x_pos = 0
    y_pos = 0
 
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([25, 25])
        self.image.fill((255, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 
    # def change_speed(self, x, y):
    #     self.speed_x += x
    #     self.speed_y += y
 
    # def move(self, walls):
    #     self.rect.x += self.x_pos
    #     list_of_blocks = pygame.sprite.spritecollide(self, walls, False)
    #     for b in list_of_blocks:
    #         if self.x_pos > 0:
    #             self.rect.right = b.rect.left
    #         else:
    #             self.rect.left = b.rect.right
    #     self.rect.y += self.y_pos
    #     list_of_blocks = pygame.sprite.spritecollide(self, walls, False)
    #     for b in list_of_blocks:
    #         if self.y_pos > 0:
    #             self.rect.bottom = b.rect.top
    #         else:
    #             self.rect.top = b.rect.bottom
    def handle_keys(self, walls):
        """ Handles Keys """
        key = pygame.key.get_pressed()
        dist = 2 # distance moved in 1 frame, try changing it to 5
        if key[pygame.K_DOWN]: # down key
            self.y_pos += dist # move down
        elif key[pygame.K_UP]: # up key
            self.y_pos -= dist # move up
        if key[pygame.K_RIGHT]: # right key
            self.x_pos += dist # move right
        elif key[pygame.K_LEFT]: # left key
            self.x_pos -= dist

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
    enemy_sprites = None
 
    def __init__(self):
        self.wall_list = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()

# class Enemies(pygame.sprite.Sprite):
#     def __init__(self, x, y, w, h, color):
#         super().__init__()
#         self.image = pygame.Surface([w, h])
#         self.image.fill(color)
#         self.rect = self.image.get_rect()
#         self.rect.x = x
#         self.rect.y = y 
#         # self.draw()

# class Enemy_placement(Setting):
#     def __init__(self):
#         super().__init__()
#         enemies_creation = [[20, 20, 20, 20, GREEN]]
#         for e in enemies_creation:
#             enemy = Enemies(e[0], e[1], e[2], e[3], e[4])
#             self.enemy_sprites.add(enemy)
 
class Maze(Setting):
    def __init__(self):
        super().__init__()
        #[x, y, width, height]
        walls_creation = [[0, 0, 20, 600, WHITE],
                 [780, 0, 20, 250, WHITE],
                 [780, 350, 20, 350, WHITE],
                 [20, 0, 760, 20, WHITE],
                 [20, 580, 760, 20, WHITE],
                 [310, 20, 20, 40, BLUE],
                 [310, 90, 20, 380,BLUE],
                 [310, 150, 80, 20, BLUE],
                 [310, 470, 200, 20, BLUE],
                 [320, 535, 20, 45, BLUE],
                 [480, 535, 20, 45, BLUE],
                 [400, 480, 20, 60, BLUE],
                 [100, 200, 20, 100, BLUE], 
                 [100, 200, 220, 20, BLUE],
                 [370, 200, 20, 200, BLUE],
                 [370, 55, 20, 100, BLUE],
                 [430, 20, 20, 140, BLUE],
                 [430, 140, 85, 20, BLUE],
                 [495, 45, 20, 105, BLUE],
                 [370, 200, 200, 20, BLUE],
                 [60, 20, 20, 145, BLUE],
                 [250, 20, 20, 145, BLUE],
                 [120, 145, 130, 20, BLUE],
                 [120, 60, 20, 90, BLUE],
                 [120, 50, 80, 20, BLUE],
                 [200, 50, 20, 50, BLUE],
                 [170, 100, 50, 20, BLUE],
                 [550, 20, 20, 130, BLUE],
                 [550, 130, 50, 20, BLUE],
                 [560, 400, 20, 180, BLUE],
                 [440, 400, 120, 20, BLUE],
                 [450, 250, 20, 110, BLUE],
                 [450, 340, 90, 20, BLUE],
                 [515, 200, 20, 95, BLUE],
                 [570, 200, 20, 115, BLUE],
                 [610, 50, 110, 20, BLUE],
                 [720, 50, 20, 300, BLUE],
                 [740, 145, 40, 20, BLUE],
                 [650, 110, 20, 205, BLUE],
                 [590, 245, 60, 20, BLUE],
                 [20, 230, 35, 20, BLUE],
                 [610, 350, 130, 20, BLUE],
                 [630, 370, 20, 180, BLUE],
                 [650, 530, 60, 20, BLUE],
                 [710, 490, 20, 60, BLUE],
                 [685, 470, 45, 20, BLUE],
                 [685, 405, 95, 20, BLUE],
                 [20, 520, 70, 20, BLUE],
                 [125, 405, 20, 175, BLUE],
                 [180, 480, 20, 100, BLUE],
                 [180, 525, 100, 20, BLUE],
                 [150, 220, 20, 130, BLUE],
                 [150, 350, 110, 20, BLUE],
                 [255, 260, 20, 110, BLUE],
                 [200, 255, 75, 20, BLUE],
                 [200, 255, 20, 70, BLUE],
                 [180, 460, 60, 20, BLUE],
                 [240, 410, 20, 70, BLUE],
                 [180, 410, 70, 20, BLUE],
                 [20, 330, 95, 20, BLUE],
                 [60, 380, 20, 105, BLUE],
                 [80, 440, 60, 20, BLUE]
                ]
        for w in walls_creation:
            wall = Wall(w[0], w[1], w[2], w[3], w[4])
            self.wall_list.add(wall)

def main():
    #game stuff
    pygame.init()
    disp = pygame.display.set_mode([800, 600])
    pygame.display.set_caption("Abbey's Maze Game for Project 4")
    player = player_(20, 555)
    movingsprites = pygame.sprite.Group()
    movingsprites.add(player)
    maze = Maze()
    # enemies = Enemy_placement()

    #time clock
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 25)
    f_count = 0
    f_rate = 60
    start_time = 60

    #music/sound
    pygame.mixer.init()
    # pygame.mixer.music.load()



    game_over = False
    while not game_over: 
        player.handle_keys(maze.wall_list)
        # player.handle_keys()
        disp.fill((0, 0, 0))

        tot_secs = start_time - (f_count//f_rate)
        # if tot_secs < 0:
        #     game_over = True
        #     print("You ran out of time!")
        secs = tot_secs%60
        mins = (tot_secs//60)
        time_shown = "Time: {0:02}:{1:02}".format(mins, secs)
        text = font.render(time_shown, True, WHITE)
        disp.blit(text, [650, 20])
        f_count += 1
        clock.tick(f_rate)
 
        movingsprites.draw(disp)
        maze.wall_list.draw(disp)
        # enemies.draw(disp)

 
        pygame.display.flip()

        for event in pygame.event.get():
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_LEFT:
            #         player.change_speed(-2, 0)
            #     if event.key == pygame.K_RIGHT:
            #         player.change_speed(2, 0)
            #     if event.key == pygame.K_UP:
            #         player.change_speed(0, -2)
            #     if event.key == pygame.K_DOWN:
            #         player.change_speed(0, 2)
            # if event.type == pygame.KEYUP:
            #     if event.key == pygame.K_LEFT:
            #         player.change_speed(2, 0)
            #     if event.key == pygame.K_RIGHT:
            #         player.change_speed(-2, 0)
            #     if event.key == pygame.K_UP:
            #         player.change_speed(0,2)
            #     if event.key == pygame.K_DOWN:
            #         player.change_speed(0, -2)
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_LEFT:
            #         player.x_pos -= 1
            #     if event.key == pygame.K_RIGHT:
            #         player.x_pos += 1
            #     if event.key == pygame.K_UP:
            #         player.y_pos -= 1
            #     if event.key == pygame.K_DOWN:
            #         player.y_pos += 1


            if player.rect.x > 801:
                game_over = True
                print("You won!")

            if event.type == pygame.QUIT:
                game_over = True

    pygame.quit()
 
if __name__ == "__main__":
    main()


