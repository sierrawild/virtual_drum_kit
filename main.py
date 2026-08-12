import pygame, palettes, drum_sounds
from instrument import Instrument

def main():
    pygame.mixer.pre_init(44100, -16, 2, 512)
    pygame.init()

    palette_index = 
    palettes_list = palettes.all_palettes
    palette = palettes.radondom_palette()
    bg = palette['bg']
    
    width, height = 1280, 720
    menu_w, menu_h = 300, 100
    screen = pygame.display.set_mode((width, height))
    menu = pygame.Surface((menu_w, menu_h), pygame.SRCALPHA)
    menu_offset_x = 20
    menu_offset_y = 20
    clock = pygame.time.Clock()
    
    # font
    font1 = pygame.Font(None, 26)
    
    instruments = instument_init(palette, width, height, screen)

    
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
        
        ### Menu ###
        # background
        pygame.draw.rect(menu, palette['colors'][1],(0,0,menu_w,menu_h), width=0, border_radius=20)
        offset = 20
        # Palette label text
        text_palette_surface1 = font1.render('Palette:', True, "#FDFFFE")
        text_palette_rect1 = text_palette_surface1.get_rect(center= (menu_w / 2, offset))
        menu.blit(text_palette_surface1, text_palette_rect1) 
        # Palete name text
        text_palette_surface = font1.render(palette['name'], True, "#FDFFFE")
        text_palette_rect = text_palette_surface.get_rect(center= (menu_w / 2, offset * 2))
        menu.blit(text_palette_surface, text_palette_rect) 

        # button
        button_size = 25
        button_L = pygame.Rect(10,offset,button_size,button_size)
        button_R = pygame.Rect(menu_w -(10 + button_size),offset,button_size,button_size)
        
        # hover and click
        mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
        mouse_pos[0] -= menu_offset_x 
        mouse_pos[1] -= menu_offset_y 
        # click
        # Left button
        plus_or_minus = -1
        if button_L.collidepoint(mouse_pos) and pygame.mouse.get_just_pressed()[0]: # click
            pygame.draw.rect(menu, palette['colors'][2],button_L.inflate(-5,-10), width=0, border_radius=5)
            palette_index = palette_index + plus_or_minus
            if palette_index < 0:
                palette_index = len(palettes_list) 
            print(f'{palette_index}  {len(palettes_list)}')
            # palette = palettes_list((palette_index - 1 % len(palettes_list))) 
        elif button_L.collidepoint(mouse_pos): # hover
            pygame.draw.rect(menu, palette['colors'][2],button_L.inflate(10,10), width=0, border_radius=5) 
        else: # draw button if nothing happen 
            pygame.draw.rect(menu, palette['colors'][2],button_L, width=0, border_radius=5) 
        # Right button
        
            

        
        
        ### Render ###
        for instrument in instruments:
            instrument.run().pretty_draw(bg)
        screen.blit(menu, (menu_offset_x,menu_offset_y))

        
        pygame.display.flip()
        clock.tick(60)
        ###
    pygame.quit()


def instument_init(palette, width, height, screen):
    ''' instruments initialization '''
    sounds = drum_sounds.eighty_eight
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
    return instruments
    
    
if __name__ == '__main__':
    main()