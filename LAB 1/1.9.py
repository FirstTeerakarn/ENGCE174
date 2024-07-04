#Dictionnary initialization
person = {'name': 'Alice', 'age': 30, 'city': 'New York' }

#Accessing values
print ("Name", person['name']) # Output: Alice

#Updating values
person['age'] = 31
print("Updated age:", person['age']) #Output: 31

#Iterating through keys and values
for key, value in person.items():
  print(f"{key}:{value}")
