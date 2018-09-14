#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
LIGHTGRAY = (192, 192, 192)
GANSBORO = (220, 220, 220)
SLATEGRAY = (112, 128, 144)

class Container:
    """Clase que permite dibujar contenedor de clases"""
    def __init__(self):
        self.num_datos = 3
        self.clases = dict()

    def add_data(self):
        """Añadir clase"""
        num_clases = len(self.clases)
        if num_clases > 10:
            print('Número de clases máximo')
        else:
            self.num_datos += 1

    #def upgrade_data(self):

class Button:
    """Clase que crea botones"""
    def __init__(self, main_surface, path_file, position=(0, 0), size=(30, 30)):
        self.surface = main_surface
        self.imagen = pygame.image.load(path_file)
        self.position = position
        self.size = size
        self.color = GRAY
        self.own_surface = pygame.Surface(size)
        self.own_surface.fill(WHITE)
        self.own_surface.blit(self.imagen, (3, 3))
        self.recta = (self.position[0], self.position[1], self.size[0], self.size[1])

    def draw_button(self):

        self.surface.blit(self.own_surface, self.position)
        pygame.draw.rect(self.surface, SLATEGRAY, self.recta, 1)

    def mouse_over(self):
        self.color = LIGHTGRAY
