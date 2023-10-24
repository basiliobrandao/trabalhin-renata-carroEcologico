class Carro_Ecologico:
    def __init__(self, tanque=0,quilometragem=0, pessoas=0):
        self.tanque = tanque
        self.quilometragem = quilometragem
        self.pessoas = pessoas
    
    def entrar(self, num_pessoas):
        if self.pessoas + num_pessoas <= 2:
            self.pessoas += num_pessoas
            return f"{num_pessoas} pessoa entrou no carro"

        else:
            return "O carro está lotado"

    def sair(self, num_pessoas):
        if self.pessoas - num_pessoas < 2:
            self.pessoas -= num_pessoas
            return f"{num_pessoas} pessoa saiu no carro"

        else:
            return "Não há pessoas suficientes no carro"
        
carro = Carro_Ecologico()

print(carro.entrar())
print(carro.sair())
       
