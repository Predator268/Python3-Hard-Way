# Declaring the number of types of people and creating a string variable.
types_of_people = 10
x = f"There are {types_of_people} types of people."

# Declaring variables
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

# Printing
print(x)
print(y)

# Printing strings inside strings.
print(f"I said: {x}")
print(f"I also said: '{y}'")

# Declaring variables.
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

# Printing a formatted string.
print(joke_evaluation.format(hilarious))

# Declaring variables.
w = "This is the left side of..."
e = "a string with a right side."

# Printing.
print(w + e)