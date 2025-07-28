'''print("ENTER YOUR DETAILS TO ACCESS YOUR RESULT ->")
name= input("Enter your name: ")
semester=input("Enter your semester: ")
rollNo=input("Enter your roll Number: ")

#input() always gives ush a string, even if the user types a number.

cgpa=8.48
sgpa=7.85

print()

print("---RESULT---")
print(f"Name: {name} || Roll-number: {rollNo} || SGPA: {sgpa} || CGPA: {cgpa}")'''

'''num1=input("Enter first number: ")
num2=input("Enter second number: ")

sum12=num1+num2 

print(f"Sum: {sum12}")       #output:78 because sum12 is treated as string as hence concatentination takes place rather than sum

print()'''
'''while(True):
     try:      #try-block
         num3=int(input("Enter third number: "))
         num4=int(input("Enter fourth number: "))

         sum34=num3+num4 
                

         print(f"Sum: {sum34}")   #output:15 because input is declared as int and hence the same would be the addition
         break
     except ValueError:      #exception-block
         print("Whoops! That wasn't a valid whole number.")'''
