import pygame
import math
import random

# Inicialização do Pygame
pygame.init()
screen = pygame.display.set_mode((1120, 980))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 24)

# Propriedades dos planetas
planetas = [
    {"color": (255, 255, 0), "distance": 200, "angle": 0, "speed": 0, "radius": 40, "name": "Sol"},  # Sol
    {"color": (169, 169, 169), "distance": 250, "angle": 0, "speed": 0.04, "radius": 5, "name": "Mercúrio"}, # Mercúrio
    {"color": (255, 215, 0), "distance": 300, "angle": 0, "speed": 0.035, "radius": 8, "name": "Vênus"},   # Vênus
    {"color": (0, 0, 255), "distance": 350, "angle": 0, "speed": 0.02, "radius": 10, "name": "Terra"},   # Terra
    {"color": (255, 0, 0), "distance": 400, "angle": 0, "speed": 0.015, "radius": 8, "name": "Marte"},   # Marte
    {"color": (255, 165, 0), "distance": 450, "angle": 0, "speed": 0.01, "radius": 15, "name": "Júpiter"}, # Júpiter
    {"color": (255, 255, 224), "distance": 500, "angle": 0, "speed": 0.008, "radius": 12, "name": "Saturno"}, # Saturno
    {"color": (135, 206, 235), "distance": 550, "angle": 0, "speed": 0.006, "radius": 10, "name": "Urano"},   # Urano
    {"color": (0, 0, 139), "distance": 600, "angle": 0, "speed": 0.004, "radius": 10, "name": "Netuno"}   # Netuno
]

# Função para desenhar estrelas
def draw_stars():
    for _ in range(80):  # Número de estrelas
        x = random.randint(0, 1100)
        y = random.randint(0, 900)
        pygame.draw.circle(screen, (60, 60, 60), (x, y), 1)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    draw_stars() # Desenhar estrelas

    # Desenhar o Sol no centro
    pygame.draw.circle(screen, (255, 255, 0), (400, 300), 40)  # Sol
    label = font.render("Sol", True, (255, 255, 255))
    screen.blit(label, (400 - label.get_width() // 2, 300 + 40 + 5))

    # Atualização e desenho dos planetas
    for planeta in planetas[1:]:  # Começar do Mercúrio
        planeta["angle"] += planeta["speed"]
        x = 400 + planeta["distance"] * math.cos(planeta["angle"])
        y = 300 + planeta["distance"] * math.sin(planeta["angle"])
        
        # Desenhar órbita
        pygame.draw.circle(screen, (255, 255, 255), (400, 300), int(planeta["distance"]), 1)

        pygame.draw.circle(screen, planeta["color"], (int(x), int(y)), planeta["radius"])

        # Renderiza o texto abaixo do planeta
        label = font.render(planeta["name"], True, (255, 255, 255))
        screen.blit(label, (int(x) - label.get_width() // 2, int(y) + planeta["radius"] + 5))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
