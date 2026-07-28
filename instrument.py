import pygame, random, math

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
            sound = self.sound1
        else:
            sound = self.sound2
        
        sound.set_volume(random.uniform(0.8, 1.1))
        sound.play()
    
    def mouse(self):
        mouse_x = pygame.mouse.get_pos()[0]
        mouse_y = pygame.mouse.get_pos()[1]
        
        sqx = (mouse_x -self.position[0])**2
        sqy = (mouse_y -self.position[1])**2
                    
        if pygame.mouse.get_just_pressed()[0] and math.sqrt(sqx + sqy) < self.radius:         
            self.play()
    
    def keybord_input(self, event):
        if event.type == pygame.KEYDOWN:
            for k in self.key:
                if event.key == k:
                    self.play()
    def run(self):
        self.draw()
        self.mouse()