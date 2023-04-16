def display_multiplication_table(n1,n2) :
    for x in range(1,10) :
        for i in range(n1,n2 + 1) :
            print(f'{i} x {x} = {i*x:2d}',end = '   ')
        print()
display_multiplication_table(2,5)
print()
display_multiplication_table(6,9)
