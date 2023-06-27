# ----------------------------------------------------------------------- #
# --------------------- ** String Methods **  --------------------------- #


# 1 - len()

address = "India"
len(address)
print(address,","" Length of address", len(address))

# 2 - [] bracket Notation 
print(address[4])
print(address[::-1])
print(address[::])
print(address[0:-1])


# String concatenation 

country = "USA"
city = "NYC"
full_address = city +  ", " + country
print(full_address)

# Upper case and Lower case 

print(address.upper())
print(address.lower())

# Uppper and lower case 
print(full_address.lower())
print(full_address.upper())

# Title 
print(full_address.title())

job = "         programmer          "
print(job)
print(job.strip())

print(job.rstrip())
print(job.lstrip())

# Find the index of the letter in the string 

print(address.find("a"))
print(full_address.find("U"))


# Replace characters 
print(full_address.replace("N", "Z"))
print(full_address.replace("U", "X"))


# In operator 
print("X" in full_address)

# Equal or != operator 

print("ne" not in address)

# formatted sings

full_address1 = f"{country}, {city}"
print(full_address1)