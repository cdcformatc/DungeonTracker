#!/usr/bin/python

import pygame

#display settings
FIELD_SIZE = 800
GRID_SIZE = 80

black = (0, 0, 0)
white = (255, 255, 255)
gray = (127,127,127)
transparent = (255,0,255)

def make_grid(screen, field_size, grid_size, color):
    grid = pygame.Surface(screen.get_size())
    grid = grid.convert()
    
    # set the alpha colorkey and fill the grid background with that color
    # grid.set_colorkey(transparent)
    # grid.fill(transparent)
    
    # draw grid lines
    for i in xrange(grid_size, field_size+grid_size, grid_size):
        pygame.draw.line(grid, color, (i, 0), (i, field_size))
        pygame.draw.line(grid, color, (0, i), (field_size,i))
        
    return grid

def main():
    # init screen
    pygame.init()
    
    screen = pygame.display.set_mode((FIELD_SIZE, FIELD_SIZE))
    pygame.display.set_caption('Dungeon Tracker')

    # display some text
    font = pygame.font.SysFont("Courier New", 18)
    text = font.render("Hello There", 1, white)
    textpos = text.get_rect()
    textpos.centerx = screen.get_rect().centerx
    
	# Create Grid
    # TODO: Resize/move grid based on background image (background image also TODO).
    grid = make_grid(screen, FIELD_SIZE, GRID_SIZE, gray)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                return
        
        # TODO: Put image on background. 
        # Also: devise a way to pick a background.
        screen.fill(black)
        
        # Draw Grid 
        screen.blit(grid, (0, 0))
        
        # Draw Text
        screen.blit(text, textpos)
        
        # Draw Players
        # TODO: Add and draw players.
        
        # Draw NPCs
        # TODO: Add and draw NPCs.
        
        # update the entire contents of the display surface
        pygame.display.flip()

if __name__ == "__main__":
    main()