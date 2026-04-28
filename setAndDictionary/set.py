collection={1,2,3,"om"}

#suppose if we write the duplicate element in set it gets ignored and unique items gets printed
#even though we have written 23 and om two timmes it get counted as one.
feature={"om",23,"male","om",23}

print(feature)
# length will be also return as no of unique item

print(len(feature))

#method to create the empty set 
details= set()

#SET METHODS

#method to add element in the set
details.add("om")
details.add(23)

#method to remove element in the set .
details.remove(23)

#this method clear the set
details.clear()

#removes random value
details.pop()

#union method is used to combine and return the unique value in both set
details.union(feature)

#intersection method combines common value and return it
details.intersection(feature)