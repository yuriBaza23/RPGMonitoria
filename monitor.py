import config
from random import randint
from config import info
from cooldown import Cooldown

class Monitor:
    def __init__(self, subjects):
        self.scholarship = 100
        self.subjects = subjects
        self.money = 1000
        self.info = info
        self.cooldown = Cooldown()

    def isBusy(self, people):
        """Retorna 0 se o monitor não está ocupado e uma quantidade de segundos caso esteja"""
        return self.cooldown.diffCooldown(people)

    def makeMonitoring(self, people, config):
        """O monitor começa a dar uma monitoria caso não esteja ocupado"""
        if self.isBusy(people) == 0:
            self.cooldown.changeCooldown(self.info['class']['cost'])
            people.useEnergy(self.info['class']['cost'])
            config.gainExp(self.info['class']['exp'])
            config.level()
            print('🏫 Você começou a dar uma monitoria.')
            return True
        print(f'😕 Você está ocupado agora... [O descanso vem em: {int(self.isBusy(people))}s]')
        return False

    # def makeATask(self):
    #     if self.isBusy() == 0:
    #         number = randint(0, 4)
    #         res = input(config.tasks[number])
    #         if res.lower() == 's':
    #             self.changeCooldown(config.info['tasks']["cost"])
    #             self.useEnergy(config.info['tasks']["cost"])
    #             self.gainExp(config.info['tasks']['exp'])
    #             prob = randint(0, 8)
    #             if prob < 8:
    #                 self.gainMoney(config.resTasks[number]["pass"])
    #                 print(f'💵 Parabéns, você ganhou R${config.resTasks[number]["pass"]}')
    #             elif number == 2:
    #                 self.useMoney(config.resTasks[number]["fail"])
    #                 print(f'💵 Putz, você perdeu R${config.resTasks[number]["fail"]}')
    #             else:
    #                 print(f'🥲 Deu ruim... você não ganhou nada')
    #         else:
    #             print('Okay, fica pra próxima')
    #     else:
    #         print(f'😕 Você está ocupado agora... [O descanso vem em: {int(self.isBusy())}s]')

    # def eatCracker(self):
    #     if self.money > config.data['cracker']['cost']:
    #         self.gainEnergy(config.data["cracker"]["energy"])
    #         print(f'🍪 Comendo uma bolachinha... [ +{config.data["cracker"]["energy"]}⚡️]')
    #     else:
    #         print('Você não tem dinheiro o suficiente pra comer isso...')