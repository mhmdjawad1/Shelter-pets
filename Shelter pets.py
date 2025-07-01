class pet:
    def __init__(self,name,species,age,):
        self.name=name
        self.species=species
        self.age=age
        self.adopted=False


    def display_info(self):
        print("Pet name is", self.name," and age is",self.age,"and its a",self.species,"and its",self.adopted)

    def mark_adopted(self):
        self.adopted=True
    
    def birthday(self):
        self.age+=1

p1=pet("dax","cat",int("1"))

p2=pet("dex","dog",int("2"))

p3=pet("max","cat",int("3"))



    





    
