import pygame

def main():
	pygame.init()
	disp = pygame.display.set_mode([800, 700])
	pygame.display.set_caption("MazePyGame by Abbey Warren")
	clock = pygame.time.Clock()

	while True:
		# disp.fill(0, 0, 255)
		pygame.display.flip()
		clock.tick(60)
	pygame.quit()

main()
