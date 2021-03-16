class Population:
    
    def __init__(self, jacks):
        self.jackalopes = jacks
        self.time = 0
    
    def tick(self):
        self.time += 1
        j = len(self.jackalopes) - 1
        while j >= 0:
            self.jackalopes[j].tick()
            if self.jackalopes[j].age in range(4, 9):
                self.jackalopes.append(self.jackalopes[j].reproduce())
            if self.jackalopes[j].age == 10:
                self.jackalopes.remove(self.jackalopes[j])
            j -= 1
                
        print(f"{self.time}: {len(self.jackalopes)}")
        if len(self.jackalopes) < 1000:
            self.tick()
        else:
            print(f"Years: {self.time}")

class Jackalope:
    age = 0
    
    def reproduce(self):
        return Jackalope()
    
    def tick(self):
        self.age += 1
      
p = Population([Jackalope(), Jackalope()])
p.tick()