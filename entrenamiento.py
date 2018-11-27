#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 12:18:38 2018

Ejemplo de Red Neuronal para comprender su funcionamiento.

@author: MedinaAJ
"""

from perceptron import Perceptron

## Datos de hombres y mujeres
input_data = [[1.7,56,1], # Mujer de 1.70m y 56kg
              [1.72,63,0],# Hombre de 1.72m y 63kg
              [1.6,50,1], # Mujer de 1.60m y 50kg
              [1.7,63,0], # Hombre de 1.70m y 63kg
              [1.74,66,0],# Hombre de 1.74m y 66kg
              [1.58,55,1],# Mujer de 1.58m y 55kg
              [1.83,80,0],# Hombre de 1.83m y 80kg
              [1.82,70,0],# Hombre de 1.82m y 70kg
              [1.65,54,1]]# Mujer de 1.65m y 54kg

## Creamos el perceptron
pr = Perceptron(3) # Perceptron con 3 entradas

## Fase de entrenamiento
for _ in range(100):
    # Vamos a entrenarlo varias veces sobre los mismos datos
    # para que los 'pesos' converjan
    for person in input_data:
        output = person[-1]
        inp = [1] + person[0:-1] # Agregamos un uno por default
        err = pr.train(inp,output)

h = float(raw_input("Introduce tu estatura en centimetros.- "))
w = float(raw_input("Introduce tu peso en kilogramos.- "))

if pr.predict([1,h,2]) == 1: print "Mujer"
else: print "Hombre"

'''
Como conclusión, vale la pena mencionar también que clasificar perfectamente 
a hombres y mujeres por peso y estatura no es posible, pero con este 
algoritmo podemos obtener una predicción razonable.
'''