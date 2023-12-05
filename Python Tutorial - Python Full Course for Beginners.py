#Python NOTES
#Python is a case sensitive language: YOU NEED TO KEEP YOUR CASES THE SAME
#When defining variables: 
#your identifiers are lowercase and the value needs to be cased depending on Python's language
#Expression is a piece of acode that produces a value
#0 will always be the first index

#Lesson 1: Learning Prints and Executables
    #when printing in code, it will execute every line
print("Hello World, I am Sophia Ceballos.")
print("o------/")
print("  ||||")
    #quotations defines a string
    #a string is a series of characters
print('*' * 10)
    # when adding a multiplcation operator it will multiply the string and the number provided. 
    # when executed the string will repeat however many times the operation was given



#Lesson 2: Learning Variables
    #we use variables to temporarily store data in a computer's memory
    #when printing the variable you do not need to put it in quotations because that will turn it into a string 

    #the 10 is first converted to its binary representation then stored, which is then stored in the computer's memory until it needs to be allocated
    #price is the identifier (name of variable) = (is) 10 (value)
price = 10 

    #when you update variables it will execute the most recently inputted
price = 10
price = 20
print(price)

    #integer (int) is a umber without a decimal point
price = 20
    #float is a number with decimals
rating = 4.0 
    #strings are variables that have words
Name = 'Sophie'
    #boolean (bool) is a variable that can be either true of false
is_published = True #we use an unserscore (_) to ahve multiple words in the identifier

    #variables practice: We check in a patient names John Smith. He's 20 years old and is a new a patient.
full_name = 'John Smith'
age = 20
new_patient = True
print(full_name, age, new_patient)



#Lesosn 3: Getting Input
name = input('What is your name? ') 
    #this funciton will print this message on the terminal, then it will wait for the user to enter a value
    #once value entered, it will return
print('Hi ' + name) #adding a + to a print funct it ill combine multiple strings

    #input practice: Ask two questions: person's name and favorite color. Then, print a message like '[name] likes [color]'
name = input('What is your name? ')
color = input('What is your favorite color? ')
print(name + ' likes ' + color)



#Lesson 4: Type Conversion
    #in order to change str to int you will incldue int before your variable: int(variable)
    #when wanting to see what type of variable you are calling you will: print(type(variable))

birth_year =input('Birth year: ') 
print(type(birth_year))#print type of birth year
age = 2023 - int(birth_year) #this will five you an error: unsupported operand type for -: 'int(1999)' and 'str('1999')'
print(type(age))#print type of age
print(age)

    #type practice: Ask a user their weight (in pounds), then convert it to kilograms and print on the terminal.
user_weight = input('Weight (lbs): ')
weight = 0.45359237 * float(user_weight)
print(weight)



#Lesson 5: Strings
    #you can use either '' or "" for string
    #you will have to use specific quotations for specific things

    #course = 'Python's course for Beginners' this cannot work because the ' in the Python
course = "Python's Course for Beginners" #use "" when using ' in str
print(course)

course = 'Python for "Beginners"' #use '' when using "" in str
print(course)

    #define string w multiple lengths: use triple quotes
course = '''
Hi John,

here is our first email to you.

Thank you,
The support team.'''
print(course)

    #using [] to get a characters at a given index in the string 
course = 'Python for Beginners'
print(course[0]) #0 is the index of the first character
print(course[-1])#-1 is the index of the last character
print(course[0:3])#will show all charcters from index 0 to index 3 but exclude index 3
print(course[:5])#will print up to index 5

    #string practice: what will the code return?
name =  'Jennifer'
print(name[1:-1]) #this will print 'ennife'

    #how to show multiple strings in an argument
first = 'John'
last = 'Smith'
message = first + ' [' + last + '] is a coder' #works but not ideal
print(message)

    #formatted string
msg = f'{first} [{last}] is a coder'
print(msg)



#Lesson 6: String Methods

