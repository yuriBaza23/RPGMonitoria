from monitor import Monitor
from config import Config
from datetime import datetime, timedelta

class People:
    def __init__(self, name, sex, subject):
        """Inicializa um jogador"""
        self.name = name
        self.sex = sex
        self.energy = 100
        self.monitor = Monitor(subject)
        self.config = Config()

    def __str__(self):
        """Imprime informações sobre o jogador"""
        if self.isBusy() > 0:
            busy = 'Sim'
        else:
            busy = 'Não'
        return f'+-DADOS DO JOGADOR----------------\n' \
               f'🔥 Nível: {self.config.lvl}\n📝 Nome: {self.name}\n🧬 Sexo: {self.whatSex()}\n😰 Ocupado: {busy}\n' \
               f'⚡️ Energia: {self.energy}\n' \
               f'+-DADOS DE MONITORIA--------------\n' \
               f'💵 Bolsa: {self.monitor.scholarship}\n📚 Matérias: {self.monitor.subjects}\n' \
               f'💸 Dinheiro em conta: {self.monitor.money}\n' \

    def useEnergy(self, quantity):
        """Decrementa a quantidade de energia do monitor"""
        self.energy -= quantity

    def gainEnergy(self, quantity):
        """Aumenta a quantidade de energia do monitor"""
        self.energy += quantity

    def isBusy(self):
        """Retorna 0 se o monitor não está ocupado e uma quantidade de segundos caso esteja"""
        return self.monitor.isBusy(self)

    def whatSex(self):
        """Retorna qual o sexo do jogador"""
        if self.sex == 'm':
            return 'Masculino'
        else:
            return 'Feminino'

    def makeSomething(self, something):
        if something == 'class':
            self.monitor.makeMonitoring(self, self.config)