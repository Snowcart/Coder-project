encoder=False
decoder=False
use=str(input('Would you like to encode or decode'))
if use==('encode'):
    encoder=True
if use==('decode'):
    decoder=True
while encoder==True:
    word=str(input('Put in a input'))
    encode=('')
    for letter in word:
        if letter==(' '):
            encode=str(encode)+(' ')
        if letter==('a'):
            encode=str(encode)+('70')
        if letter==('b'):
            encode=str(encode)+('80')
        if letter==('c'):
            encode=str(encode)+('90')
        if letter==('d'):
            encode=str(encode)+('40')
        if letter==('e'):
            encode=str(encode)+('50')
        if letter==('f'):
            encode=str(encode)+('60')
        if letter==('g'):
            encode=str(encode)+('10')
        if letter==('h'):
            encode=str(encode)+('20')
        if letter==('i'):
            encode=str(encode)+('30')
        if letter==('j'):
            encode=str(encode)+('770')
        if letter==('k'):
            encode=str(encode)+('880')
        if letter==('l'):
            encode=str(encode)+('990')
        if letter==('m'):
            encode=str(encode)+('440')
        if letter==('n'):
            encode=str(encode)+('550')
        if letter==('o'):
            encode=str(encode)+('660')
        if letter==('p'):
            encode=str(encode)+('110')
        if letter==('q'):
            encode=str(encode)+('220')
        if letter==('r'):
            encode=str(encode)+('330')
        if letter==('s'):
            encode=str(encode)+('7770')
        if letter==('t'):
            encode=str(encode)+('8880')
        if letter==('u'):
            encode=str(encode)+('9990')
        if letter==('v'):
            encode=str(encode)+('4440')
        if letter==('w'):
            encode=str(encode)+('5550')
        if letter==('x'):
            encode=str(encode)+('6660')
        if letter==('y'):
            encode=str(encode)+('1110')
        if letter==('z'):
            encode=str(encode)+('2220')
    print (encode)
if decoder==True:
    print('Work in progress')
    
