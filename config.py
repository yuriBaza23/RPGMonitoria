from random import randint

data = {
    "cracker": {
        "energy": 20,
        "cost": 3.5
    }
}

info = {
    "monitoring": {
        "cost": 80,
        "exp": 100
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