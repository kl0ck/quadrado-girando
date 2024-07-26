import pygame
import math

# Inicializa o Pygame
pygame.init()

# Configurações da tela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Quadrado Girando")

# Define a cor
preto = (0, 0, 0)
branco = (255, 255, 255)

# Parâmetros do quadrado
lado = 100
angulo = 0

# Loop principal
executando = True
relogio = pygame.time.Clock()

while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

    # Limpa a tela
    tela.fill(preto)

    # Calcula as coordenadas do quadrado
    centro_x = largura // 2
    centro_y = altura // 2

    # Calcula a rotação
    angulo += 1
    rad = math.radians(angulo)
    cos_ang = math.cos(rad)
    sin_ang = math.sin(rad)

    # Pontos do quadrado
    pontos = [
        (centro_x + lado * cos_ang / 2 - lado * sin_ang / 2,
         centro_y + lado * sin_ang / 2 + lado * cos_ang / 2),
        (centro_x - lado * cos_ang / 2 - lado * sin_ang / 2,
         centro_y - lado * sin_ang / 2 + lado * cos_ang / 2),
        (centro_x - lado * cos_ang / 2 + lado * sin_ang / 2,
         centro_y - lado * sin_ang / 2 - lado * cos_ang / 2),
        (centro_x + lado * cos_ang / 2 + lado * sin_ang / 2,
         centro_y + lado * sin_ang / 2 - lado * cos_ang / 2)
    ]

    # Desenha o quadrado
    pygame.draw.polygon(tela, branco, pontos)

    # Atualiza a tela
    pygame.display.flip()

    # Controla a taxa de atualização
    relogio.tick(60)

pygame.quit()
