# formater for print statements
formatter = "{} {} {} {}"

# ways to test the formatter test block
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem", 
    "or a song about fear"
))
print(formatter.format(
    "Time...",
    "is the",
    "fire...", 
    "in which we burn"
))

# notes: made a mistake, i.e. 1 T instead of 2 Ts
# date type doesn't seem to matter which is cool
