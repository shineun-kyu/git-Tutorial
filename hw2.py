def get_integer() :
    total = int(input('동전으로 교환하고자 하는 금액은? '))
    return total
def exchange(t) :
    n500 = t // 500
    t %= 500
    n100 = t // 100
    t %= 100
    n50 = t // 50
    t %= 50
    n10 = t // 10
    print('500원 동전의 개수 : ',n500)
    print('100원 동전의 개수 : ',n100)
    print('50원 동전의 개수 : ',n50)
    print('10원 동전의 개수 : ',n10)
result = get_integer()
exchange(result)
