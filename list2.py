lucky_numbers=[12,4,8,15,16,23,42]
friends=["Kevin","'Karen","Jim","Jim","Oscar","Toby"]

#list functions
print(friends)

#to shoh how mant times a given element has been mentioned-- we will use the count function
print(friends.count("Jim"))


#extend function- allows you to take a list an append another list at the end of it
friends.extend(lucky_numbers)
print(friends)

#append function- adding individual elements into a list- at the emd of the list
friends.append("Guinevere")
print(friends)

#insert function--allows us to insert to any desired place in the list
friends.insert(1,"Kelly")
print(friends)

#removing a given element in a list
friends.remove("Jim")
print(friends)

#to get rid of the entire list-- friends.clear() -- we use the clear function

#pop function- removes the last element in the list
friends.pop()
print(friends)

#to check if a given element is on a list by use of index 

print(friends.index("Kevin"))
# print(friends.index("Rajesh"))-- will say it is not in the list


#sort function is used in sorting the list in ascending order
#reverse function is used to reverse the list in the array
#lucky_numbers.sort()
lucky_numbers.reverse()
print(lucky_numbers)


#copy function 
friends2=friends.copy()
print(friends2)


 