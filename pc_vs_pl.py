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
    add_cards = []
    if len(c)>0:
        add_cards = random.sample(c,n)
    else:
        print('Карты в колоде закончились')
    return add_cards

def reduce_card_list(list1,list2):
    for el in list2:
        list1.remove(el)
    return list1

# Первым ходит тот у кого в наличии козыри с минимальным весом
def perviy_hod(pc_list,pl_list):
    list_koz_pc = [100]
    list_koz_pl = [100]
    hod = False
    for i in range(len(pc_list)):
        if int(pc_list[i][2]) >= 10:
            list_koz_pc.append(pc_list[i][2])
    for i in range(len(pl_list)):
        if int(pl_list[i][2]) >= 10:
            list_koz_pl.append(pl_list[i][2])
    if min(list_koz_pc) < min(list_koz_pl):
        hod = True
        print('Первым ходит компьютер: у него самая слабая козырная карта')
    else:
        hod = False
        print('Первым ходит игрок: у него самая слабая козырная карта')
    return hod

# Показывает карты 'list' игрока 'x'
def show_cards(list):
    print('Игрок в вашем распоряжении следующие карты:')
    for i in range(len(list)):
        print (i+1,'-',list[i][0],list[i][1])

# Показывает карту , поставленную на кон
def pl_kon(pl_cards):
    print('Игрок, введите номер карты на кон:')
    card_index = int(input())
    card = pl_cards[card_index-1]
    print('На кон поставлена карта (',card[0],card[1],')')
    return card

# Выбор компьютером карты на кон - случайный выбор
def pc_kon(pc_cards):
    card = random.choice(pc_cards)
    print('На кон компьютером поставлена карта (',card[0],card[1],')')
    return card

# Логика компьютера выбора карты, чтобы бить карту игрока. Выбираем минимальную по весу с той же мастью или козырной мастью
def pc_kon_check(koziry,card1,pc_list):
    pc_kon_list = []
    card2 = []
    for i in range(len(pc_list)):
        if pc_list[i][0] == card1[0] or pc_list[i][0] == koziry:
            if pc_list[i][2] > card1[2]:
                pc_kon_list.append(pc_list[i])
    if len(pc_kon_list) != 0:
        card2 = pc_kon_list[0]
        for i in range(len(pc_kon_list)):
            if pc_kon_list[i][2] < card2[2]:
                card2 = pc_kon_list[i]
        print('Карта (',card1[0],card1[1],') бита картой (',card2[0],card2[1],')')
    else:
        card2 = False
        print('Компьютеру нечем бить вашу карту, он ее забирает')
    return card2

# Проверяет, может ли карта игрока  'card2' побить карту компьютера 'card1'
def pl_kon_check(kozyri,card1,card2):
    if card2[0] == card1[0] or card2[0] == kozyri:
        if card2[2] > card1[2]:
            check = True
            print('Карта (',card1[0],card1[1],') бита картой (',card2[0],card2[1],')')
        else:
            check = False
            print(card1[1],' не може быть побита картой ',card2[1], sep='')
    else:
        check = False
        print(card1[0],' не може быть побита картой ',card2[0], sep='')
    return check

pc_cards = razdacha(cards,6)
cards = reduce_card_list(cards,pc_cards)
pl_cards = razdacha(cards,6)
cards = reduce_card_list(cards,pl_cards)
# show_cards(pc_cards)
show_cards(pl_cards)
hod = perviy_hod(pc_cards,pl_cards)


# Прописана логика принятия решения об изменении списка карт игроков и колоды карт и кто из игроков ходит следующим

while len(pc_cards) > 0 and len(pl_cards) > 0 : #Программа до конца не доделана
    if hod == True:
        card1 = pc_kon(pc_cards)
        check = False
        while check == False: #Зациклено принятия решения: игрок либо бьет карту либо забирает ее
            take_or_bit = input('Игрок, бить карту компьютера да/нет: ')
            if take_or_bit == 'да':
                card2 = pl_kon(pl_cards)
                check = pl_kon_check(kozyri,card1,card2)
                if check == True:
                    pc_cards.remove(card1)
                    pl_cards.remove(card2)
                    if len(pc_cards)<6: #Проверка перед раздачей еще одной карты, что на руках меньше 6 карт
                        add_card = razdacha(cards,1)
                        if len(add_card) != 0:
                            cards.remove(add_card[0])
                            pc_cards.append(add_card[0])
                    if len(pl_cards)<6: #Проверка перед раздачей еще одной карты, что на руках меньше 6 карт
                        add_card = razdacha(cards,1)
                        if len(add_card) != 0:
                            cards.remove(add_card[0])
                            print('Игроку роздана карта (',add_card[0][0],add_card[0][1],')')
                            pl_cards.append(add_card[0])
                    hod = False
            elif take_or_bit == 'нет':
                check = True
                pl_cards.append(card1)
                print('Вы забрали карту себе.')
                pc_cards.remove(card1)
                if len(pc_cards)<6: #Проверка6 перед раздачей еще одной карты, что на руках меньше 6 карт
                    add_card = razdacha(cards,1)
                    if len(add_card) != 0:
                        cards.remove(add_card[0])
                        pc_cards.append(add_card[0])
                hod = True
    else:
        card1 = pl_kon(pl_cards)
        card2 = pc_kon_check(kozyri,card1,pc_cards)
        if card2 == False:
            pc_cards.append(card1)
            pl_cards.remove(card1)
            if len(pl_cards)<6: #Проверка перед раздачей еще одной карты, что на руках меньше 6 карт
                add_card = razdacha(cards,1)
                if len(add_card) != 0:
                    pl_cards.append(add_card[0])
                    print('Игроку роздана карта (',add_card[0][0],add_card[0][1],')')
                    cards.remove(add_card[0])
            hod = False
        else:
            pl_cards.remove(card1)
            pc_cards.remove(card2)
            if len(pc_cards)<6: #Проверка перед раздачей еще одной карты, что на руках меньше 6 карт
                add_card = razdacha(cards,1)
                if len(add_card) != 0:
                    pc_cards.append(add_card[0])
                    cards.remove(add_card[0])
            if len(pl_cards)<6: #Проверка перед раздачей еще одной карты, что на руках меньше 6 карт
                add_card = razdacha(cards,1)
                if len(add_card) != 0:
                    pl_cards.append(add_card[0])
                    print('Игроку роздана карта (',add_card[0][0],add_card[0][1],')')
                    cards.remove(add_card[0])
            hod = True
    if len(pc_cards) == 0:
        print('Компьютер победил')
        break
    if len(pl_cards) == 0:
        print('Игрок победил')
        break
    show_cards(pl_cards)

