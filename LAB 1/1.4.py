#List initialization
numbers = [1, 2, 3, 4, 5]

#Accesing elements
print("First element:", numbers[0]) #OUTPUT: 1
print("last element:", numbers[-1]) #OUTPUT: 5

#Slicing
print("Sliced elements:", numbers[2:4]) #Output:[3, 4]

#Appending and extending
numbers.append(6)
print("After append:", numbers) #Output: [1, 2, 3, 4, 5, 6]

#Removing element
numbers.remove(3)
print("After removal:", numbers) #Output: [1, 2, 4, 5, 6]
