import pygame, palettes, drum_sounds
from instrument import Instrument

def main():
    pygame.mixer.pre_init(44100, -16, 2, 512)
    pygame.init()

    palette = palettes.radondom_palette()
    bg = palette['bg']
    
    width, height = 1280, 720
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    
    # text
    font = pygame.Font(None, 82)
    text_surface = font.render('self', True, (255,255,255))
    text_rect = text_surface.get_rect(center=(width/2, height/2))

    
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

        ### render ###
        screen.blit(text_surface, text_rect)

        
        pygame.display.flip()
        clock.tick(60)
        ###
    pygame.quit()



    
    
if __name__ == '__main__':
    main()