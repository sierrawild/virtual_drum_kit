import pygame, random, palettes

width, height = 1280, 720

palette = palettes.all_palettes[4]
bg = palette['bg']
def main():
    pygame.mixer.pre_init(44100, -16, 2, 512)
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Keys
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    
        screen.fill(bg)
        
        ### Render ###
        pygame.draw.circle(screen,palette['colors'][0], (width/2, height/2), 10)
        pygame.draw.circle(screen,palette['colors'][1], (width/2, height/2 + 20), 10)
        pygame.draw.circle(screen,palette['colors'][2], (width/2, height/2 + 40), 10)
        pygame.draw.circle(screen,palette['colors'][3], (width/2, height/2 + 60), 10)
        pygame.draw.circle(screen,palette['colors'][4], (width/2, height/2 + 80), 10)
        
        pygame.display.flip()
        clock.tick(60)
        ###
    pygame.quit()
    
    
if __name__ == '__main__':
    main()