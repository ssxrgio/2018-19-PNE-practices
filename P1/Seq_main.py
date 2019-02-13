from Seq import seq  # Importing the file.

s1 = seq('AATCGATAGTGC') # Converting a string into type seq.
s2 = seq('AAAATCGCTGATAGCTAGATCT')
s3 = s1.reverse()
s4 = s2.complement()

seq_list = [s1, s2, s3, s4]

for i in range(len(seq_list)):
    lenght = seq_list[i].len()

    count_a = seq_list[i].count('A')
    count_g = seq_list[i].count('G')
    count_c = seq_list[i].count('C')
    count_t = seq_list[i].count('T')

    perc_a = seq_list[i].perc('A')
    perc_g = seq_list[i].perc('G')
    perc_c = seq_list[i].perc('C')
    perc_t = seq_list[i].perc('T')

    print('Sequence: {}'.format(seq_list[i].strbases))
    print('   Lenght: {}'.format(lenght))
    print('   Bases count A: {}, C: {}, T: {}, G: {}'.format(count_a, count_c, count_t, count_g))
    print('   Bases percentage: A: {}, C: {}, T: {}, G: {}'.format(perc_a, perc_c, perc_t, perc_g))




