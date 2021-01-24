class Complex (object):
    def __init__(self, realPart, imagPart):
        self.realPart = realPart
        self.imagPart = imagPart            

    def __str__(self):
         if self.imagPart == 0:
            result = "%.2f+0.00i" % (self.realPart)
         elif self.realPart == 0:
            if self.imagPart >= 0:
                result = "0.00+%.2fi" % (self.imagPart)
            else:
                result = "0.00-%.2fi" % (abs(self.imagPart))
         elif self.imagPart > 0:
            result = "%.2f+%.2fi" % (self.realPart, self.imagPart)
         else:
            result = "%.2f-%.2fi" % (self.realPart, abs(self.imagPart))
         return result

    def __add__(self, other):
        r1 = self.realPart
        i1 = self.imagPart
        r2 = other.realPart
        i2 = other.imagPart
        resultR = r1+r2
        resultI = i1+i2
        result = Complex(resultR, resultI)
        return result

    def __sub__(self, other):
        r1 = self.realPart
        i1 = self.imagPart
        r2 = other.realPart
        i2 = other.imagPart
        resultR = r1-r2
        resultI = i1-i2
        result = Complex(resultR, resultI)
        return result   

    def __mul__(self, other):
        r1 = self.realPart
        i1 = self.imagPart
        r2 = other.realPart
        i2 = other.imagPart
        resultR = (r1*r2-i1*i2)
        resultI = (r1*i2+r2*i1)
        result = Complex(resultR, resultI)
        return result

    def __div__(self, other):
        r1 = self.realPart
        i1 = self.imagPart
        r2 = other.realPart
        i2 = other.imagPart
        resultR = float(float(r1*r2+i1*i2)/float(r2*r2+i2*i2))
        resultI = float(float(r2*i1-r1*i2)/float(r2*r2+i2*i2))
        result = Complex(resultR, resultI)
        return result

c1 = Complex(2,3)
c2 = Complex(1,4)

print (c1+c2)
print (c1-c2)
print (c1*c2)
print (c1/c2)
