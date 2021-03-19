#Version 1

class Population:
    
    def __init__(self, jacks):
        self.jackalopes = jacks
        self.time = 0
    
    def tick(self):
        self.time += 1
        i = len(self.jackalopes) - 1
        while i >= 0:
            self.jackalopes[i].tick()
            if self.jackalopes[i].age in range(4, 9):
                self.jackalopes.append(self.jackalopes[i].reproduce())
            if self.jackalopes[i].age == 10:
                self.jackalopes.remove(self.jackalopes[i])
            i -= 1
                
        print(f"Year: {self.time}, Population: {len(self.jackalopes)}")
        if len(self.jackalopes) < 1000:
            self.tick()
        else:
            print(f"Years to reach population 1000: {self.time}")

class Jackalope:
    age = 0
    
    @staticmethod
    def reproduce():
        return Jackalope()
    
    def tick(self):
        self.age += 1
      
p = Population([Jackalope(), Jackalope()])
p.tick()