from datetime import datetime, timedelta

class Cooldown:
    def __init__(self):
        self.waitingCooldown = 0
        self.cooldown = datetime.now()

    def changeCooldown(self, seconds):
        """Muda o cooldown para um tempo específico adicionando segundos"""
        self.cooldown = datetime.now() + timedelta(seconds=seconds)
        self.waitingCooldown = seconds

    def diffCooldown(self, people):
        if (self.cooldown - datetime.now()).total_seconds() <= 0:
            if self.waitingCooldown != 0:
                people.gainEnergy(self.waitingCooldown)
                self.waitingCooldown = 0
            return 0
        return (self.cooldown - datetime.now()).total_seconds()