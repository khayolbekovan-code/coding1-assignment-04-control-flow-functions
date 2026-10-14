def add_one(value): 
    return value + 1 #add_one takes a number and returns it plus 1. Defining it does not run it.

for number in [1, 2, 3]: #The loop goes through 1, 2 and 3
    if number > 1: # but the if only lets numbers greater than 1 through
        print(add_one(number))  #1 is skipped. For 2 and 3, add_one is called and its result is printed.

# 1. What is printed, in order? Explain how the loop and the if condition
# decide which numbers are passed to add_one.
# Your answer: It prints 3 and 4.
# The loop takes 1, 2 and 3 one at a time. The if only lets a number through
# when it is greater than 1, so 1 is skipped and add_one is never called on it.
# 2 and 3 pass, so add_one(2) and add_one(3) run and their results are printed.

# 2. What does add_one(2) return? Explain the difference between return
# inside the function and print in the loop.
# Your answer:add_one(2) returns 3.
# return sends the value back to wherever the function was called, but it does
# not show anything on the screen. print in the loop is what displays that
# returned value. Without print, add_one(2) would still give back 3, but nothing
# would appear in the output.




