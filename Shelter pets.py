class pet:
    def __init__(self,name,species,age,adopted):
        self.name=name
        self.species=species
        self.age=age
        self.adopted=False
    def display_info(self):
        print("Pet name is", self.name," and age is",self.age,"and its a",self.species)
    
