# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 20:04:35 2020

@author: Samarendra
"""

import pygame 
from fourierLib import rotate,fourierSeries
from cmath import pi,exp,sqrt  


def main(file_name):
    pygame.init()

    '''pygame variables'''
    #define constants
    white,black = (255,255,255),(0,0,0)
    yellow = (255,255,0)
    win_size = 800
    #game display
    gameDisplay = pygame.display.set_mode((win_size,win_size))
    #clock
    clock = pygame.time.Clock()

    '''fourier constants'''
    #imaginary constant
    j = sqrt(-1)

    '''required functions'''
    def drawline(start,end,color=white, is_poly=False):
        start,end = start.conjugate(),end.conjugate()
        start += complex(win_size/2,win_size/2)
        end += complex(win_size/2,win_size/2)
        if is_poly and ((start.real - end.real)**2 + (start.imag - end.imag)**2 > 100):
            return
        pygame.draw.line(gameDisplay,color,
                (start.real,start.imag),(end.real,end.imag),1)
        
    def draw_poly(z_arr):
        for i, z in enumerate(z_arr[:-1]):
            if i != 0:
                drawline(z, z_arr[i+1], yellow, is_poly=True)
        

    '''Loop Variables'''
    done = False
    time = pygame.time.get_ticks()

    '''The code that you want to change'''
    #Number of circles is 2m+1
    m = 300
    #(small)z is the list of points and (big)Z is the fourier series#

    '''Reading from csv file'''
    import pandas as pd

    tmpz = pd.read_csv(file_name)
    z = tmpz['Coords'].apply(complex)
    z2_tmp = z
    z = z*exp(-j*pi/2)
    z = z.to_list()
    L = len(z)
    Z = fourierSeries(z,m)
    '''End'''

    '''Speed Of One Cycle'''
    phi = 5
    theta = j*(phi/L)*(2*pi)
    z_arr = []

    '''Code to animate the movement'''
    c = complex(0,0)
    stop_drawing = False
    seen_complex = set()

    while not done:
        
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                done = True
                
        gameDisplay.fill(black)
        
        if pygame.time.get_ticks() - time > 1:
            time = pygame.time.get_ticks()
            
            for n in range(1,m+1):

                if stop_drawing:
                    break
                
                Z[n] = rotate(Z[n],n*theta)
                Z[-n] = rotate(Z[-n],(-n)*theta)
                
                if (c != complex(0,0)) and (c not in seen_complex):
                    z_arr.append(c)
                    seen_complex.add(c)

                # print(theta.imag)
                # if theta.imag >= 2*pi:
                #     stop_drawing = True
        
        c = complex(0,0)
        
        for n in range(1,m+1):

            if stop_drawing:
                break

            drawline(c,c+Z[n])
            c += Z[n]
            drawline(c,c+Z[-n])
            c += Z[-n]
            
        draw_poly(z_arr)
        clock.tick(60)
        pygame.display.flip()
        
    pygame.quit()

if __name__ == "__main__":

    import sys

    files = {
        "train": './coords/thecodingtrain.csv',
        "simpson": './coords/simpsons.csv'
    }
    
    drawing = 'train'
    if (len(sys.argv) > 1) and (sys.argv[1] in files):
        drawing = sys.argv[1]

    main(files[drawing])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    














    