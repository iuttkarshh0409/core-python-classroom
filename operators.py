#arithmetic operators (are used to perform arithmetic operations with the numeric data type)
a=7
b=3
'''
print(a+b) #addition
print(a-b) #subtraction
print(a*b) #multiplication
print(a/b) #division (quotient)
print(a//b) #floor-division
print(a%b)  #modulus (remainder)
print(a**b) #exponential
'''

#assignment operators (are used to assign value to the variables)
'''
a+=3 #addition
print(a)

b-=3 #subtraction
print(b)

a*=7 #multiplication
print(a)

b/=3 #division
print(b)

a%=2 #modulus
print(a)

b**=2 #exponential
print(b)
'''

#comparison operator (compares values of operator(s) and return result in boolean
'''
print(a==b)
print(a!=b)
print(a>b)
print(a>=b)
print(a<b)
print(a<=b)
'''

#logical operators (are used to perform logical operations)
c=7
d=3
'''
print((c>d)and(c==d))
print((d>c)or(d<c))
'''

#special operator (checks identity (is, is not) and membership (in, not in) and returns a boolean result)
e=3
list_e=[0,1,3,5]
f=7
'''
print(d is e)
print(c is e)

print(7 in list_e)
print(1 not in list_e)
print(0 in list_e)
'''

#bit-wise operators (work by converting numbers to their binary (base-2) representation and then performing operations on them bit by bit)

print(3&4)
print(3|4)
print(3^4)
print(5>>6)
print(1>>7)

#conditional operators (executes statements after evaluating condition(s)
marks=int(input("Enter your marks (out of 100): "))
#simple if block
if marks > 95:
       pass
if marks >= 90: print("Grade: O")
if marks >= 80: print("Grade: A+")
if marks >= 70: print("Grade: A")
if marks >= 60: print("Grade: B+")
if marks >= 50: print("Grade: B")
if marks >= 40: print("Grade: C")
if marks >= 35: print("Grade: P")
if 0 < marks < 35: print("Grade: F")

#simple if-else block
if marks >=35:
    print("Congratulations! You passed your exam.")
elif 50 < marks < 70:
    print("Good Attempt! Your performance is satisfactory.")
else:
    print("Sorry, you failed your exam!")
