class seq:
    def __init__(self, strbases): # When an object is created the string will be stored inside the object.
        print("New sequence created.")

        self.strbases = strbases # Store a variable in the object.

    def len(self):
        return len(self.strbases)

class gene(seq):
    """ This class is derived form the seq class
        All the objects of this class will
        inherite the methods from seq class """

s1 = gene("AATGCTGAAA")
s2 = seq("TCATCCTT")

l1 = s1.len()
l2 = s2.len()

str1 = s1.strbases
str2 = s2.strbases

print()
print("Sequence 1: {}".format(str1))
print("  Lenght: {}".format(l1))
print("Sequence 2: {}".format(str2))
print("  Lenght: {}".format(l2))
print("\nFinished")