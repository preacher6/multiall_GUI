#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import pygame
import easygui as eg

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
LIGHTGRAY = (192, 192, 192)
GANSBORO = (220, 220, 220)
SLATEGRAY = (112, 128, 144)


class Container:
    """Clase que permite dibujar contenedor de clases"""
    def __init__(self):
        self.num_datos = 2
        #self.clases = dict()

    def add_data(self, data):
        """Añadir clase"""
        num_clases = len(data)
        if num_clases > 10:
            print('Número de clases máximo')
        else:
            self.num_datos += 1
            data.append({'tag':'Clase_'+str(num_clases+1), 'path':'', 'files':[]})
        print(data)
        return data

    def delete_data(self, data):
        num_clases = len(data)
        if num_clases == 2:
            print('minimas clases')
        else:
            self.num_datos -= 1
            data.pop()
        print(data)
        return data

    def open(self, data, selected_data):
        ext = [".png", ".jpg"]
        path = eg.diropenbox(msg="Especificar directorio:",
                           title="Control: diropenbox",
                           default='C')

        files = os.listdir(path)
        data_files = [file for file in files if file.endswith(tuple(ext))]
        if len(data_files) >= 10:
            data[selected_data - 1]['path'] = path
            data[selected_data - 1]['files'] = data_files
        else:
            print('minimo 10')
        print(data)
        return data

    #def upgrade_data(self):


class Button:
    """Clase que crea botones"""
    def __init__(self, main_surface, path_file, name, position=(0, 0), size=(30, 30)):
        self.surface = main_surface
        self.imagen = pygame.image.load(path_file)
        self.name = name
        self.position = position
        self.size = size
        self.color = WHITE
        self.own_surface = pygame.Surface(size)
        self.own_surface.fill(self.color)
        self.own_surface.blit(self.imagen, (3, 3))
        self.recta = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])
        self.over = False
        self.wait = False

    def draw_button(self):
        """Dibujar boton"""
        if self.over:
            self.own_surface.fill(GRAY)
            self.own_surface.blit(self.imagen, (3, 3))
        else:
            self.own_surface.fill(WHITE)
            self.own_surface.blit(self.imagen, (3, 3))
        self.surface.blit(self.own_surface, self.position)
        self.own_surface.fill(self.color)
        pygame.draw.rect(self.surface, SLATEGRAY, self.recta, 1)

    def mouse_over(self):
        self.over = True
