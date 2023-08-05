# list
name = ["Rafi", "Nahid", "Rabbi", "Raian", "Afroza", "Shohayef"]

# loop use in list 
for i in name:
    print(i)


# Add data using append
name.append("Shihab")
print("Append list : ",name)

# Add data using insert
name.insert(1, "Rejaul")
print("Insert list : ",name)

# Find index from item name
i = name.index("Shihab")
print(i)

# Find item from index name 
item = name[5]
print(item)

# Change item from list 
name[7] = "Rohan"
print("Change list : ",name)


# Remove item from list 
name.remove("Rabbi")
print("Remove list : ",name)



