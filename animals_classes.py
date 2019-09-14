class MyAnimals():
    def __init__(self,run,hop,swim,fly):
        
        self.run = run
        self.hop = hop
        self.swim = swim
        self.fly = fly
        
    def Dog(self):
        print("Dogs can {}".format(self.run))
        
    def Rabbit(self):
        print("Rabbits can {}".format(self.hop))
        
    def Fish(self):
        print("Fishes can {}".format(self.swim))
        
    def Birds(self):
        print("Birds can {}".format(self.fly))
