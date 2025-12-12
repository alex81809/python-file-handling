# Read Mode 
file_read = open('text.txt', 'r')
print("Read mode")
print(file_read.read())
file_read.close()

# Write Mode
file_write = open('text.txt', 'w')
# writing
file_write.write("Write mode")
file_write.write("doodo odoodo od od odo ")
file_write.close()

# Append Mode
file_append = open('text.txt', 'a')
# append
file_append.write("\n Append mode")
file_append.write("This is append mode")
file_append.close()
