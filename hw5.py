def read_single_digit(n) :
    if n == 0 :
        return '영 '
    elif n == 1 :
        return '일 '
    elif n == 2 :
        return '이 '
    elif n == 3 :
        return '삼 '
    elif n == 4 :
        return '사 '
    elif n == 5 :
        return '오 '
    elif n == 6 :
        return '육 '
    elif n == 7 :
        return '칠 '
    elif n == 8 :
        return '팔 '
    elif n == 9 :
        return '구 '
    else :
        return ''
def read_number(n) :
    one = n // 100
    one1 = n % 100
    two = one1 // 10
    two1 = one1 % 10
    three = two1 // 1
    if one == 0 :
        a = read_single_digit(-1)
        if two == 0 :
            b = read_single_digit(-1)
        else :
            b = read_single_digit(two)
    else :
        a = read_single_digit(one)
        b = read_single_digit(two)
    c = read_single_digit(three)
    return f'{a}{b}{c}'

n = int(input('세 자리 정수 입력 : '))
print(read_number(n))
