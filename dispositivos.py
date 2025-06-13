from abc import ABC, abstractmethod

#Classe Abstrata
class DispositivoInteligente(ABC):

    @abstractmethod
    def ligar():
        pass

    @abstractmethod
    def desligar():
        pass

    @abstractmethod
    def obter_status():
        pass

#Lâmpada Inteligente
class Lampada(DispositivoInteligente):
    def __init__(self, nome):
        self.nome = nome
        self.status = False

    def ligar(self):
        self.status = True
        return f"Ligando luzes..."
    
    def desligar(self):
        self.status = False
        return f"Desligando luzes..."
    
    def obter_status(self):
        return f"Lâmpada '{self.nome}"
    
    def obter_status(self):
        if self.status:
            return f"Lâmpada '{self.nome}': Ligada"
        else:
            return f"Lâmpada '{self.nome}': Desligada"

#Termostato Inteligente        
class Termostato(DispositivoInteligente):
    def __init__(self, nome, temperatura_alvo = 22):
        self.nome = nome
        self.status = False
        self.temperatura_alvo = temperatura_alvo

    def ligar(self):
        self.status = True
        return f"Ativando sistema de climatização..."
    
    def desligar(self):
        self.status = False
        return f"Desativando sistema de climatização..."
    
    def obter_status(self):
        if self.status:
            return f"Termostato '{self.nome}': Ligado, Temperatura alvo: {self.temperatura_alvo}"
        else:
            return f"Termostato '{self.nome}': Desligado"

#Fechadura Inteligente 
class Fechadura(DispositivoInteligente):
    def __init__(self, nome):
        self.nome = nome
        self.status = False

    #Ligar == Trancar
    def ligar(self):
        self.status = True #Trancada
        return f"Trancando '{self.nome}'..."
    
    #Desligar == Destrancar
    def desligar(self):
        self.status = False #Destrancada
        return f"Destrancando '{self.nome}'..."

    def obter_status(self):
        if self.status:
            return f"Fechadura '{self.nome}': Trancada"
        else:
            return f"Fechadura '{self.nome}': Destrancada"