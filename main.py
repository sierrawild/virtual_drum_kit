import pygame, random, palettes

def main():
    pygame.mixer.pre_init(44100, -16, 2, 512)
    pygame.init()

    palette = palettes.all_palettes[4]
    bg = palette['bg']
    
    width, height = 1280, 720
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    
    sounds = {'name': '88',
              # other
              'clap': [r'samples\clap-808.wav'],
              
              # cymbals
              'hihat': [r'samples\hihat-acoustic01.wav', r'samples\hihat-acoustic02.wav'],
              'hihat-open': [r'samples\openhat-acoustic01.wav'],
              'crash': [r'samples\crash-acoustic.wav'],
              'ride': [r'samples\ride-acoustic01.wav' , r'samples\ride-acoustic02.wav'],
              
              # drums
              'kick': [r'samples\kick-acoustic01.wav', r'samples\kick-acoustic02.wav'],
              'snare': [r'samples\snare-acoustic01.wav', r'samples\snare-acoustic02.wav'],
              'tom': [r'samples\tom-acoustic01.wav', r'samples\tom-acoustic02.wav'],
              }
    
    # instruments initialization
    clap = Instrument(sounds['clap'])
    snare = Instrument(sounds['snare'])
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Keys
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_SPACE:
                    clap.play()
                elif event.key == pygame.K_s:
                    snare.play()
                    
                    
        
        screen.fill(bg)
        
        ### Render ###
        snare.draw(screen, palette['colors'][0], (100,100), 50)
        pygame.draw.circle(screen,palette['colors'][0], (width/2, height/2), 10)
        pygame.draw.circle(screen,palette['colors'][1], (width/2, height/2 + 20), 10)
        pygame.draw.circle(screen,palette['colors'][2], (width/2, height/2 + 40), 10)
        pygame.draw.circle(screen,palette['colors'][3], (width/2, height/2 + 60), 10)
        pygame.draw.circle(screen,palette['colors'][4], (width/2, height/2 + 80), 10)
        
        pygame.display.flip()
        clock.tick(60)
        ###
    pygame.quit()


class Instrument:
    def __init__(self, sound):
        # sets the sound1 and checks if the library has second sound. 
        # If it dosnt both sounds will be the same
        self.sound1 = pygame.mixer.Sound(sound[0])
        try:
            self.sound2 = pygame.mixer.Sound(sound[1])
        except IndexError:
            self.sound2 = pygame.mixer.Sound(sound[0])
        
    def draw(self, surface, color, position, radius):
        p = pygame.Vector2(position)
        pygame.draw.circle(surface, color, p, radius)
        
    def play(self, weights=[6,1]):
        '''Plays the sounds. Adjust the weights to set how oftern 2 diferent sounds play'''
        choice = random.choices([1,2], weights=weights, k= 1)
        if choice[0] == 1:
            self.sound1.play()
        else:
            self.sound2.play()
            
        
    
    
if __name__ == '__main__':
    main()