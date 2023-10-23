import random


class Lotocard:
    def __init__(self):
        seq = []
        #for i in range(90):
            #seq.append(i)
        card = []
        card1 = []
        card2 = []
        card3 = []
        number = []
        for i in range(90):
            seq.append(i)
        for i in range(5):
            random_element = random.choice(seq)
            seq.remove(random_element)
            card1.append(random_element)
        for i in range(5):
            random_element = random.choice(seq)
            seq.remove(random_element)
            card2.append(random_element)
        for i in range(5):
            random_element = random.choice(seq)
            seq.remove(random_element)
            card3.append(random_element)
        card2.sort()
        card1.sort()
        card3.sort()
        for i in range(4):
            card1.insert(random.randint(0, 9), ' ')
            card2.insert(random.randint(0, 9), ' ')
            card3.insert(random.randint(0, 9), ' ')
        self.card = card1 + card2 + card3
        #print('Карточка создана')
        #print(f'{card1}\n{card2}\n{card3}')
        #print(f'{card[0]} {card[1]} {card[2]} {card[3]} {card[4]} {card[5]} {card[6]} {card[7]} {card[8]} ')
        #print(f'{card[9]} {card[10]} {card[11]} {card[12]} {card[13]} {card[14]} {card[15]} {card[16]} {card[17]} ')
        #print(f'{card[18]} {card[19]} {card[20]} {card[21]} {card[22]} {card[23]} {card[24]} {card[25]} {card[26]}')
        #return card
    def printcard(self):
        #print("**************************")
        print(f'{self.card[0]} {self.card[1]} {self.card[2]} {self.card[3]} {self.card[4]} {self.card[5]} {self.card[6]} {self.card[7]} {self.card[8]} ')
        print(f'{self.card[9]} {self.card[10]} {self.card[11]} {self.card[12]} {self.card[13]} {self.card[14]} {self.card[15]} {self.card[16]} {self.card[17]} ')
        print(f'{self.card[18]} {self.card[19]} {self.card[20]} {self.card[21]} {self.card[22]} {self.card[23]} {self.card[24]} {self.card[25]} {self.card[26]}')
        print("________________________________")
    # print()
    def numberincard(self, number):
        if number in self.card:
            print('OK!!!')
        else:
            print('NE OK!!!')

# if 3 in card:
# print("ok")
