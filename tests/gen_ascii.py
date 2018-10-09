from ascii import ascii


base = ord(" ")

for x in range(96):
    entry = 5*x
    print(chr(base+x), end='')
    print("=", end='')
    print('{0:07b}'.format(ascii[0+entry]), end='')
    print('{0:07b}'.format(ascii[1+entry]), end='')
    print('{0:07b}'.format(ascii[2+entry]), end='')
    print('{0:07b}'.format(ascii[3+entry]), end='')
    print('{0:07b}'.format(ascii[4+entry]), end='')
    print('\n', end='')


    