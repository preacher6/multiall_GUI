#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pygame
import easygui as eg
from properties import Container, Button, TextButton, RadioButton
from textbox import TextBox

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
LIGHTGRAY = (192, 192, 192)
RED = (255, 0, 0)
GAINSBORO = (220, 220, 220)
DIMGRAY = (105, 105, 105)
BLUE = (65, 105, 225)


class PygameMultiAll:
    def __init__(self):
        #self.container_clases = pygame.Rect(100, 100, 400, 100)
        self.initialize_pygame()
        self.screenform = pygame.display.set_mode((700, 600))
        self.acciones = pygame.Rect(50, 65, 380, 40)
        self.panel = pygame.Rect(40, 60, 400, 400)  # Panel grande
        self.subpanel = pygame.Rect(50, 110, 380, 300)  # Panel donde se ubican las acciones a realizar
        # Acción datos
        self.container_clases = pygame.Surface((200, 150))  # listmenu de clases
        self.container_clases.fill(WHITE)
        self.posi_container = (60, 120)
        self.selected_class = pygame.Rect(self.posi_container[0]+1, self.posi_container[1]+1, 198, 28)
        self.container = Container()  # Inicializa la clase contenedor
        self.class_actual = 1  # Indica que clase esta seleccionada
        self.conten_actual = 1  # Indicar que elemento de contenedor esta activo
        self.rect1 = pygame.Rect(self.posi_container[0] + 1, self.posi_container[1] + 1, 198, 28)
        self.rect2 = pygame.Rect(self.posi_container[0] + 1, self.posi_container[1] + 31, 198, 28)
        self.rect3 = pygame.Rect(self.posi_container[0] + 1, self.posi_container[1] + 61, 198, 28)
        self.rect4 = pygame.Rect(self.posi_container[0] + 1, self.posi_container[1] + 91, 198, 28)
        self.rect5 = pygame.Rect(self.posi_container[0] + 1, self.posi_container[1] + 121, 198, 28)
        self.down = 0  # Indicar cuantos desplazamientos ha dado el scroll de clases
        # Acción descriptor
        self.panel_forma = pygame.Rect(65, 150, 350, 110)  # Panel config. forma
        # Sistema
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('Arial', 14)
        self.font2 = pygame.font.SysFont('Arial', 25)
        self.actual = 1  # Indica en que sección de la GUI se encuentra

        self.buttons = list()
        self.textbuttons = list()
        self.text_fields = list()
        self.radio_buttons_desc = list()
        self.mouse_position = (0, 0)
        self.data = [{'tag':'Clase_1', 'path':'', 'files':[]},
                     {'tag':'Clase_2', 'path':'', 'files':[]}]

    @staticmethod
    def initialize_pygame():
        pygame.init()
        pygame.display.set_caption('Interfaz MultiAll')
        os.environ['SDL_VIDEO_CENTERED'] = '1'

    def build_buttons(self):
        """Construir botones"""
        open_button = Button(self.screenform, os.path.join('pics', 'open.png'), 'open',
                             position=(self.posi_container[0]+10, self.posi_container[1]+160))
        edit_button = Button(self.screenform, os.path.join('pics', 'edit.png'), 'edit',
                             position=(self.posi_container[0] + 45, self.posi_container[1] + 160))
        add_button = Button(self.screenform, os.path.join('pics', 'add.png'), 'add',
                            position=(self.posi_container[0] + 80, self.posi_container[1] + 160))
        del_button = Button(self.screenform, os.path.join('pics', 'delete.png'), 'delete',
                            position=(self.posi_container[0] + 115, self.posi_container[1] + 160))
        refresh_button = Button(self.screenform, os.path.join('pics', 'refresh.png'), 'refresh',
                                position=(self.posi_container[0] + 150, self.posi_container[1] + 160))

        self.buttons = [open_button, edit_button, add_button, del_button, refresh_button]

        selec_data = TextButton(self.screenform, 'Selección de datos', 'datos', position=(self.acciones[0]+3,
                                                                                         self.acciones[1]+4),
                                size=(94, 30), text_position=(3, 5))
        descriptor = TextButton(self.screenform, 'Descriptor', 'descriptor', position=(self.acciones[0]+100,
                                                                                       self.acciones[1]+4),
                                text_position=(20, 5))
        clasificador = TextButton(self.screenform, 'Clasificador', 'clasificador', position=(self.acciones[0] + 193,
                                                                                             self.acciones[1] + 4),
                                  text_position=(20, 5))
        validar = TextButton(self.screenform, 'Validación', 'validar', position=(self.acciones[0] + 286,
                                                                                 self.acciones[1] + 4),
                             text_position=(20, 5))

        self.textbuttons = [selec_data, descriptor, clasificador, validar]

        shape_radio = RadioButton(self.screenform, 'forma', os.path.join('pics', 'radio_unchecked.png'),
                                  os.path.join('pics', 'radio_checked.png'), 'Forma', position=(self.subpanel[0]+10,
                                                                                                self.subpanel[1]+10),
                                  active=True)
        color_radio = RadioButton(self.screenform, 'color', os.path.join('pics', 'radio_unchecked.png'),
                                  os.path.join('pics', 'radio_checked.png'), 'Color', position=(self.subpanel[0] + 10,
                                                                                                self.subpanel[1] + 160))

        shape_pred = RadioButton(self.screenform, 'forma_pred', os.path.join('pics', 'check_unchecked.png'),
                                 os.path.join('pics', 'check_checked.png'), 'Valores predeterminados',
                                 position=(self.subpanel[0] + 20, self.subpanel[1] + 45), active=True, size=(22, 22),
                                 color=LIGHTGRAY)

        self.radio_buttons_desc = [shape_radio, color_radio, shape_pred]

    def build_textfields(self):
        """Construir campos de texto"""
        celda1 = TextBox((self.panel_forma[0]+250, self.panel_forma[1]+10, 40, 20), buffer=["8"], id="cell1",
                         clear_on_enter=False, inactive_on_enter=True)
        celda2 = TextBox((self.panel_forma[0]+300, self.panel_forma[1]+10, 40, 20), buffer=["8"], id="cell2",
                         clear_on_enter=False, inactive_on_enter=True)
        bloque1 = TextBox((self.panel_forma[0] + 250, self.panel_forma[1] + 40, 40, 20), buffer=["2"], id="block1",
                          clear_on_enter=False, inactive_on_enter=True)
        bloque2 = TextBox((self.panel_forma[0] + 300, self.panel_forma[1] + 40, 40, 20), buffer=["2"], id="block2",
                          clear_on_enter=False, inactive_on_enter=True)
        bins = TextBox((self.panel_forma[0] + 250, self.panel_forma[1] + 70, 40, 20), buffer=["9"], id="bins",
                       clear_on_enter=False, inactive_on_enter=True)
        self.text_fields = [celda1, celda2, bloque1, bloque2, bins]

    def draw_surfaces(self):
        """Dibujar superficies adicionales"""
        self.screenform.blit(self.font2.render('-MultiAll-', True, BLACK), (250, 16))

        pygame.draw.rect(self.screenform, GAINSBORO, self.panel, 0)
        pygame.draw.rect(self.screenform, GRAY, self.subpanel, 0)
        if self.actual == 1:
            self.screenform.blit(self.container_clases, self.posi_container)
            self.draw_classes()

        pygame.draw.rect(self.screenform, GRAY, self.acciones, 0)

    def draw_buttons(self):
        for textbutton in self.textbuttons:
            textbutton.draw_button()
            if textbutton.recta.collidepoint(self.mouse_position):
                textbutton.over = True
            else:
                textbutton.over = False

        if self.actual == 1:
            for button in self.buttons:
                button.draw_button()
                if button.recta.collidepoint(self.mouse_position):
                    button.over = True
                else:
                    button.over = False

        if self.actual == 2:
            image = pygame.Surface(self.panel_forma[2:4])
            image.fill(GRAY)
            image.set_alpha(170)
            pygame.draw.rect(self.screenform, LIGHTGRAY, self.panel_forma, 0)
            for radio in self.radio_buttons_desc:
                radio.draw_button()
                if radio.recta.collidepoint(self.mouse_position):
                    radio.over = True
                else:
                    radio.over = False
                if radio.name == "forma":
                    if radio.push:
                        block_forma = False
                    else:
                        block_forma = True
            if block_forma:
                self.screenform.blit(image, self.panel_forma[:2])

        if self.actual == 2:
            for text in self.text_fields:
                text.update()
                text.draw(self.screenform)

    def draw_classes(self):
        if self.actual == 1:
            self.selected_class = pygame.Rect(self.posi_container[0] + 1,
                                              (self.posi_container[1]+(30*(self.conten_actual-1))) + 1, 198, 28)
            pygame.draw.rect(self.screenform, BLUE, self.selected_class, 0)
            for i in range(self.container.num_datos):
                self.screenform.blit(self.font.render('Clase '+str(i+1), True,
                                     BLACK), (self.posi_container[0]+5, self.posi_container[1]+5+(i*30)))

    def consult_container(self, position):
        if self.actual == 1:
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

    def button_actions(self, position):
        for textbutton in self.textbuttons:
            if textbutton.recta.collidepoint(position):
                if textbutton.name == "datos":
                    self.actual = 1
                    print('data')
                if textbutton.name == "descriptor":
                    self.actual = 2
                    print('descriptor')
                if textbutton.name == "clasificador":
                    self.actual = 3
                if textbutton.name == "validar":
                    self.actual = 4
                    for text in self.text_fields:
                        text.execute()
                        print("".join(text.buffer))

        if self.actual == 1:
            for button in self.buttons:
                if button.recta.collidepoint(position):
                    selected = self.conten_actual + self.down  # Determina clase elegida
                    if button.name == "open":
                        self.data = self.container.open(self.data, selected)
                    if button.name == "add":
                        self.data = self.container.add_data(self.data)
                    if button.name == "delete":
                        self.data = self.container.delete_data(self.data)
                    if button.name == "edit":
                        texto = eg.enterbox(msg='Etiqueta para clase '+str(selected)+':',
                                            title='Control: enterbox',
                                            default=self.data[selected-1]['tag'], strip=True,
                                            image=None)
                        self.data[selected-1]['tag'] = texto
                        print(self.data)

        if self.actual == 2:
            for radio in self.radio_buttons_desc:
                if radio.recta.collidepoint(position):
                    if radio.name == "forma":
                        radio.push = not radio.push
                    if radio.name == "forma_pred":
                        radio.push = not radio.push

    def check_text(self, event):
        for text in self.text_fields:
            text.get_event(event)

    def run_all(self, close):
        """Función que ejecuta all"""
        valor_1 = 0
        self.build_buttons()
        self.build_textfields()
        while not close:
            self.mouse_position = pygame.mouse.get_pos()
            for event in pygame.event.get():
                self.check_text(event)
                #self.text_u.get_event(event)
                if event.type == pygame.QUIT:
                    close = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    print(position)
                    self.consult_container(position)
                    self.button_actions(position)

            self.screenform.fill(DIMGRAY)
            self.draw_surfaces()
            self.draw_buttons()
            self.clock.tick(60)
            pygame.display.flip()
