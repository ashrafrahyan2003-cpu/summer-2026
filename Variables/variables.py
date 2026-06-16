first_name = "Bro"


# f-string is a way to format strings in Python. It allows you to embed 
# expressions inside string literals, using curly braces {}. The expressions are
#  evaluated at runtime and then formatted using the __format__ protocol.

print(first_name)
food = "pizza"
email = "bro123@gmail.com"
print(f"Hello {first_name}! You like {food}. Your email is {email}.")


#integers
age = 25
quantity = 3
num_of_students = 30
print(f"You are {age} years old.")
print(f"You have {quantity} items in your cart.")
print(f"There are {num_of_students} students in the class.")

#floats
price = 19.99
temperature = 36.5
print(f"The price of the item is ${price}.")
print(f"The current temperature is {temperature} degrees Celsius.")

#booleans
is_student = True
for_sale = False

print(f"Is the person a student? {is_student}.")

if is_student:
    print("The person is a student.")
else:   
    print("The person is not a student.")

if for_sale:
    print("That item is for sale.")
else:
    print("That item is not  for sale.")