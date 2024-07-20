# Sets are used to store multiple items in a single variable.
# A set is a collection which is unordered, unchangeable, and unindexed.

# To create a set
thisset = {"apple", "banana", "cherry"}
print(thisset)

# also does not allow duplicate values
# To get the number of items
print(len(thisset))

# Because you can't index a specific number
# you have to loop through the set instead

for x in thisset:
  print(x)

# check for a specific item by using the "in" keyword
print("banana" in thisset)

# Add items using add method

thisset.add("orange")

# Add one iterable object (tuples, lists, dictionaries etc.) to another 
tropical = {"pineapple", "mango", "papaya"} # set 2

thisset.update(tropical) # set1 + set2

# Remove items using remove method

thisset.remove("banana")

# The union() method returns a new set with all items from both sets.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2) # you can also use "|" instead of the union word Eg set1 | set2
print(set3)

