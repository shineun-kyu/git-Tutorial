print('[구매]')
shopping_bag = {}
item = 'd'
while not item == '' :
    item = input('상품명? ')
    if item != '' :
        n = int(input('수량은? '))
        shopping_bag[item] = n
        print(f'장바구니에 {item} {n}개가  담겼습니다.')
    print()
print()
print('>>> 장바구니 보기 : ',shopping_bag)
print()
print('[검색]')
text = input('장바구니에서 확인하고자 하는 상품은? ')
if text in shopping_bag :
    print(f'{text}은(는) {shopping_bag[text]}개 담겨 있습니다.')
else :
    print('그런 상품은 없습니다.')
