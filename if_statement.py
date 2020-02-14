#if is a conditional statement-- its basis is based on conditions

#basic if statement
is_male=False
if is_male:
    print("You are a male")
else:
    print("You are not a male")

#complex if statement with two variables
#if you want to apply both the two variable in your conditional statement--
#we use either the (and) or (or) keyword
#we can also use --and not(variable)
is_junkie=False
is_foodie=True
if is_junkie and is_foodie:
    print("You are a junkie foodie")
elif is_junkie and not(is_foodie):
    print ("You are just normal")
elif not (is_junkie) and is_foodie:
    print ("You are just a confused being")
else:
    print("You are neither a foodie nor junkie")