file = open('sample.txt' 'r+')
writing_file = file.write('This is a simple text file\nit contains multiple files' 'r+')
print(writing_file)

file = open('sample.txt' 'r+')
reading_file = file.read('This is a simple text file\nit contains multiple files' 'r+')
print(reading_file)

file.close()