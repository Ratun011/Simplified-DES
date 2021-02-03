# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 02:51:34 2020

@author: User
"""
from keygeneration import * 

class decrypt:
    
    def __init__(self):
        keyobject=keygeneration()
        self.hexa = input("The Cipher Text:\n")
        binary=bin(int(self.hexa, 16))[2:].zfill(24)
        pt= []
        for i in str(binary):
            pt.append(int(i))
          
        self.ip=[pt[18-1], pt[10-1], pt[2-1],
                 pt[20-1], pt[12-1], pt[4-1],
                 pt[22-1], pt[14-1], pt[6-1],
                 pt[24-1], pt[16-1], pt[8-1],
                 pt[17-1], pt[9-1], pt[1-1],
                 pt[19-1], pt[11-1], pt[3-1], 
                 pt[21-1], pt[13-1], pt[5-1], 
                 pt[23-1], pt[15-1], pt[7-1]]
        
        length=int(len(self.ip)/2)
        self.Left=self.ip[:length]
        self.Right=self.ip[length:]
        print("Initial Permutation =",self.ip)
        print("Left ", self.Left)
        print("Right ", self.Right)
        self.keys=keyobject.gen()
    
    def permu(self,m):
        p= [m[7-1],m[12-1],m[1-1],m[5-1]
           ,m[10-1],m[2-1],m[8-1],m[3-1]
           ,m[9-1],m[6-1],m[11-1],m[4-1]]
        return p
    
    
    def extend(self,ex):
        EX = [ex[12-1],  ex[1-1],  ex[2-1],  ex[3-1],  ex[4-1], ex[5-1],
                 ex[4-1],  ex[5-1],  ex[6-1],  ex[7-1],  ex[8-1],  ex[9-1], 
                 ex[8-1],  ex[9-1],  ex[10-1], ex[11-1], ex[12-1], ex[1-1]]
        return (EX)
    
    def s_box(self):
        s1 =    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
                 [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
                 [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
                 [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]
        s2 =    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
                 [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
                 [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
                 [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]]
        s3 =    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
                 [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
                 [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
                 [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]]
        
        return [s1, s2, s3]
    
    
    def decryption(self):
        for x in range(6):
            extend_right=self.extend(self.Right)
            print("\n")
            print ()
            print ("Round:", x+1)
            print ("\n")
            print("Expanded Right:", extend_right)
            new=[]
            key=self.keys[5-x]
            print("Key:", key)
            
            for i in range(18):
                    new.append(extend_right[i] ^ key[i])     
               
            print("XOR rult:", new)
        
            new= list(map(str, new))
            temp1=[]
            sbox =self.s_box()
            y=0
            for x in range (0,18,6):
                temp = sbox[y][int(''.join(new[x]+new[x+5]),2)][int(''.join(new[x+1:x+5]),2)]
                if y < 3: 
                    y+=1
                temp=bin(int(temp))[2:].zfill(4)
                temp1.append([int(i) for i in str(temp)])
            array1=[]
            for i in range(3):
                for j in range(4):
                    array1.append(temp1[i][j])
            print("S BOX output ",  array1)
            array1=self.permu(array1)
            print("Output of permutation function ",  array1)
            array2=[]
            for i in range(12):
                    array2.append(array1[i] ^ self.Left[i])
            self.Left=self.Right
            self.Right=array2
            print("New Right ", self.Right)
            print("New Left ", self.Left)
        
        self.Right, self.Left = self.Left, self.Right
        r=self.Left+self.Right
        inverse_ip =[r[15-1], r[3-1], r[18-1],
                     r[6-1], r[21-1], r[9-1],
                    r[24-1], r[12-1],r[14-1],
                    r[2-1], r[17-1], r[5-1], 
                    r[20-1], r[8-1], r[23-1], 
                    r[11-1], r[13-1], r[1-1], 
                    r[16-1], r[4-1], r[19-1],
                    r[7-1], r[22-1], r[10-1]]
        print("\n")            
        print("Plain Text in Binary :", inverse_ip)
        inverse_ip= map(str, inverse_ip)
        inverse_ip=''.join(inverse_ip)
        inverse_ip=hex(int(inverse_ip, 2))[2:].zfill(6)
        print("Plain text in Hex :", inverse_ip)
