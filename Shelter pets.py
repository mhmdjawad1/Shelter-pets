class pet:
    def __init__(self,name,species,age):
        self.name=name
        self.species=species
        self.age=age
        self.adopted=False


    def display_info(self):
        current_status = "adopted" if self.adopted else "not adopted"
        print( self.name," is",self.age,"years old and its a",self.species,"and its currently",current_status)

    def mark_adopted(self):
        self.adopted=True
    
    def birthday(self):
        self.age+=1
   
    def rename(self, new_name):
        print(f"Renaming {self.name} to {new_name}")
        self.name = new_name



pet1=pet("Max","cat",int("1"))

pet2=pet("Dex","dog",int("2"))

pet3=pet("Leo","cat",int("3"))

pet1.display_info()
pet2.display_info()
pet3.display_info()


pet1.birthday()
pet2.mark_adopted()



pet1.display_info()
pet2.display_info()
pet3.display_info()

#__________________________________________________________

pets = [
    pet("Mila", "rabbit", 3),
    pet("Lara", "dog", 2),
    pet("Rey", "dog", 2),
    pet("Nala", "rabbit", 4),
]

pets[0].mark_adopted()
pets[3].mark_adopted()

def find_non_adopted(pets):
    non_adopted_pets = []
    for p in pets:
        if not p.adopted:
            non_adopted_pets.append(p)
    return non_adopted_pets

pets[0].rename("Kay")



print("Pets:")
for p in pets:
    p.display_info()

