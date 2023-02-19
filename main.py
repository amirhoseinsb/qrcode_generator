#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 00:43:54 2023

@author: amir
"""
from qrcode_generator import get_string,create_qrcode,save_qrcode


class Handler:
    
    @staticmethod
    def run():
        name = get_string()
        qr = create_qrcode(string=name)
        save_qrcode(filename=name[0-21],qrcode=qr)
        
if __name__ == "__main__":
    Handler.run()