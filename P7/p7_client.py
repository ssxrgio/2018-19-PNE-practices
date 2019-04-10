from Seq import Seq
import http.client
import json
import termcolor
import collections


PORT = 80
SERVER = 'rest.ensembl.org'

print("\nConnecting to server: {}:{}\n".format(SERVER, PORT))

# Connect with the server
conn = http.client.HTTPConnection(SERVER, PORT)

conn.request("GET", "/sequence/id/ENSG00000165879?content-type=application/json")

r1 = conn.getresponse()

print("Response: {} {}\n".format(r1.status, r1.reason))

data = r1.read().decode("utf-8")

sequence = json.loads(data)
termcolor.cprint("Sequence: {}".format(sequence['seq']), "cyan")
gene = Seq(sequence["seq"])
lenght = gene.len()

print("The length of the sequence is {}.".format(lenght))

countT = gene.strbases.count('T')

print("There are {} Thymine bases the sequence.".format(countT))

frequency = collections.Counter(gene.strbases).most_common(1)[0]

print("The most popular character we find is {} which appears in {}.".format(frequency[0], Seq.perc(gene, frequency[0])))

perca = Seq.perc(gene, 'A')
percc = Seq.perc(gene, 'C')
percg = Seq.perc(gene, 'G')
perct = Seq.perc(gene, 'T')

print("The total percentages of the bases are: ")
print("     A : {}.".format(perca))
print("     T : {}.".format(perct))
print("     C : {}.".format(percc))
print("     G : {}.".format(percg))


print("CONTENT: ")
