#there are more like Objects syntax in Javascript
#the keys should be unique-- no duplicates
monthConversions={
    "Jan":"January",
    "Feb":"Febraury",
    "Mar":"March",
    "Apr":"April",
    "May":"May",
    "Jun":"June",
    "Jul":"July",
    "Aug":"August",
    "Sep":"September",
    "Oct":"October",
    "Nov":"Novemebr",
    "Dec":"December" 

}
print(monthConversions["Nov"])

#another method of accessing a given key value is using the get function

print(monthConversions.get("Sep"))

#we can also use the get function to  pass in a default value for a key that does not exist
print(monthConversions.get("Luv","Not a valid key"))#not a valid key will be the dafault value