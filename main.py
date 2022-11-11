from monitor import Monitor

name = input("Fala meu bom, qual teu nome? ")
subject = input("Qual matéria tu quer dar? ")
m1 = Monitor(name, [subject])

isOn = True
while isOn:
    choice = input("Eaê, o que quer fazer hoje? (me/money/class/eat/tasks) ")
    if choice == 'me':
        print(m1)
    elif choice == 'money':
        if m1.haveMoney():
            print('Uia, parece que você tem dinheiro!')
        else:
            print('Rapaiz... tu ta falido!')
    elif choice == 'class':
        m1.makeMonitoring()
    elif choice == 'tasks':
        m1.makeATask()
    elif choice == 'eat':
        m1.eatCracker()