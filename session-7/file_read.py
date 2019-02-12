# Example of reading a file located in our local file system.

name = 'mynotes.txt'

# Opening the file

file = open(name, 'r')

print('File opened: {}'.format(file.name)) # Name is an attribute that stores the name of the file opened.

contents = file.read()

print('The file contents are: {}'.format(contents))

file.close()

