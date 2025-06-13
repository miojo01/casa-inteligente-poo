class ControladoraCasa:
    def __init__(self):
        self.dispositivos = []

    def adicionar_dispositivo(self, dispositivo):
        self.dispositivos.append(dispositivo)

    def ligar_todos(self):
        for dispositivo in self.dispositivos:
            dispositivo.ligar()

    def desligar_todos(self):
        for dispositivo in self.dispositivos:
            dispositivo.desligar()

    def status_geral(self):
        for dispositivo in self.dispositivos:
            print(dispositivo.obter_status())