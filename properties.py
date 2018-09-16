#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import pygame
import easygui as eg

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SEMIWHITE = (245, 245, 245)
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
                             title="Control: diropenbox")

        files = os.listdir(path)
        data_files = [file for file in files if file.endswith(tuple(ext))]
        if len(data_files) >= 10:
            data[selected_data - 1]['path'] = path
            data[selected_data - 1]['files'] = data_files
        else:
            print('minim 10')
        print(data)
        return data


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

    def draw_button(self):
        """Dibujar boton"""
        if self.over:
            self.own_surface.fill(SLATEGRAY)
            self.own_surface.blit(self.imagen, (3, 3))
        else:
            self.own_surface.fill(WHITE)
            self.own_surface.blit(self.imagen, (3, 3))
        self.surface.blit(self.own_surface, self.position)
        pygame.draw.rect(self.surface, BLACK, self.recta, 1)

    def mouse_over(self):
        self.over = True


class TextButton:
    def __init__(self, mainscreen, text, name, position=(0, 0), size=(90, 30), text_position=(5, 5)):
        self.surface = mainscreen
        self.text = text
        self.name = name
        self.position = position
        self.size = size
        self.text_position = text_position
        self.own_surface = pygame.Surface(self.size)
        self.own_surface.fill(SEMIWHITE)
        self.recta = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])
        self.font = pygame.font.SysFont('Arial', 13)
        self.own_surface.blit(self.font.render(self.text, True,
                              BLACK), self.text_position)
        self.over = False

    def draw_button(self):
        if self.over:
            self.own_surface.fill(SLATEGRAY)
            self.own_surface.blit(self.font.render(self.text, True,
                                                   BLACK), self.text_position)
            self.font.set_underline(True)
        else:
            self.own_surface.fill(SEMIWHITE)
            self.own_surface.blit(self.font.render(self.text, True,
                                                   BLACK), self.text_position)
            self.font.set_underline(False)
        self.surface.blit(self.own_surface, self.position)
        pygame.draw.rect(self.surface, BLACK, self.recta, 1)


class RadioButton:
    def __init__(self, mainscreen, name, no_pushed, pushed, texto, position=(0, 0), size=(24, 24), color=GRAY, active=False):
        self.surface = mainscreen
        self.name = name
        self.no_pushed = pygame.image.load(no_pushed)
        self.pushed = pygame.image.load(pushed)
        self.text = texto
        self.position = position
        self.size = size
        self.color = color
        self.own_surface = pygame.Surface(size)
        self.own_surface.fill(self.color)
        self.own_surface.blit(self.no_pushed, (0, 0))
        self.font = pygame.font.SysFont('Arial', 14)
        self.recta = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])
        self.over = False
        self.push = active

    def draw_button(self):
        if self.over:
            self.surface.blit(self.font.render(self.text, True, BLACK), (self.position[0] + 26, self.position[1] + 2))
            self.font.set_underline(True)
        else:
            self.surface.blit(self.font.render(self.text, True, BLACK), (self.position[0] + 26, self.position[1] + 2))
            self.font.set_underline(False)
        if self.push:
            self.own_surface.fill(self.color)
            self.own_surface.blit(self.pushed, (0, 0))
        else:
            self.own_surface.fill(self.color)
            self.own_surface.blit(self.no_pushed, (0, 0))
        self.surface.blit(self.own_surface, self.position)
