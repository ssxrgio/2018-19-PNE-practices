def count_a(seq):
    """Counting the number of As in the sequence."""

    result = 0 # Counter for the As.

    for e in seq:
        if e == 'A':
            result += 1

    return result # Return the result.

# Main program

s = input("Type a valid sequence: ")
na = count_a(s)

print("The Number of As is {}".format(na))

# Calculate the total sequence length.
tl = len(s)

if tl <= 0:
    perc = 0

else:
    perc = round((100.0 * na) / tl, 1)

print("The total lenght is {}".format(tl))
print("The percentage of As is {}%".format(perc))