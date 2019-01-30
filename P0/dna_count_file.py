dna = open('dna.txt', 'r')
base_list = ['A', 'T', 'C', 'G']

a = 0
c = 0
t = 0
g = 0

for line in dna:
    for e in line:
        if e == 'A':
            a += 1

        if e == 'G':
            g += 1

        if e == 'T':
            t += 1

        if e == 'C':
            c += 1

    print('\nTotal count of bases:')
    print('\nA:', a)
    print('C:', c)
    print('T:', t)
    print('G:', g)
