with open('lib2', 'r') as lib:
    line = lib.readline()
    lookup = {}
    print('{', end='')
    while line:
        letter = line.rsplit('=',1)[0]
        seq = line.rsplit('=',1)[1]
        print("\"{}\": [".format(letter), end='')
        # print(seq, end='')

        for x in range(7):
            print('"', end='')
            for y in range(5):
                print(seq[(7*(y+1)-1)-x], end='')
            print('", ', end='')

        print('],\n', end='')
        line = lib.readline()
    print('}\n', end='')
