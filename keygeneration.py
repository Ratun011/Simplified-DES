
class keygeneration:
    
    def __init__(self):
        self.hexa = input("The Key in Hexa:\n")
        binary=bin(int(self.hexa, 16))[2:].zfill(24)
        k= []
        for i in str(binary):
             k.append(int(i))
        self.pc1=[k[16],k[8],k[0],
             k[17],k[9],k[1],
             k[18],k[10],k[2],
             k[22],k[14],k[6],
             k[21],k[13],k[5],
             k[20],k[12],k[4],
             k[19],k[11],k[3]]
        self.shift_table=[1,1,2,2,2,2]
    
    def shiftLeft(self,array, n):
        shifted=array[n:]+array[:n]
        return shifted
    
    def table_pc2(self,m):
        pc2=[m[16],m[10],m[0],m[4],m[2],m[14],
             m[5],m[17],m[9],m[18],m[11],m[3],
             m[7],m[15],m[8],m[19],m[12],m[1]]
        return pc2
    
    
    def gen(self):
        length=int(len(self.pc1)/2)
        c=self.pc1[:length]
        d=self.pc1[length:]
        all_keys=[]
        print("\n")
        print("Key Generation rounds\n")
        for i in range(6):
            print("Round",i+1)
            ci=self.shiftLeft(c,self.shift_table[i])
            di=self.shiftLeft(d,self.shift_table[i])
            new=ci+di
            key=self.table_pc2(new)
            all_keys.append(key)
            print("The key:",key)
            c=ci
            d=di
        return all_keys
  

    
