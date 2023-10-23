import random
from lotoclass import Lotocard

card_people = Lotocard()
print('*******Карточка игрока********')
card_people.printcard()
#print('***************')

card_computer = Lotocard()
print('*******Карточка компьютера********')
card_computer.printcard()
#print('***************')

card_computer.numberincard(10)
card_people.numberincard(10)

#card_computer = Lotocard()
#Lotocard.numberincard(10, card_computer)

# seq= []
# for i in range(90):
#     seq.append(i)
#
# card1 = []
# card2 = []
# card3 = []
# number= None
# for i in range(5):
#     random_element = random.choice(seq)
#     seq.remove(random_element)
#     card1.append(random_element)
# for i in range(5):
#     random_element = random.choice(seq)
#     seq.remove(random_element)
#     card2.append(random_element)
# for i in range(5):
#     random_element = random.choice(seq)
#     seq.remove(random_element)
#     card3.append(random_element)
# card2.sort()
# card1.sort()
# card3.sort()
# for i in range(4):
#     card1.insert(random.randint(0, 9),' ')
#     card2.insert(random.randint(0, 9), ' ')
#     card3.insert(random.randint(0, 9), ' ')
#
# #print(card1)
# #print(card2)
# #print(card3)
#
# card = card1 + card2 + card3
# #print(f'{card1}\n{card2}\n{card3}')
#
# first_row=[]
# print("**************************")
# print(f'{card[0]} {card[1]} {card[2]} {card[3]} {card[4]} {card[5]} {card[6]} {card[7]} {card[8]} ')
# print(f'{card[9]} {card[10]} {card[11]} {card[12]} {card[13]} {card[14]} {card[15]} {card[16]} {card[17]} ')
# print(f'{card[18]} {card[19]} {card[20]} {card[21]} {card[22]} {card[23]} {card[24]} {card[25]} {card[26]}')
# print("**************************")
#  #print()



#if 3 in card:
    #print("ok")