# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 17:29:21 2019

@author: Marcin
"""

import sys
import keyboard

while True:
    print("Nacisnij 'q' aby zakonczyc program")
    if keyboard.is_pressed('q'):
        sys.exit()