class Animal:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        return "Oi eu sou um animal!"
    
    def apresentar(self):
        return f"Oi eu sou {self.nome} e tenho {self.idade} anos {self.falar}"
    
class Cachorro(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def falar(self):
        return "Auau rs"
    
class Gato(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        
    def falar(self):
        return "Miar kkkk"

class Zoologico(Animal):
    def __init__(self):
        self.animais = []

    def adicionar_Animal(self, *animal):
        self.animais.extend(animal)

    def mostrar_Animais(self):
        for animal in self.animais:
            print(animal.apresentar())
    
    def mostrar_Filtrado(self,raca):
        for animal in self.animais:
            if(isinstance(animal,raca)):
                print(animal.apresentar())


#Animais
gatoDoInteior = Cachorro("Cachorro",6)
senhorAnimal = Animal("MrAnimal",24)
gato = Gato("Gato",1)
#Zoológico
zoo = Zoologico()
zoo.adicionar_Animal(gatoDoInteior,senhorAnimal,gato)
zoo.mostrar_Filtrado(Animal)

#print("O que o gato do interior falou? "+gatoDoInteior.apresentar())

