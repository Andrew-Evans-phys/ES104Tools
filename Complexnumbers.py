


class Complex:
    def __init__(self,x,i):
        self.x = x
        self.i = i

    def getcomplex(self):
        if self.i == 1:
            print("("+str(self.x)+",", "i"+")")
        elif self.i == 0:
            print("("+str(self.x)+",","0)")
        elif self.i == -1:
            print("("+str(self.x)+",", "-i"+")")
        else:
            print("("+str(self.x)+",", str(self.i)+"i"+")")
        return self.x, self.i

    def Addition(self,o):
        self.x = self.x + o.x
        self.i = self.i + o.i
    
    def scalarmulti(self,c):
        self.x = self.x*c
        self.i = self.i*c

    def complexmulti(self,o):
        self.tempx = (self.x)*(o.x)-(self.i)*(o.i)
        self.tempi = (self.x)*(o.i)+(self.i)*(o.x)
        self.x = self.tempx
        self.i = self.tempi
    
    def complexdivision(self, o):
        self.conx = o.x
        self.coni = -o.i
        self.tempx = (self.x)*(self.conx)-(self.i)*(self.coni)
        self.tempi = (self.x)*(self.coni)+(self.i)*(self.conx)
        self.x = self.tempx
        self.i = self.tempi
        self.dx = (o.x)*(self.conx)-(o.i)*(self.coni)
        self.di = (o.x)*(self.coni)+(o.i)*(self.conx)
        self.x = self.x/(self.dx+self.di)
        self.i = self.i/(self.dx+self.di)


    
b = Complex(5,3)
a = Complex(2,-1)

a.complexdivision(b)
a.getcomplex()