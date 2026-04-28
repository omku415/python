info={
    "key":"value",
    "name":"om",
    "Age":23,
    #we can store the list also in the value
    "subject":["math","science"],
    #we can also store the tuples in the value option
    "topic":("dictionary","set")
}

print(info["Age"])

info["name"]="Ankit"

print(info["name"])

info["surname"]="Bhardwaj"

print(info["surname"])

# we can also make the null dictionary

null_dist={}

#Nested Dictionary
student={
    "name":"om",
    #here we are doing nesting 
    "subject":{
        "phy":52,
        "math":41,
    }
}
# here it is the how  to access the nested dictionary
print(student["subject"]["phy"])

#Returns all the keys
print(student.keys())

#Returns All the values
print(student.values())

#Returns pair but in the form of tuples

print(student.items())

#

print(student.get("name"))

#suppose in dictionary if value is not present then

print(student["roll"]) # this will give error if not present

print(student.get("roll")) # this will simply return none ..no error 

student.update({"college":"cucek"})