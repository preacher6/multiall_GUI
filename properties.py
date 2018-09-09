#!/usr/bin/env python
# -*- coding: utf-8 -*-

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