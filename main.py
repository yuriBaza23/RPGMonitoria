from people import People

isInit = True
isOn = False
m1 = any

name = input("Fala meu bom, qual teu nome? ")
while isInit:
    sex = input("Qual teu sexo? (m/f) ")
    if sex != 'm' and sex != 'f' and sex != 'M' and sex != 'F':
        print('Você precissa nos dizer alguma dessas opções...')
    else:
        m1 = People(name, sex.lower(), [])
        isInit = False
        isOn = True

while isOn:
    choice = input("Eaê, o que quer fazer hoje? (me/class) ")
    if choice == 'me':
        print(m1)
    elif choice == 'class':
        m1.makeSomething(choice)