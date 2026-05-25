#if file is not in the same folder we have to give complete path
f = open(r"C:\Users\omku4\OneDrive\Python\fileOP\demo.txt","r")

# we can also pass the no of character to be read
data= f.read(5)
print(data)

data = f.read()
print(data)

# we can also read it line by line

line=f.readline()
print(line)

print(type(data))

f.close()


#there is another way of writing this using WITH syntax
# if we are using with no need of closing the with will automatically close it.
with open ("demo.txt","w") as f:
    data= f.read()
    print(data)