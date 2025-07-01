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



    





    
