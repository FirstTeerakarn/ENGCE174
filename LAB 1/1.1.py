#List Comprehension
squares = [x**2 for x in range(10)]

#Dictionary comprehension
square_dict ={x: x**2 for x in range(5)}

#set comprehension
even_squares = {x**2 for x in range(10) if x % 2 == 0}
