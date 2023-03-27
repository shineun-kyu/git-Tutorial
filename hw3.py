def get_fixed_price(t,a,b) :
    print(b,'상품의 정가는 ',a / (1 - t / 100),'원')
percent = int(input('할인율은? :'))         
a = int(input('A 상품의 할인된 가격은은? :'))
b = int(input('B 상품의 할인된 가격은은? :'))
get_fixed_price(percent,a,'A')
get_fixed_price(percent,b,'B')
