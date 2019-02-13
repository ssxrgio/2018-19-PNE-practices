from Seq import seq  # Importing the file.

''' Creating the sequences '''

s1 = seq('AATCGATAGTGC') # Converting a string into type seq.
s2 = seq(input('Type a valid sequence: ').upper())
s3 = s1.reverse()
s3 = seq(s3) # Turn s3 (a string) into seq class.
s4 = s2.complement()
s4 = seq(s4) # Doing the same as with s3.

seq_list = [s1, s2, s3, s4] # Store all sequences in a list in order to loop on it and get all data only writing one print function.
a = 0 # Counter for printing the number of the sequence.

''' Printing loop '''

for i in range(len(seq_list)):
    lenght = seq_list[i].len()

    count_a = seq_list[i].count('A')         # Getting counts
    count_g = seq_list[i].count('G')
    count_c = seq_list[i].count('C')
    count_t = seq_list[i].count('T')

    perc_a = seq_list[i].perc('A')           # Getting percentages
    perc_g = seq_list[i].perc('G')
    perc_c = seq_list[i].perc('C')
    perc_t = seq_list[i].perc('T')

    a += 1

    print('\nSequence {}: {}'.format(a, seq_list[i].strbases)) # Turn seq class into str type.
    print('   Lenght: {}'.format(lenght))
    print('   Bases count A: {}, C: {}, T: {}, G: {}'.format(count_a, count_c, count_t, count_g))
    print('   Bases percentage: A: {}%, C: {}%, T: {}%, G: {}%'.format(perc_a, perc_c, perc_t, perc_g))




