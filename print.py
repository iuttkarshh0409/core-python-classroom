import keyword

'''print('Hello')
print("Hello")'''
#We are getting same output because python doesn't have a separate data type for a single character. A single character is just a string with a length of one.

#using separators
'''print("Hello","World")         #default: one char space separated
print("Hello","World",sep="")  #using sep
print("Hello"," World")        #creating an extra char space separator'''

#using end
'''print("Greetings", end="!")    #merges the next line, separated by !
print(" Captain", end="-")     ##merges the next line, separated by -
print("Yashkarsh")
#output: Greetings! Captain-Yashkarsh'''

#using both separators and end
'''print("Dear","Boss", sep="-",end="!")
print(" Please take a break", end=".")
print(" I need to Rest :(")'''

#using f-string (string formatting)
name="Yashkarsh"
age=21
profession="Java Developer"
company="Elevate Labs"

'''print("--Persoanl Details--")
details=(f"Hello! this is {name}, aged {age} working as {profession} at {company} ")
print(details)'''
#The f-string f"..." creates one single string value and can be passed to a variable

#print(keyword.kwlist)

#Escape characters
'''print("Hola World!") #Hola World!  (simple printing)
print("Hola\nWorld!") #Hola   (new line character (\n) prints the next character(s) in new line
                      #World
print("Hola\tWorld!") #Hola	World (8 characters space between strings) (tab line character (\t) separates the content by 8 characters)

print("I \'m good!")
print("I \'m \"Yashkarsh\"") #use "\" before an apostrophe to print it without errors

print("C:\\Users\\dubey\\Desktop\\Personal Vault\\Codespace\\Python") #while printing path use "\\" instead of "\"
'''