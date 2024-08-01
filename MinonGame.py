def minion_game(s):
    stuart = 0
    kevin = 0
    length = len(s)
    vowels = 'AEIOU'
    
    for i in range(length):
        if s[i] in vowels:
            kevin += length - i
        else:
            stuart += length - i

    if stuart > kevin:
        print(f'Stuart {stuart}')
    elif stuart < kevin:
        print(f'Kevin {kevin}')
    else:
        print('Draw')
