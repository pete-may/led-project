with open('lib', 'r') as lib:
    line = lib.readline()
    lookup = {}
    print('{', end='')
    while line:
        letter = line.split('=')[0]
        seq = line.split('=')[1]
        print("\"{}\": [".format(letter), end='')
        # print(seq, end='')

        if(letter == 's'):
            line = lib.readline()
            continue

        for x in range(7):
            print('"', end='')
            for y in range(5):
                print(seq[(7*(y+1)-1)-x], end='')
            print('", ', end='')

        print('],\n', end='')
        line = lib.readline()
    print('}\n', end='')
