from random import randint
from datetime import datetime, timedelta

class Config:
    def __init__(self):
        self.lvl = 1
        self.exp = 0

    def level(self):
        """Faz updates de nível dependendo da experiência adquirida"""
        if self.exp >= self.lvl * 100:
            self.lvl += 1
            if self.lvl % 5 == 0:
                print(f'🤩 Aopa! Agora você está no lvl {self.lvl}')

    def gainExp(self, quantity):
        """Aumenta o xp do monitor"""
        self.exp += quantity

data = {
    "cracker": {
        "energy": 20,
        "cost": 3.5
    }
}

info = {
    "class": {
        "cost": 60, #80
        "exp": 100 #100
    },
    "tasks": {
        "cost": 40,
        "exp": 25
    }
}

resTasks = {
    0: {
        "pass": 15,
        "fail": 0
    },
    1: {
        "pass": 5,
        "fail": 0
    },
    2: {
        "pass": 10,
        "fail": -5
    },
    3: {
        "pass": 20,
        "fail": 0
    },
    4: {
        "pass": randint(30, 100),
        "fail": 0
    }
}

tasks = {
    0: "✏️ Eita! Um calouro está com problemas com o trabalho... (s/n) ",
    1: "✏️ Putz! Uma galera precisa de ajuda com a prova! (s/n) ",
    2: "🎮️ Catapimbas! O professor te chamou pro Valorant (s/n) ",
    3: "✏️ Vishh! O professor precisa de ajuda na aula de hoje (s/n) ",
    4: "✏️ Ta pegaaa! Tire os mineradores de bitcoins dos PC's da E003 (s/n) ",
}