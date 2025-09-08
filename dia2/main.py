import math

def calcRaizQuadrada(valor):
    return(math.sqrt(valor))

def arrendondador(valor):
    decimal = valor - int(valor)
    if decimal>0.5:
        return math.ceil(valor)
    else:
        return math.floor(valor)
    
class figuraGeometrica:
    @staticmethod
    def areaCirculo(raio):
        return(math.pi * math.pow(raio,2))
    @staticmethod
    def areaTriangulo(base,altura):
        return((base*altura)/2)
    @staticmethod
    def hipotenusa(catetoA,catetoB):
        return(math.pow(catetoA,2)+math.pow(catetoB,2))

calculadora = figuraGeometrica
escolha = int(input("Insira o que deseja:\n" \
                    "1- Calcular área de um círculo\n" \
                    "2- Calcular a área de um triângulo\n" \
                    "3- Calcular a hipotenusa de um triângulo retângulo\n"\
                    "Escolha: "))

if escolha==1:
    calculadora.areaCirculo(float(input("Insira a área: ")))
elif escolha==2:
    calculadora.areaTriangulo(float(input("Insira a base do triângulo: ")),
                                float(input("Insira a área do triângulo: ")))
elif escolha==3:
    calculadora.hipotenusa(float(input("Insira o cateto A: ")),
                            float(input("Insira o cateto B: ")))