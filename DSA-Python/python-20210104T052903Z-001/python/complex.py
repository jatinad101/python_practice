class complex:
    def __init__(self,real,img):
        self.real= real
        self.img = img

    def __add__(self,comp1):
        newreal = self.real + comp1.real
        newimg  = self.img  + comp1.img
        comp2   = complex(newreal,newimg)
        return comp2
c1=complex(2,1)
c2=complex(3,5)
c3= c1+c2
print(c3.real,c3.img)
