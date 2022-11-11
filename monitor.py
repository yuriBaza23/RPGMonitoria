import config
from datetime import datetime, timedelta
from random import randint

class Monitor:
    def __init__(self, name, subjects):
        self.name = name
        self.scholarship = 100
        self.subjects = subjects
        self.money = 0
        self.energy = 300
        self.cooldown = datetime.now()
        self.lvl = 1
        self.exp = 0
        self.waitingCooldown = 0

    def makeMonitoring(self):
        """O monitor começa a dar uma monitoria caso não esteja ocupado"""
        if self.isBusy() == 0:
            self.changeCooldown(config.info['monitoring']["cost"])
            self.useEnergy(config.info['monitoring']["cost"])
            self.gainExp(config.info['monitoring']["exp"])
            self.level()
            print('🏫 Você começou a dar uma monitoria.')
            return True
        print(f'😕 Você está ocupado agora... [O descanso vem em: {int(self.isBusy())}s]')
        return False

    def makeATask(self):
        if self.isBusy() == 0:
            number = randint(0, 4)
            res = input(config.tasks[number])
            if res.lower() == 's':
                self.changeCooldown(config.info['tasks']["cost"])
                self.useEnergy(config.info['tasks']["cost"])
                self.gainExp(config.info['tasks']['exp'])
                prob = randint(0, 8)
                if prob < 8:
                    self.gainMoney(config.resTasks[number]["pass"])
                    print(f'💵 Parabéns, você ganhou R${config.resTasks[number]["pass"]}')
                elif number == 2:
                    self.useMoney(config.resTasks[number]["fail"])
                    print(f'💵 Putz, você perdeu R${config.resTasks[number]["fail"]}')
                else:
                    print(f'🥲 Deu ruim... você não ganhou nada')
            else:
                print('Okay, fica pra próxima')
        else:
            print(f'😕 Você está ocupado agora... [O descanso vem em: {int(self.isBusy())}s]')

    def eatCracker(self):
        if self.money > config.data['cracker']['cost']:
            self.gainEnergy(config.data["cracker"]["energy"])
            print(f'🍪 Comendo uma bolachinha... [ +{config.data["cracker"]["energy"]}⚡️]')
        else:
            print('Você não tem dinheiro o suficiente pra comer isso...')

    # Métodos de apoio / simples ---------------------------------------------------------------------
    def level(self):
        if self.exp >= self.lvl * 100:
            self.lvl += 1
            self.gainMoney(self.scholarship)
            if self.lvl % 5 == 0:
                self.scholarship += 250
            print(f'🤩 Aopa! Agora você está no lvl {self.lvl}')

    def gainExp(self, quantity):
        """Aumenta o xp do monitor"""
        self.exp += quantity

    def useEnergy(self, quantity):
        """Decrementa a quantidade de energia do monitor"""
        self.energy -= quantity

    def gainEnergy(self, quantity):
        """Aumenta a quantidade de energia do monitor"""
        self.energy += quantity

    def useMoney(self, quantity):
        """Decrementa a quantidade de dinheiro do monitor"""
        self.money -= quantity

    def gainMoney(self, quantity):
        """Decrementa a quantidade de dinheiro do monitor"""
        self.money += quantity

    def isBusy(self):
        """Retorna 0 se o monitor não está ocupado e uma quantidade de segundos caso esteja"""
        if (self.cooldown - datetime.now()).total_seconds() <= 0:
            if self.waitingCooldown != 0:
                self.gainEnergy(self.waitingCooldown)
                self.waitingCooldown = 0
            return 0
        return (self.cooldown - datetime.now()).total_seconds()

    def changeCooldown(self, seconds):
        """Muda o cooldown para um tempo específico adicionando segundos"""
        self.cooldown = datetime.now() + timedelta(seconds=seconds)
        self.waitingCooldown = seconds

    def haveMoney(self):
        """Retorna se o monitor tem dinheiro na conta"""
        if self.money > 0:
            return True
        return False

    def __str__(self):
        """Imprime informações sobre o monitor"""
        if self.isBusy() > 0:
            busy = 'Sim'
        else:
            busy = 'Não'
        return f'🔥 Nível: {self.lvl}\n📝 Nome: {self.name}\n😰 Ocupado: {busy}\n💵 Bolsa: {self.scholarship}\n' \
               f'📚 Matérias: {self.subjects}\n💸 Dinheiro em conta: {self.money}\n⚡️ Energia: {self.energy}'