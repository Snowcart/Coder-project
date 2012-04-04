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
        if letter==('~'):
            encoder=False
            decoder=True
            print ('switched to decoder')
    print (encode)
while decoder==True:
    newword=str(input('Put in a input'))
    for letter in newword:
        encode=('')
        if letter==(' '):
            encode=str(encode)+(' ')
        if letter==('70'):
            print('works')
            encode=str(encode)+('a')
            print('works2')
        if letter==('80'):
            encode=str(encode)+('b')
        if letter==('90'):
            encode=str(encode)+('c')
        if letter==('40'):
            encode=str(encode)+('d')
        if letter==('50'):
            encode=str(encode)+('e')
        if letter==('60'):
            encode=str(encode)+('f')
        if letter==('10'):
            encode=str(encode)+('g')
        if letter==('20'):
            encode=str(encode)+('h')
        if letter==('30'):
            encode=str(encode)+('i')
        if letter==('770'):
            encode=str(encode)+('j')
        if letter==('880'):
            encode=str(encode)+('k')
        if letter==('990'):
            encode=str(encode)+('l')
        if letter==('440'):
            encode=str(encode)+('m')
        if letter==('550'):
            encode=str(encode)+('n')
        if letter==('660'):
            encode=str(encode)+('o')
        if letter==('110'):
            encode=str(encode)+('p')
        if letter==('220'):
            encode=str(encode)+('q')
        if letter==('330'):
            encode=str(encode)+('r')
        if letter==('7770'):
            encode=str(encode)+('s')
        if letter==('8880'):
            encode=str(encode)+('t')
        if letter==('9990'):
            encode=str(encode)+('u')
        if letter==('4440'):
            encode=str(encode)+('v')
        if letter==('5550'):
            encode=str(encode)+('w')
        if letter==('6660'):
            encode=str(encode)+('x')
        if letter==('1110'):
            encode=str(encode)+('y')
        if letter==('2220'):
            encode=str(encode)+('z')
        if letter==('~'):
            encoder=True
            decoder=False
            print ('Switched to encoder')
    print (encode)

