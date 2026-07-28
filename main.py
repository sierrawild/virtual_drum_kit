import pygame, palettes, drum_sounds
from instrument import Instrument

def main():
    pygame.mixer.pre_init(44100, -16, 2, 512)
    pygame.init()

    palette = palettes.all_palettes[4]
    bg = palette['bg']
    
    width, height = 1280, 720
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    
    sounds = drum_sounds.eighty_eight
    
    # instruments initialization
    clap = Instrument(sounds['clap'], surface=screen, color=palette['colors'][1], position=(width*0.1, height*0.9), radius=30, key=[pygame.K_SPACE])

    snare = Instrument(sounds['snare'], surface=screen, color=palette['colors'][0], position=(width/2, height*0.8), radius=100, key=[pygame.K_KP2, pygame.K_s])
    kick1 = Instrument(sounds['kick'], surface=screen, color=palette['colors'][2], position=(width*0.35, height*0.82), radius=60, key=[pygame.K_KP1, pygame.K_z])
    kick2 = Instrument(sounds['kick'], surface=screen, color=palette['colors'][2], position=(width*0.65, height*0.82), radius=60, key=[pygame.K_KP3, pygame.K_x])
    snare = Instrument(sounds['snare'], surface=screen, color=palette['colors'][0], position=(width/2, height*0.8), radius=100, key=[pygame.K_KP2, pygame.K_s])
    
    instruments = [snare, clap, kick1, kick2]
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Keys
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            
            for instrument in instruments:
                instrument.keybord_input(event)
        

                
        screen.fill(bg)
        
        ### Render ###
        for instrument in instruments:
            instrument.run()

        
        pygame.display.flip()
        clock.tick(60)
        ###
    pygame.quit()



    
    
if __name__ == '__main__':
    main()