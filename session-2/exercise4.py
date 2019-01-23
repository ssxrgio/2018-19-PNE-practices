seq = input('Type a valid DNA sequence: ').upper()
base_list = ['A', 'T', 'C', 'G']

a = 0
c = 0
t = 0
g = 0

for i in seq:
    if i == 'A':
        a += 1

    if i == 'G':
        g += 1

    if i == 'T':
        t += 1

    if i == 'C':
        c += 1

print('\nTotal lenght:', len(seq))
print('\nA:', a)
print('C:', c)
print('T:', t)
print('G:', g)


