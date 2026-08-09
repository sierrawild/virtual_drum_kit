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
    
    sounds = drum_sounds.eighty_eight
    
    # instruments initialization
    clap = Instrument('Clap', sounds['clap'], surface=screen, color=palette['colors'][1], position=(width*0.1, height*0.9), radius=40, key=[pygame.K_c, pygame.K_SPACE])
    clap.make_square()
    
    snare = Instrument('Snare', sounds['snare'], surface=screen, color=palette['colors'][0], position=(width/2, height*0.8), radius=100, key=[pygame.K_KP2, pygame.K_s])
    kick1 = Instrument('Kick', sounds['kick'], surface=screen, color=palette['colors'][2], position=(width*0.39, height*0.88), radius=48, key=[pygame.K_KP1, pygame.K_z])
    kick2 = Instrument('Kick', sounds['kick'], surface=screen, color=palette['colors'][2], position=(width*0.61, height*0.88), radius=48, key=[pygame.K_KP3, pygame.K_x])

    tom1 = Instrument('Tom', sounds['tom'], surface=screen, color=palette['colors'][3], position=(width*0.40, height*0.60), radius=70, key=[pygame.K_KP5, pygame.K_d])
    tom2 = Instrument('Tom', sounds['tom2'], surface=screen, color=palette['colors'][3], position=(width*0.52, height*0.54), radius=75, key=[pygame.K_KP6, pygame.K_f])
    tom3 = Instrument('Tom', sounds['tom3'], surface=screen, color=palette['colors'][3], position=(width*0.63, height*0.65), radius=80, key=[pygame.K_KP_PLUS, pygame.K_e])
    floor_tom = Instrument('Floor Tom', sounds['floor_tom'], surface=screen, color=palette['colors'][3], position=(width*0.73, height*0.82), radius=85, key=[pygame.K_KP8, pygame.K_r])

    crash = Instrument('Crash', sounds['crash'], surface=screen, color=palette['colors'][4], position=(width*0.3, height*0.40), radius=75, key=[pygame.K_KP7, pygame.K_q])
    ride = Instrument('Ride', sounds['ride'], surface=screen, color=palette['colors'][4], position=(width*0.7, height*0.40), radius=80, key=[pygame.K_KP9, pygame.K_w])
    
    hihat = Instrument('HiHat', sounds['hihat'], surface=screen, color=palette['colors'][4], position=(width*0.3, height*0.7), radius=60, key=[pygame.K_KP4, pygame.K_a])


    instruments = [snare, clap, kick1, kick2, tom1, tom2, tom3, floor_tom, crash, ride, hihat]

    
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
            instrument.run().pretty_draw(bg)

        
        pygame.display.flip()
        clock.tick(60)
        ###
    pygame.quit()



    
    
if __name__ == '__main__':
    main()