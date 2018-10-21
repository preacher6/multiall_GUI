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
        self.screenform = pygame.display.set_mode((700, 460))
        self.acciones = pygame.Rect(50, 65, 380, 40)
        self.panel = pygame.Rect(40, 60, 400, 360)  # Panel grande
        self.panelout = pygame.Rect(450, 60, 200, 360)  # Panel configuración sistema
        self.rectaout = pygame.Rect(465, 110, 170, 210)
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
        self.panel_forma = pygame.Rect(65, 150, 350, 100)  # Panel config. forma
        self.block_forma = False
        self.block_forma_pred = True
        self.panel_color = pygame.Rect(65, 290, 350, 100)  # Panel config. forma
        # Sistema
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('Arial', 14)
        self.font2 = pygame.font.SysFont('Arial', 25)
        self.font3 = pygame.font.SysFont('Arial', 18)
        self.actual = 1  # Indica en que sección de la GUI se encuentra

        self.parametros = {'clases':2, 'verified':'No', 'descriptor':'HOG', 'clasificador':'SVM', 'validacion':'Sí',
                           'reduccion':'No'}
        self.buttons = list()
        self.textbuttons = list()
        self.text_fields_shape = list()
        self.text_fields_color = list()
        self.radio_buttons_desc = list()
        self.mouse_position = (0, 0)
        self.data = [{'tag':'Clase_1', 'path':'', 'files':[]},
                     {'tag':'Clase_2', 'path':'', 'files':[]}]
        self.verified_data = 'No'
        self.descriptor = 'HOG'
        self.desc_activo = [1, 0]  # Indica q descriptor esta activo [forma, color]

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
                                                                                                self.subpanel[1] + 150))

        shape_pred = RadioButton(self.screenform, 'forma_pred', os.path.join('pics', 'check_unchecked.png'),
                                 os.path.join('pics', 'check_checked.png'), 'Valores predeterminados',
                                 position=(self.subpanel[0] + 20, self.subpanel[1] + 45), active=True, size=(22, 22),
                                 color=LIGHTGRAY)
        rgb_radio = RadioButton(self.screenform, 'rgb', os.path.join('pics', 'radio_uncheck21.png'),
                                os.path.join('pics', 'radio_check21.png'), 'RGB', position=(self.subpanel[0] + 25,
                                                                                            self.subpanel[1] + 190),
                                size=(21, 21), color=LIGHTGRAY, active=True)
        hsv_radio = RadioButton(self.screenform, 'hsv', os.path.join('pics', 'radio_uncheck21.png'),
                                os.path.join('pics', 'radio_check21.png'), 'HSV', position=(self.subpanel[0] + 25,
                                                                                            self.subpanel[1] + 220),
                                size=(21, 21), color=LIGHTGRAY)
        lab_radio = RadioButton(self.screenform, 'lab', os.path.join('pics', 'radio_uncheck21.png'),
                                os.path.join('pics', 'radio_check21.png'), 'Lab', position=(self.subpanel[0] + 25,
                                                                                            self.subpanel[1] + 250),
                                size=(21, 21), color=LIGHTGRAY)

        self.radio_buttons_desc = [shape_radio, color_radio, shape_pred, rgb_radio, hsv_radio, lab_radio]

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
        self.text_fields_shape = [celda1, celda2, bloque1, bloque2, bins]

        bin1 = TextBox((self.panel_color[0]+140, self.panel_color[1]+35, 40, 20), buffer=[""], id="bin1",
                       clear_on_enter=False, inactive_on_enter=True)
        bin2 = TextBox((self.panel_color[0] + 190, self.panel_color[1] + 35, 40, 20), buffer=[""], id="bin2",
                       clear_on_enter=False, inactive_on_enter=True)
        bin3 = TextBox((self.panel_color[0] + 240, self.panel_color[1] + 35, 40, 20), buffer=[""], id="bin3",
                       clear_on_enter=False, inactive_on_enter=True)

        self.text_fields_color = [bin1, bin2, bin3]

    def draw_surfaces(self):
        """Dibujar superficies adicionales"""
        self.screenform.blit(self.font2.render('-MultiAll-', True, BLACK), (250, 16))
        pygame.draw.rect(self.screenform, GAINSBORO, self.panel, 0)
        pygame.draw.rect(self.screenform, GAINSBORO, self.panelout, 0)  # Recta superficie panel salida parametros
        pygame.draw.rect(self.screenform, LIGHTGRAY, self.rectaout, 1)  # Recta de parámetros
        self.screenform.blit(self.font3.render('Configuración del Sistema', True, BLACK), (self.panelout[0] + 13,
                                                                                           self.panelout[1] + 10))
        pygame.draw.rect(self.screenform, GRAY, self.subpanel, 0)
        if self.actual == 1:
            self.screenform.blit(self.container_clases, self.posi_container)
            self.draw_classes()

        if self.actual == 2:
            pygame.draw.rect(self.screenform, LIGHTGRAY, self.panel_forma, 0)

        pygame.draw.rect(self.screenform, GRAY, self.acciones, 0)

    def block_all(self):
        image = pygame.Surface(self.panel_forma[2:4])
        image.fill(GRAY)
        image.set_alpha(170)
        if self.block_forma:
            self.screenform.blit(image, self.panel_forma[:2])

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
            pygame.draw.rect(self.screenform, LIGHTGRAY, self.panel_forma, 0)
            pygame.draw.rect(self.screenform, LIGHTGRAY, self.panel_color, 0)
            for text in self.text_fields_shape:  # Dibujar text fields forma
                text.update()
                text.draw(self.screenform)
            self.screenform.blit(self.font.render('Celdas:', True, BLACK), (self.panel_forma[0]+210,
                                                                            self.panel_forma[1]+10))
            self.screenform.blit(self.font.render('Bloques:', True, BLACK), (self.panel_forma[0] + 204,
                                                                             self.panel_forma[1] + 40))
            self.screenform.blit(self.font.render('Bins:', True, BLACK), (self.panel_forma[0] + 222,
                                                                          self.panel_forma[1] + 70))
            for text in self.text_fields_color:  # Dibujar text fields color
                text.update()
                text.draw(self.screenform)

            for radio in self.radio_buttons_desc:
                if radio.recta.collidepoint(self.mouse_position):
                    radio.over = True
                else:
                    radio.over = False
                if radio.name == "forma":
                    if radio.push:
                        self.block_forma = False
                    else:
                        self.block_forma = True
                if radio.name == "forma_pred":
                    if radio.push:
                        self.block_forma_pred = True
                    else:
                        self.block_forma_pred = False
                image = pygame.Surface(self.panel_forma[2:4])
                image.fill(GRAY)
                image.set_alpha(100)
                if self.block_forma_pred:
                    self.screenform.blit(image, self.panel_forma[:2])
                radio.draw_button()

    def draw_classes(self):
        """Dibujar contenedor de clases"""
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
                    for text in self.text_fields_shape:
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
            lista_radio = ["forma", "forma_pred", "color", "rgb", "hsv", "lab"]
            lista = [0, 0]
            pushed = False
            print(self.desc_activo)
            for radio in self.radio_buttons_desc[:3]:  # Botones:forma, forma_pred y color
                if radio.recta.collidepoint(position):
                    for name in lista_radio:
                        if radio.name == name:
                            radio.push = not radio.push
                        if radio.name == "forma":
                            pushed = True
                            lista[0] = radio.push
                        if radio.name == "color":
                            pushed = True
                            lista[1] = radio.push
            print(lista)
            print(self.desc_activo)
            #if lista != self.desc_activo:
            if lista == [0, 0] and pushed:
                print('in')
                for radio in self.radio_buttons_desc[:3]:  # Botones:forma, forma_pred y color
                    print('joo')
                    if radio.name == "forma":
                        lista[0] = self.desc_activo[0]
                        radio.push = lista[0]
                    if radio.name == "color":
                        lista[1] = self.desc_activo[1]
                        radio.push = lista[1]
            if pushed:
                self.desc_activo = lista.copy()

    def check_text(self, event):
        """Verificar acciones sobre text fields"""
        for text in self.text_fields_shape:
            text.get_event(event)

        for text in self.text_fields_color:
            text.get_event(event)

    def update_parametros(self):
        self.parametros['clases'] = str(len(self.data))
        etiquetas = ['Número de clases: ', 'Archivos verificados: ', 'Descriptor: ', 'Clasificador: ',
                     'Validación: ', 'Reducción dimensión: ']
        keys = ['clases', 'verified', 'descriptor', 'clasificador', 'validacion', 'reduccion']
        incremento = 10
        for etiqueta, key in zip(etiquetas, keys):
            self.screenform.blit(self.font.render(etiqueta + self.parametros[key],
                                                  True, BLACK), (self.rectaout[0] + 10, self.rectaout[1] + incremento))
            incremento += 30

    def run_all(self, close):
        """Función que ejecuta all"""
        valor_1 = 0
        self.build_buttons()
        self.build_textfields()
        while not close:
            self.mouse_position = pygame.mouse.get_pos()
            for event in pygame.event.get():
                self.check_text(event)
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
            self.block_all()
            self.update_parametros()
            self.clock.tick(60)
            pygame.display.flip()
