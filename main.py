# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 23:45:49 2020

@author: User
"""
from decryption import *
from encryption import *

if __name__=='__main__':
    task=input("The DES Procedure (D\E):")
    task=task.lower()
    if task[0]=='d':
        d=decrypt()
        d.decryption()
    elif task[0]=='e':
        e=encrypt()
        e.encryption()
    else:
        print("No Procedure As such")