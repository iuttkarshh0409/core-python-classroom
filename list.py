#list is ds in py stored in square braces.
cgpa=[7.6,6.6,6.8,7.43]
cgpa.append(8.17)
print("CGPA","in","float:", sep="-", end=" ")
print(cgpa)

cgpa[0]=8
cgpa[1]=7
cgpa[2]=7
cgpa[3]=7
cgpa.append(8)
print("CGPA","in","int:",sep="-", end=" ")  #this is mutation of old cgpa list
print(cgpa)

cgpa=[8.5,7.5,7.5,7.5]
print("Improvised CGPA: ",cgpa)  #this is re-assignment of old cgpa list

#we were able to update cgpa because list is mutable (change-able)