#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pygame
import easygui as eg
from properties import Container

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128,128,128)
LIGHTGRAY = (192, 192, 192)
RED = (255, 0, 0)
GAINSBORO = (220, 220, 220)
DIMGRAY = (105, 105, 105)
BLUE = (65,105,225)

class PygameMultiAll:
    def __init__(self):
        #self.container_clases = pygame.Rect(100, 100, 400, 100)
        self.initialize_pygame()
        self.screenform = pygame.display.set_mode((700, 600))
        self.panel = pygame.Rect(40, 60, 400, 400)
        self.container_clases = pygame.Surface((200, 150))
        self.container_clases.fill(WHITE)
        self.posi_container = (50, 110)
        self.selected_class = pygame.Rect(self.posi_container[0]+1, self.posi_container[1]+1, 198, 28)
        self.clock = pygame.time.Clock()
        self.container = Container()  # Inicializa la clase contenedor
        self.actual = 1  # Indica en que sección de la GUI se encuentra
        self.class_actual = 1  # Indica que clase esta seleccionada
        self.conten_actual = 1  # Indicar que elemento de contenedor esta activo
        self.font = pygame.font.SysFont('Arial', 14)
        self.font2 = pygame.font.SysFont('Arial', 25)
        self.rect1 = pygame.Rect(self.posi_container[0]+1, self.posi_container[1]+1, 198, 28)
        self.rect2 = pygame.Rect(self.posi_container[0]+1, self.posi_container[1]+31, 198, 28)
        self.rect3 = pygame.Rect(self.posi_container[0]+1, self.posi_container[1]+61, 198, 28)
        self.rect4 = pygame.Rect(self.posi_container[0] + 1, self.posi_container[1] + 91, 198, 28)
        self.rect5 = pygame.Rect(self.posi_container[0] + 1, self.posi_container[1] + 121, 198, 28)
        self.down = 0  # Indicar cuantos desplazamientos ha dado el scroll de clases

    @staticmethod
    def initialize_pygame():
        pygame.init()
        pygame.display.set_caption('Interfaz MultiAll')
        os.environ['SDL_VIDEO_CENTERED'] = '1'

    def draw_surfaces(self):
        """Dibujar superficies adicionales"""
        #self.panel_acciones
        self.screenform.blit(self.font2.render('-MultiAll-', True, BLACK), (250, 16))
        pygame.draw.rect(self.screenform, GAINSBORO, self.panel, 0)
        if self.actual == 1:
            self.screenform.blit(self.container_clases, self.posi_container)
            self.draw_clases()

    def draw_clases(self):
        self.selected_class = pygame.Rect(self.posi_container[0] + 1,
                                          (self.posi_container[1]+(30*(self.conten_actual-1))) + 1, 198, 28)
        pygame.draw.rect(self.screenform, BLUE, self.selected_class, 0)
        for i in range(self.container.num_datos):
            self.screenform.blit(self.font.render('Clase '+str(i+1), True,
                                 BLACK), (self.posi_container[0]+5, self.posi_container[1]+5+(i*30)))

    def run_all(self, close):
        """Función que ejecuta all"""
        while not close:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    close = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    print(position)
                    if self.rect1.collidepoint(position):
                        print('recta1')
                        self.conten_actual = 1
                    if self.rect2.collidepoint(position):
                        print('recta2')
                        self.conten_actual = 2
                    if self.container.num_datos > 2:
                        if self.rect3.collidepoint(position):
                            print('recta3')
                            self.conten_actual = 3
                        if self.container.num_datos > 3:
                            if self.rect4.collidepoint(position):
                                print('recta4')
                                self.conten_actual = 4
                            if self.container.num_datos > 4:
                                if self.rect5.collidepoint(position):
                                    print('recta5')
                                    self.conten_actual = 5

            self.screenform.fill(DIMGRAY)
            self.draw_surfaces()
            self.clock.tick(60)
            pygame.display.flip()
