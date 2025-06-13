from dispositivos import Lampada, Termostato, Fechadura
from controladora import ControladoraCasa

#Criando a central de controle
central = ControladoraCasa()

#Criando e adicionando dispositivos
lampada_sala = Lampada("Sala")
termostato_quarto = Termostato("Quarto", 24)
termostato_sala = Termostato("Sala")
fechadura_entrada = Fechadura("Entrada")

central.adicionar_dispositivo(lampada_sala)
central.adicionar_dispositivo(termostato_quarto)
central.adicionar_dispositivo(termostato_sala)
central.adicionar_dispositivo(fechadura_entrada)

#Operações
central.ligar_todos()
central.status_geral()

print("\n--- Após Desligar ---\n")

central.desligar_todos()
central.status_geral()
