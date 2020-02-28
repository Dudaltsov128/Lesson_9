import random

cards = []

kozyri_list = ['Черви','Треф','Бубны','Крести']
card_list = [6,7,8,9,10,'Валет','Дама','Король','Туз']
kozyri = random.choice(kozyri_list)
for i in kozyri_list:
    if i == kozyri:
        x = 10
        for el in card_list:
            cards.append([i,el,x])
            x +=1
    else:
        x = 1
        for el in card_list:
            cards.append([i,el,x])
            x +=1

print('Козыри -',kozyri)


# 'Раздаем из перечня карт 'с' 'n'-количество карт'
def razdacha(c,n):
    cards_list = []
    cards_list = random.sample(c,n)
    return cards_list

def reduce_card_list(list1,list2):
    for el in list2:
        list1.remove(el)
    return list1

# Первым ходит тот у кого в наличии козыри с минимальным весом
def perviy_hod(pl1_list,pl2_list):
    list_koz_pl1 = [100]
    list_koz_pl2 = [100]
    hod = True
    for i in range(len(pl1_list)):
        if int(pl1_list[i][2]) >= 10:
            list_koz_pl1.append(pl1_list[i][2])
    for i in range(len(pl2_list)):
        if int(pl2_list[i][2]) >= 10:
            list_koz_pl2.append(pl2_list[i][2])
    if min(list_koz_pl1) < min(list_koz_pl2):
        hod = True
        print('Первым ходит игрок №1: у него самая слабая козырная карта')
    else:
        hod = False
        print('Первым ходит игрок №2: у него самая слабая козырная карта')
    return hod

# Показывает карты 'list' игрока 'x'
def show_cards(x,list):
    print('Игрок',x,'в вашем распоряжении следующие карты:')
    for i in range(len(list)):
        print (i+1,'-',list[i][0],list[i][1])

# Показывает карты 'list' игрока 'x'
def kon(x,pl_cards):
    print('Игрок',x,' введите номер карты на кон:')
    card_index = int(input())
    card = [pl_cards[card_index-1]]
    print('На кон поставлена карта',card[0][0],card[0][1])
    return card

# Проверяет, может ли 'card2' побить 'card1'
def kon_check(card1,card2):
    if card2[0][0] == card1[0][0] or card2[0][0] == kozyri:
        if card2[0][2] > card1[0][2]:
            check = True
            print('Карта (',card1[0][0],card1[0][1],') бита картой (',card2[0][0],card2[0][1],')')
        else:
            check = False
            print(card1[0][1],' не може быть побита картой ',card2[0][1], sep='')
    else:
        check = False
        print(card1[0][0],' не може быть побита картой ',card2[0][0], sep='')
    return check

pl1_cards = razdacha(cards,6)
cards = reduce_card_list(cards,pl1_cards)
pl2_cards = razdacha(cards,6)
cards = reduce_card_list(cards,pl2_cards)
show_cards(1,pl1_cards)
show_cards(2,pl2_cards)
hod = perviy_hod(pl1_cards,pl2_cards)

# Прописана логика принятия решения об изменении списка карт игроков и колоды карт и кто из игроков ходит следующим

while len(cards) >=20: #Программа до конца не доделана
    if hod == True:
        card1 = kon(1,pl1_cards)
        check = False
        while check == False: #Зациклено принятия решения: игрок либо бьет карту либо забирает ее
            take_or_bit = input('Игрок №2, бить карту игрока №1? Да/Нет: ')
            if take_or_bit == 'Да':
                card2 = kon(2,pl2_cards)
                check = kon_check(card1,card2)
                if check == True:
                    pl1_cards.remove(card1[0])
                    pl2_cards.remove(card2[0])
                    if len(pl1_cards)<6: #Проверка перед раздачей еще одной карты, что на руках меньше 6 карт
                        add_card = razdacha(cards,1)
                        pl1_cards.append(add_card[0])
                        cards.remove(add_card[0])
                    if len(pl2_cards)<6: #Проверка перед раздачей еще одной карты, что на руках меньше 6 карт
                        add_card = razdacha(cards,1)
                        pl2_cards.append(add_card[0])
                        cards.remove(add_card[0])
                    hod = False
            elif take_or_bit == 'Нет':
                check = True
                pl2_cards.append(card1[0])
                pl1_cards.remove(card1[0])
                if len(pl1_cards)<6: #Проверка перед раздачей еще одной карты, что на руках меньше 6 карт
                    add_card = razdacha(cards,1)
                    pl1_cards.append(add_card[0])
                    cards.remove(add_card[0])
                hod = True
    else:
        card1 = kon(2,pl2_cards)
        check = False
        while check == False:
            take_or_bit = input('Игрок №1, бить карту игрока №2? Да/Нет: ')
            if take_or_bit == 'Да':
                card2 = kon(1,pl1_cards)
                check = kon_check(card1,card2)
                if check == True:
                    pl2_cards.remove(card1[0])
                    pl1_cards.remove(card2[0])
                    if len(pl2_cards)<6: #Проверка перед раздачей еще одной карты, что на руках меньше 6 карт
                        add_card = razdacha(cards,1)
                        pl2_cards.append(add_card[0])
                        cards.remove(add_card[0])
                    if len(pl1_cards)<6: #Проверка перед раздачей еще одной карты, что на руках меньше 6 карт
                        add_card = razdacha(cards,1)
                        pl1_cards.append(add_card[0])
                        cards.remove(add_card[0])
                    hod = True
            elif take_or_bit == 'Нет':
                check = True
                pl2_cards.remove(card1[0])
                pl1_cards.append(card1[0])
                if len(pl1_cards)<6: #Проверка перед раздачей еще одной карты, что на руках меньше 6 карт
                    add_card = razdacha(cards,1)
                    pl1_cards.append(add_card[0])
                    cards.remove(add_card[0])
                hod = False
    show_cards(1,pl1_cards)
    show_cards(2,pl2_cards)










