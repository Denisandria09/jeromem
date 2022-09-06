
   
class capteur:
    def __init__(self,gnd,vcc):
        self.gnd=gnd
        self.vcc=vcc

class temp(capteur):
        def __init__(self,pin,out):
          # super().__init__(lgt, np)
           self.pin=pin
           self.out=out
           
class couleur(capteur):
        def __init__(self,S0,S1,S2,S3,out):
           self.S0=S0
           self.S1=S1
           self.S2=S2
           self.S3=S3
           self.out=out
           
           
        def affiche1(self):
            print("out:",self.out)
           
B=temp("pin9",[1,2,3])

B.affiche1()


