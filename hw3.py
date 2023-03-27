def get_fixed_price(t,a,b) :
    print('A 상품의 정가는 ',a / (1 - t / 100),'원')
    print('B 상품의 정가는 ',b / (1 - t / 100),'원')
percent = int(input('할인율은? :'))         
a = int(input('A 상품의 할인된 가격은은? :'))
b = int(input('B 상품의 할인된 가격은은? :'))
get_fixed_price(percent,a,b)
