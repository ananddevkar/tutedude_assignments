file1 = open('sample.txt' 'r+')
writing_file = file1.write('This is a simple text file\nit contains multiple files' 'r+')
print(writing_file)

file1 = open('sample.txt' 'r+')
reading_file = file1.read('This is a simple text file\nit contains multiple files' 'r+')
print(reading_file)

file.close()