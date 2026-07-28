import pygame, random, palettes, math

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
    snare = Instrument(sounds['snare'], surface=screen, color=palette['colors'][0], position=(width/2, height*0.8), radius=50, key=pygame.K_b)
    
    instruments = [snare]
    
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


class Instrument:
    def __init__(self, sound, surface, color, position, radius, key, weights=[6,1]):
        
        self.weights = weights
        self.surface = surface
        self.color = color
        self.position = position
        self.radius = radius
        self.key = key
        
        # sets the sound1 and checks if the library has second sound. 
        # If it dosnt esist both sounds will be the same
        self.sound1 = pygame.mixer.Sound(sound[0])
        try:
            self.sound2 = pygame.mixer.Sound(sound[1])
        except IndexError:
            self.sound2 = pygame.mixer.Sound(sound[0])
        
        
    def draw(self):
        p = pygame.Vector2(self.position)
        pygame.draw.circle(self.surface, self.color, p, self.radius)
        
    def play(self):
        '''Plays the sounds. Adjust the weights to set how oftern 2 diferent sounds play'''
        choice = random.choices([1,2], weights=self.weights, k= 1)
        if choice[0] == 1:
            self.sound1.play()
        else:
            self.sound2.play()
    
    def mouse(self):
        mouse_x = pygame.mouse.get_pos()[0]
        mouse_y = pygame.mouse.get_pos()[1]
        
        sqx = (mouse_x -self.position[0])**2
        sqy = (mouse_y -self.position[1])**2
                    
        if pygame.mouse.get_just_pressed()[0] and math.sqrt(sqx + sqy) < self.radius:         
            self.play()
    
    def keybord_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == self.key:
                self.play()
    def run(self):
        self.draw()
        self.mouse()
    
    
if __name__ == '__main__':
    main()