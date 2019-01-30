dna = open('CPLX2.txt', 'r')

for line in dna:
    line = line.rstrip('\n')
    print(line)

dna.close()