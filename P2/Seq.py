class seq:
    def __init__(self, strbases):
        self.strbases = strbases

    def len(self):
        return len(self.strbases)

    def complement(self):
        comp = ''
        for e in self.strbases:
            if e == 'A':
                comp += 'T'

            elif e == 'C':
                comp += 'G'

            elif e == 'G':
                comp += 'C'

            elif e == 'T':
                comp += 'A'

        return comp

    def reverse(self):
        return self.strbases[::-1]

    def count(self, base):
        n = 0

        if base == 'A':
            n += 1

        elif base == 'G':
            n += 1

        elif base == 'T':
            n += 1

        elif base == 'C':
            n += 1

        return n

    def perc(self, base):
        (self.count(base) / self.len()) * 100