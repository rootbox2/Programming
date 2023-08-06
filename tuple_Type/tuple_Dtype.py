# Creat tuple 
name = ("Rafi", "Avro", "Labib", "Hasibul", "Rayhan", "Redwan")

# Print type 
print(type(name))



# Print item by index 
print(name[0])
print(name[1])
print(name[2])



# Add data in tuple by converting 
C = list(name)              #Convert tuple to list

print(type(C))
print(C)

C.append("Raiyan")          #Add Data
print(C)

name = tuple(C)             #Convert to tuple

print(type(name))
print(name)



# Unpack tuple 
(a, b, c, d, e, f, g) = name

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)

# One variable full tuple 
(*x, y) = name
print(x)
print(y)