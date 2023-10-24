class CarroEcologico:
    def __init__(self, tanque=0,quilometragem=0, pessoas=0):
        self.tanque = tanque
        self.quilometragem = quilometragem
        self.pessoas = pessoas
    
    def entrar(self, num_pessoas):
        if self.pessoas + num_pessoas <= 2:
            self.pessoas += num_pessoas
            print(f"{num_pessoas} pessoa(s) entrou/entraram no carro")

        else:
            print("O carro está lotado")

    def sair(self, num_pessoas):
        if self.pessoas - num_pessoas <= 2:
            self.pessoas -= num_pessoas
            print(f"{num_pessoas} pessoa(s) saiu/sairam no carro")

        else:
            print("Não há pessoas suficientes no carro")
       