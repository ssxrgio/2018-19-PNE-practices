def count_seq(seq):
    """Counting the number of As in the sequence."""

    result_a = 0 # Counter for the As.
    result_g = 0
    result_c = 0
    result_t = 0

    for e in seq:
        if e == 'A':
            result_a += 1
        if e == 'G':
            result_g += 1
        if e == 'C':
            result_c += 1
        if e == 'T':
            result_t += 1

    return result_a, result_g, result_c, result_t # Return the result.

# Main program

s = input("Type a valid sequence: ")
na = count_seq(s)[0]
ng = count_seq(s)[1]
nc = count_seq(s)[2]
nt = count_seq(s)[3]

print("The Number of As is {}".format(na))
print("The Number of Gs is {}".format(ng))
print("The Number of Cs is {}".format(nc))
print("The Number of Ts is {}".format(nt))


# Calculate the total sequence length.
tl = len(s)

if tl <= 0:
    perc = 0

else:
    perc_a = round((100.0 * na) / tl, 1)
    perc_g = round((100.0 * ng) / tl, 1)
    perc_c = round((100.0 * nc) / tl, 1)
    perc_t = round((100.0 * nt) / tl, 1)

print("The total lenght is {}".format(tl))
print("The percentage of As is {}%".format(perc_a))
print("The percentage of Gs is {}%".format(perc_g))
print("The percentage of Cs is {}%".format(perc_c))
print("The percentage of Ts is {}%".format(perc_t))