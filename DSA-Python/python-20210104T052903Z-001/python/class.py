class car:
    def __init__(self,comp,model_no,color): #init is constructor self is storing its value

        self.comp  = comp
        self.model_no = model_no
        self.color = color
        self.kmrun = 0


    def run(self,dist):
        self.kmrun+=dist

    def howmuchrun(self):
        return self.kmrun

a=car("BMW","A100","RED")
print (a.model_no)
a.run(10)
print(a.howmuchrun())
        
