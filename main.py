import random
from lotoclass import Lotocard

allnumber = []
firstigrok = str(input("Выберите ПЕРВОГО ИГРОКА (1 - человек, 2 - компьютер) : "))
secondigrok = str(input("Выберите ВТОРОГО ИГРОКА (1 - человек, 2 - компьютер): "))
for i in range(90):
    allnumber.append(i)

if (firstigrok == '1') and (secondigrok == '2'):
    print(f'играет Человек и Компьютер')
    card_people = Lotocard()
    print('*******Карточка игрока********')
    # card_people.printcard()
    print(card_people)
    card_computer = Lotocard()
    print('*******Карточка компьютера********')
    # card_computer.printcard()
    print(card_people)
    print('__________________________________')
    print('Карточки одинаковые' if card_people == card_computer else "Карточки конечно разные")
    print('Карточки естественно РАЗНЫЕ ' if card_people != card_computer else "Карточки на удивление одинаковые")
    print('__________________________________')
    while True:
        number = random.choice(allnumber)
        allnumber.remove(number)
        print(f'Выпало число {number} и осталось {len(allnumber)} боченков')
        print(f'Компьютеру осталось вычеркнуть {card_computer.winpoint} чисел, а вам {card_people.winpoint}')
        print('*******Карточка игрока********')
        print(card_people)
        print('*******Карточка компьютера********')
        print(card_computer)
        deletenumber = input(str(f'Вычеркиваем {number} ? Y/N '))
        if (number in card_people.card) and (deletenumber.upper() == 'Y'):
            card_people.removenumberincard(number)
        elif (number in card_people.card) and (deletenumber.upper() != 'Y'):
            print("Вы не вычеркнули число из своей карты и проиграли. Сожалеем.")
            print('Компьютер выиграл!!')
            break
        elif (number not in card_people.card) and (deletenumber.upper() == 'Y'):
            print("Вы вычеркнули число которого нет в вашей карточке и проиграли. Сожалеем.")
            print('Компьютер выиграл!!')
            break
        card_computer.removenumberincard(number)
        if card_people.winpoint == 0:
            print(f'ПОБЕДА!!!! в мешке осталось {len(allnumber)} боченков')
            print('*******Карточка игрока********')
            print(card_people)
            print('*******Карточка компьютера********')
            print(card_computer)
            break
        if card_computer.winpoint == 0:
            print(f'ПОБЕДА!!!! в мешке осталось {len(allnumber)} боченков')
            print('*******Карточка компьютера********')
            print(card_computer)
            print('*******Карточка игрока********')
            print(card_people)
            break
elif (firstigrok == '2') and (secondigrok == '2'):
    print(f'играет КОМПЬЮТЕР против КОМПЬЮТЕРА')
    card_computer1 = Lotocard()
    print('*******Карточка КОМПЬЮТЕРА 1 ********')
    print(card_computer1)
    card_computer2 = Lotocard()
    print('*******Карточка КОМПЬЮТЕРА 2 ********')
    print(card_computer2)
    while True:
        number = random.choice(allnumber)
        allnumber.remove(number)
        print(f'Выпало число {number} и осталось {len(allnumber)} боченков')
        print(
            f'КОМПЬЮТЕРУ1 осталось вычеркнуть - {card_computer1.winpoint} чисел, а КОМПЬЮТЕРУ2 - {card_computer2.winpoint}')
        card_computer1.removenumberincard(number)
        card_computer2.removenumberincard(number)
        if card_computer1.winpoint == 0:
            print(f'Компьютер 1 ПОБЕДИЛ!!!! В мешке осталось {len(allnumber)} боченков')
            print('*******Карточка КОМПЬЮТЕРА 1 ********')
            print(card_computer1)
            print('*******Карточка КОМПЬЮТЕРА 2 ********')
            print(card_computer2)
            break

        if card_computer2.winpoint == 0:
            print(f'Компьютер 2 ПОБЕДИЛ!!!! В мешке осталось {len(allnumber)} боченков')
            print('*******Карточка КОМПЬЮТЕРА 2 ********')
            print(card_computer2)
            print('*******Карточка КОМПЬЮТЕРА 1 ********')
            print(card_computer1)
            break
elif (firstigrok == '1') and (secondigrok == '1'):
    print(f'ИГРАЕТ ДВА ЧЕЛОВЕКА')
    card_people1 = Lotocard()
    print('*******Карточка ПЕРВОГО ИГРОКА ********')
    print(card_people1)
    card_people2 = Lotocard()
    print('*******Карточка ВТОРОГО ИГРОКА ********')
    print(card_people2)
    while True:
        number = random.choice(allnumber)
        allnumber.remove(number)
        print(f'Выпало число {number} и осталось {len(allnumber)} боченков')
        print(
            f'ПЕРВОМУ ИГРОУ осталось вычеркнуть - {card_people1.winpoint} чисел, а ВТОРОМУ ИГРОКУ - {card_people2.winpoint}')
        print('*******Карточка ПЕРВОГО ИГРОКА ********')
        print(card_people1)
        print('*******Карточка ВТОРОГО ИГРОКА ********')
        print(card_people2)
        deletenumber1 = input(str(f'Первый игрок, вычеркиваем {number} ? Y/N '))
        if (number in card_people1.card) and (deletenumber1.upper() == 'Y'):
            card_people1.removenumberincard(number)
        elif (number in card_people1.card) and (deletenumber1.upper() != 'Y'):
            print("Вы не вычеркнули число из своей карты и проиграли. Сожалеем.")
            print("Выиграл ВТОРОЙ ИГРОК.")
            break
        elif (number not in card_people1.card) and (deletenumber1.upper() == 'Y'):
            print("Вы вычеркнули число которого нет в вашей карточке и проиграли. Сожалеем.")
            print("Выиграл ВТОРОЙ ИГРОК.")
            break
        deletenumber2 = input(str(f'Второй игрок, вычеркиваем {number} ? Y/N '))
        if (number in card_people2.card) and (deletenumber2.upper() == 'Y'):
            card_people2.removenumberincard(number)
        elif (number in card_people2.card) and (deletenumber2.upper() != 'Y'):
            print("Вы не вычеркнули число из своей карты и проиграли. Сожалеем.")
            print("Выиграл ПЕРВЫЙ ИГРОК.")
            break
        elif (number not in card_people2.card) and (deletenumber2.upper() == 'Y'):
            print("Вы вычеркнули число которого нет в вашей карточке и проиграли. Сожалеем.")
            print("Выиграл ПЕРВЫЙ ИГРОК.")
            break
        if card_people1.winpoint == 0:
            print(f'ПЕРВЫЙ ИГРОК ПОБЕДИЛ В мешке осталось {len(allnumber)} боченков')
            print('*******Карточка КОМПЬЮТЕРА 1 ********')
            print(card_people1)
            print('*******Карточка КОМПЬЮТЕРА 2 ********')
            print(card_people2)
            break

        if card_people2.winpoint == 0:
            print(f'ВТОРОЙ ИГРОК ПОБЕДИЛ!!!! В мешке осталось {len(allnumber)} боченков')
            print('*******Карточка КОМПЬЮТЕРА 2 ********')
            print(card_people2)
            print('*******Карточка КОМПЬЮТЕРА 1 ********')
            print(card_people1)
            break
