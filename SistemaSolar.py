#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 23:36:58 2020

@author: juanjo
"""

import numpy as np

''' El programa almacenará en cada fichero la x, y, vx, vy, ax, ay en ese orden'''

''' Vamos a empezar definiendo las funciones que vamos a usar para el programa: '''

def CalcularAceleracion(X, Y,  M, x, y, m):
    ''' X es la lista de la componente x de las distancias de los planetas al Sol, 
    Y es la lista de la componente y de las distancias de los planetas al Sol, 
    M es la lista 
    de las masas de los planetas, r es la distancia del planeta al que le que-
    remos calcular la aceleración al Sol, m es la masa del planeta al que le 
    queremos calcular la aceleración.'''
    
    
    if (len(M) != len(X)):
        print('Tenemos un problema')
    else:
        sumax = 0.0
        sumay = 0.0
        for i in range(0, len(M)):
            if(float(M[i]) != float(m)):
                sumax += -(M[i]*(x - X[i]))/(((((x- X[i])**2) + ((y - Y[i])**2)))**1.5)
                sumay += -(M[i]*(y - Y[i]))/(((((x- X[i])**2) + ((y - Y[i])**2)))**1.5)
    return sumax, sumay

def CalcularPosicion(h, X, Y, Vx, Vy, ax, ay):
    ''' Esta función nos calcula el valor de la posicion en un tiempo t+h a 
    partir de las variables en el tiempo t.'''
    for i in range (0, len(X)):
        X[i] = X[i] + h*Vx[i] + 0.5*h*h*ax[i]
        Y[i] = Y[i] + h*Vy[i] + 0.5*h*h*ay[i]
    return 

def CalcularW(Vx, Vy, ax, ay, h, Wx, Wy):
    for i in range(0, len(Vx) ):
        Wx[i] = Vx[i] + 0.5*h*ax[i]
        Wy[i] = Vy[i] + 0.5*h*ay[i]
    return 

def CalcularVelocidad(Wx, Wy, h, ax, ay, Vx, Vy):
    for i in range(0, len(ax)):
        Vx[i] = Wx[i] + 0.5*h*ax[i]
        Vy[i] = Wy[i] + 0.5*h*ay[i]
    return

''' Empezamos con el programa en sí: '''


h = float(input(' Salto temporal: '))
lim = float(input(' Dame el limite temporal: '))
t = 0.0 

#X, Y, Vx, Vy, ax, ay, M = [], [], [], [], [], [], []
fdatos = open('datos.dat', 'r')

X = np.loadtxt('datos.dat', usecols = (0))
X = X.tolist()

Y = np.loadtxt('datos.dat', usecols = (1))
Y = Y.tolist()

Vy = np.loadtxt('datos.dat', usecols = (2))
Vy = Vy.tolist()

M = np.loadtxt('datos.dat', usecols = (3))
M = M.tolist()

Vx = np.zeros_like(M).tolist()
#Vx = Vx.tolist()

ax, ay = np.zeros_like(M).tolist(), np.zeros_like(M).tolist()
Wx, Wy = np.zeros_like(M).tolist(), np.zeros_like(M).tolist()

file = list([])
f = list([])

for i in range(0, len(M)):
    file.append('planeta' + str(i) + '.dat')
    ax[i], ay[i] = CalcularAceleracion(X, Y, M, X[i], Y[i], M[i])
    f.append(open(file[i], 'w'))
    f[i].write(str(X[i]) +' ' + str(Y[i]) + ' ' + str(Vx[i]) + ' ' + str(Vy[i]) + ' ' + str(ax[i]) + ' ' + str(ay[i]) + ' ' + str(0) + '\n')

while(lim > t):
   CalcularPosicion(h, X, Y, Vx, Vy, ax, ay)
   CalcularW(Vx, Vy, ax, ay, h, Wx, Wy)
   for i in range(0, len(M)):
       ax[i], ay[i] = CalcularAceleracion(X, Y, M, X[i], Y[i], M[i])
   CalcularVelocidad(Wx, Wy, h, ax, ay, Vx, Vy)
   for i in range(0, len(M)):
       f[i].write(str(X[i]) +' ' + str(Y[i]) + ' ' + str(Vx[i]) + ' ' + str(Vy[i]) + ' ' + str(ax[i]) + ' ' + str(ay[i]) + ' ' + str(t) +'\n')
   t += h
fdatos.close()
print('Han pasado ' + str(t/0.01720306409) + ' días')
for i in range(0, len(M)):
    f[i].close()
