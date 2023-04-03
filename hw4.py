def draw_line_string(name) :
    msg1 = 'Hello ' + name + ','
    msg2 = 'Welcome to Seoul.'
    nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)
    print('-'*nstr)
    print(msg1)
    print(msg2)
    print('-'*nstr)
name = input('Input his/her name: ')
draw_line_string(name)
