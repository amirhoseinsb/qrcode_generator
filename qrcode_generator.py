#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 00:14:57 2023

@author: amir
"""

import qrcode
from config import BANNER

def get_string():
    text = input(str(BANNER))
    return text

def create_qrcode(string):
    text = string
    generator = qrcode.make(data=text)
    return generator 

def save_qrcode(filename,qrcode):
    generator = qrcode
    filename = filename
    generator.save(f'{filename}.png')