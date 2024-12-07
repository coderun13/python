#Python is used to perform different operations on a file.(Read and write data)
#Types of files
# Text files: .txt, .docx , .log etc.
# Binary files: .mp4, .mov, .png, .jpeg etc

# Open, read and close File
# We have to open a file before reading or writing.
# f = open("file_name", "mode")
# r: mode to read
# w: to write(overwrite)
# x: create a new file and open it for writing
# a: open for writing, appending to the end of the file if it exists
# b: binary file mode
# t: text mode
# +: open a disk file for uploading(read and write)
# r+: ptr start , read + overwrite (no truncate)
# w+: read + overwrite(truncate)
# a+: read + append(no truncate)

# readline(): read line by line

# Writing to a file
# f= open("file_name","mode") 


f = open("file.txt", "r")
data = f.read(5) #here 5 means only 5 letters from start
print(data)
print(type(data))

line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

f.close()


f = open("file.txt","a")
f.write("\nnice to see you here")
f.close


#with syntax

with open("file.txt","r") as f:
    data = f.read(12)
    print(data)


# Deleting a file
# using the os module
# os.remove(file_name) 
