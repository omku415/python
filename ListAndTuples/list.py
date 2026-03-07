# list is python is similar to array in c++ which stores  set of value;

marks=[50,60,70]

print(marks)

#There is slight difference that in c++ array stores similar data type value but the list in python can store differnt types of data types

student=["om",23,"Bihar",8.1] # it is valid in python

print(student)

#list slicing ..list_name[starting_index:ending_index] -> ending index is not included
name2=student[1:3]
print(name2)

#list methods
list=[1,2,3]

# add element at the end of the list
list.append(4)

# sort the list
list.sort()

#sort in descending order
list.sort(reverse=True)

# reverse the list
list.reverse()

#insert the element at the particular index
#list.insert(idx,element)
list.insert(4,"om")

#find the 1 and remove that.
list.remove(1)

#removes the element at idx
list.pop(3)