# a function is a collection of code that performs specific functiolns

#def -- is a keyword used to create a function
#codes that goes inside a function needs to be indented
#function should be named in lower case

def say_hi():
    print("Hello user")
say_hi()# this is how we call a function


#function with parameter
def greeting(name,age):
    print("Hello "+name +" of age " +str(age))
greeting("John Doe",45)
greeting("Steve",22)
