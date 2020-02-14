print("Girrafe Academy")

#print in the next line
print("Girrafe \nAcademy")

#putting a quotation mark inside a string
print("Girrafe \"Academy\"")

#creating a string variable
phrase="Giraffe Academy"
print(phrase)
#concatenation
print(phrase + " is cool")
print(phrase.upper())#function to change it to upper case
print(phrase.lower()) #fucntion to change it to lowercase
print(phrase.isupper()) #function to check if it is in upper case
print(phrase.upper().isupper()) #will convert first to upper then confirm it's indeed true


#check the lenght of a string (len)
print(len(phrase))

#getting individual characters by specifying the index
print(phrase[12])
print(phrase[0])
 
#using the index function
print(phrase.index("G"))

#using the replace fucntion
print(phrase.replace("Giraffe","Elephant"))