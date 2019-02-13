import socket
from Seq import seq

port = 8081
IP = '212.128.253.96'

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Socket created successfully.\n')
    s.connect((IP, port))

    sequence = input('Type a valid DNA sequence: ').upper()

    if sequence == 'EXIT':
        False

    else:
        sequence = seq(sequence)
        seq_rev = seq(sequence.reverse())
        seq_comp = seq_rev.complement()
        s.send(str.encode(('Reverse-complementary sequence: {}'.format(seq_comp))))

        s.close()