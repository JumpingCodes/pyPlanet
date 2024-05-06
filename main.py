import pygame
import math

pygame.init()
WIDTH, HEIGHT = 1000, 1000
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("pyPlanet")

WHITE = (255, 255, 255)
YELLOW = (255, 205, 7)
BLUE = (3, 126, 183)
ORANGE = (216, 104, 6)
SILVER = (102,102,102)
BEIGE = (244, 222, 155)

class Planet:
    # distance from sun
    AU = 149.6e6 * 1000
    # gravitational constant
    G = 6.67430e-11
    SCALE = 300 / AU # 1AU = 100pixel
    TIMESTEP = 3600*24 # 1 day

    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0

        self.x_val = 0
        self.y_val = 0

    def draw(self, window):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2
        pygame.draw.circle(window, self.color, (x,y), self.radius)



def main():
    run = True
    clock = pygame.time.Clock()

    sun = Planet(0, 0, 69.5700 , YELLOW, 1.9885 * 10**30)
    sun.sun = True

    earth = Planet(Planet.AU, 0, 12.756, BLUE, 5.9722 * 10**24)

    mars = Planet(Planet.AU * 1.524, 0, 6.792, ORANGE, 6.4171 * 10**23)

    mercury = Planet(Planet.AU * 0.39, 0, 4.879, SILVER, 3.3011 * 10**23)

    venus = Planet(Planet.AU * 0.72, 0, 12.104 ,BEIGE, 4.867 * 10**24)

    Planets = [sun, earth, mars, mercury, venus]


    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        for planet in Planets:
            planet.draw(WINDOW)

        pygame.display.update()
    
    pygame.quit()

main()
