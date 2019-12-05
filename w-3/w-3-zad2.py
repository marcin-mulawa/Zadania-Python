# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 16:43:44 2019

@author: Marcin
"""

# Zad 2
import matplotlib.pyplot as plt


def rysuj(x, y):
     plt.plot(x,y)
     plt.legend(('f(x)',))
     plt.xlabel('x')
     plt.ylabel('y')
     plt.show()