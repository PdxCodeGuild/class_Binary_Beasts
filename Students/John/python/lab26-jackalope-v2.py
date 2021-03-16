import random

class Population:
    
    def __init__(self, jacks):
        self.jackalopes = jacks
        self.time = 0
    
    def tick(self):
        self.time += 1
        random.shuffle(self.jackalopes)
        j = len(self.jackalopes) - 1
        while j >= 0:
            self.jackalopes[j].tick()
            if self.jackalopes[j].age in range(4, 9) and j != 0:
                if (self.jackalopes[j].sex == "F" and not self.jackalopes[j].pregnant) and \
                        (self.jackalopes[j - 1].sex == "M" and self.jackalopes[j - 1].age in range(4, 9)):
                    j1, j2 = self.jackalopes[j].reproduce()
                    self.jackalopes.append(j1)
                    self.jackalopes.append(j2)
            elif self.jackalopes[j].age in range(4, 9) and j != len(self.jackalopes) - 1:
                if (self.jackalopes[j].sex == "F" and not self.jackalopes[j].pregnant) and \
                        (self.jackalopes[j + 1].sex == "M" and self.jackalopes[j + 1].age in range(4, 9)):
                    j1, j2 = self.jackalopes[j].reproduce()
                    self.jackalopes.append(j1)
                    self.jackalopes.append(j2)
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
    
    def __init__(self, name, i, sex):
        self.name = name
        self.i = i
        self.sex = sex
    
    def reproduce(self):
        if self.sex == "F":
            self.pregnant = True
        return Jackalope("jack-" + str(self.i + 1), self.i, "M"), \
            Jackalope("jack-" + str(self.i + 2), self.i + 2, "F")
    
    def tick(self):
        self.age += 1
        if self.sex == "F":
            self.pregnant = False
      
p = Population([Jackalope("jack-1", 1, "M"), Jackalope("jack-2", 2, "F")])
p.tick()