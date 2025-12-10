# ask for file names
firstfile = input("Enter the name of the first file: ")
secondfile = input("Enter the name of the second file: ")

# open the second file and read its content
f2 = open(secondfile, 'r')
data = f2.read()
f2.close()

# open the first file and add the second file's content to it 
f1 = open(firstfile, 'r')
f1.write(data)
f1.close()

print("Content of", secondfile, "has been added to", firstfile)
