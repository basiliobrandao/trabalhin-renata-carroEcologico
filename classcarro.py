class Carro_Ecologico:
    def __init__(self,modelo, cor):
        self.modelo = modelo
        self.cor = cor
        self.tanque = 0
        self.quilometragem = 0
        self.pessoas = 0
        self.max_pessoas = 2
        self.teto_solar_aberto = False
    
    def entrar(self):
        
        if self.pessoas < self.max_pessoas:
            self.pessoas += 1 
            return "Uma pessoa entrou no carro."

        else:
            return "O carro está lotado."

    def sair(self):
        
        if self.pessoas > 0:
            self.pessoas -= 1
            return  "Uma pessoa saiu no carro."

        else:
            return "Não há pessoas dentro do carro."
        
    def abastecer(self, litros):
        
        espaco_disponivel = 100 - self.tanque
        
        if espaco_disponivel > 0:
            if litros <= espaco_disponivel:
                self.tanque += litros
                return f"Abastecido com {litros} litros de água."
            else:
                self.tanque = 100  
                return "O tanque foi completamente abastecido."
        else:
            return "O tanque já está cheio e não pode ser abastecido mais."
    
    def dirigir(self,distancia):
        
        if self.pessoas > 0:
            kilometros_maximos = min(self.tanque, distancia)
            self.tanque -= kilometros_maximos
            self.quilometragem += kilometros_maximos
            if kilometros_maximos < distancia:
                return f"A viagem não concluída totalmente. Só foi possivél andar {kilometros_maximos} Km."
            
            else:
                return f"O carro andou {kilometros_maximos} Km."
            
        else:
            print("Não é possível andar com o carro. Certifique-se se existem pessoas e combustivél suficiente no carro.")
            kilometros_maximos = 0
        return kilometros_maximos
                   
    def abrir_TetoSolar(self):
        if not self.teto_solar_aberto:
            self.teto_solar_aberto = True
            return "Teto solar abriu."
        
        else:
            return "O teto solar já está aberto."
        
    def fechar_TetoSolar(self):
        
        if self.teto_solar_aberto:
            self.teto_solar_aberto = False
            return "Teto solar fechou."
        else:
            return "O teto solar já fechou."
        
    def buzinar(self):
        return "Bip Bip, sai da frente!!!"
    
    def info(self):
        teto_solar = "Aberto" if self.teto_solar_aberto else "Fechado."
        return f"Carro Ecológico: \n Tanque: {self.tanque} litros.\n Quilometragem: {self.quilometragem} km.\n Pessoas: {self.pessoas}.\n Teto Solar: {teto_solar}. \n Modelo: {self.modelo}. \n Cor: {self.cor}."
        
carro = Carro_Ecologico('Fiat', 'Preto')

print(carro.entrar())
print(carro.entrar())

print(carro.sair())

print(carro.abastecer(90))

print(carro.abrir_TetoSolar())
print(carro.buzinar())

print(carro.fechar_TetoSolar())

print(carro.abrir_TetoSolar())

distancia_percorrida = carro.dirigir(80)

print(f"Informações do Carro Ecológico:")
print(carro.info())

print(f"Quilometragem total: {carro.quilometragem} km")
print(f"Água restante no tanque: {carro.tanque} litros")
print(f"Distância percorrida: {distancia_percorrida}")
