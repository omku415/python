#for the next line
str1= "Hey\nGood Night" 
# for the tab sequence
str2= "Hey\t Good Night"

print(str1)
print(str2)

#concatination
str3="om"
str4="kumar"

print(str3+str4)

#length

print(len(str1))

#slicing
print(str4[1:3])# ending index is not included

print(str4[0:])# if we  miss the last index it means to end
print(str4[:4])# if we  miss the starting index it means from 0.

# in pyton there is also a feature of negative indexing 
# it will start from end with -1 then -2 etc
print(str4[-3:-1])