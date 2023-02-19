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
        try:
            save_qrcode(filename=name[0:20],qrcode=qr)
        except:
            save_qrcode(filename='file',qrcode=qr)
            
if __name__ == "__main__":
    Handler.run()