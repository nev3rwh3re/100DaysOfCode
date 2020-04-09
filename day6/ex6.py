# Types of people is the variable with a value of 10
types_of_people = 10

# x is the variable - string value
x = f"There are {types_of_people} types of people"

# string values
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

# print strings
print(x)
print(y)

# print strings+
print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't this joke so funny?! {}"
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
