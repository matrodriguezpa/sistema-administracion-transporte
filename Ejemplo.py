class Terrestre:
    def desplazar(self):
        print("El animal camina.")

class Acuatico:
    def desplazar(self):
        print("El animal nada.")

class Cocodrilo(Terrestre,Acuatico):
    pass

def main():
    juancho = Cocodrilo()
    juancho.desplazar()

main()
