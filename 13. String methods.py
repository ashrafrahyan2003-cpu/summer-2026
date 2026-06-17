name = input("Enter your full name")
phone_number = inpiut("Enter your phone number")

result = len(name)

result = name.find(" ")     #first occurance of a " "
result = name.find("B")     #first occurance of "B"
result = name.rfind("o")    #last occurance of "o"
name = name.capitalize()    #capitalizes the first letter of the string
name = name.upper()         #capitalizes all the letters
name = name.lower()         #lower case for all the letters
result = name.isdigit()     #returns true ONLY if the entire string contains digits. else false
result = name.isalpha()     #returns true ONLY if the entire string contains only alphabets
result = phone_number.count("-")
phone_number = phone_number.replace("-", " ")

print(phone_number)
print(result)

#to find out all the available string methods built-in into python, type print(help(str))
