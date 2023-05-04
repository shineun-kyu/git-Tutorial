def buy(dic) :
    item = 'd'
    while not item == '' :
        print('[구입]')
        item = input('상품명? ')
        if item != '' :
            n = int(input('수량은? '))
            print(f'장바구니에 {item} {n}개가  담겼습니다.')
            print()
            dic[item] = n
        elif item == '' :
            print()
            return False
def show(dic) :
    print(f'>>>  장바구니 보기 :  {dic}')
    print()        
def find(dic) :
    print('[검색]')
    text = input('장바구니에서 확인하고자 하는 상품은? ')
    if text in dic :
        print(f'{text}은(는) {dic[text]}개 담겨 있습니다.')
    else :
        print(f'장바구니에 {text}은(는) 없습니다.')
shopping_bag = {}    
while True :
    if buy(shopping_bag) == False:
        break
print()
show(shopping_bag)
find(shopping_bag)
