# Example of reading a file located in our local file system.

name = 'mynotes.txt'

# Opening the file

file = open(name, 'r')

print('File opened: {}'.format(file.name)) # Name is an attribute that stores the name of the file opened.

contents = file.read()

print('The file contents are: {}'.format(contents))

file.close()


f = open(name, 'a') # Writing an 'a' adds new things to the text. A 'w' will erase everything and replace it with the new text.
f.write('__________________________________________________________\n This line was written with the file_write.py program\n----------------------------------------------------------')
f.close()

print('The End.')