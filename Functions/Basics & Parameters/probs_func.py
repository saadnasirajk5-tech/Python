""" 
Write a function `add_numbers(a, b)` that returns the sum. 
Then extend it to accept any number of positional arguments using `*args`."""
def add_numbers(*args):
    return sum(args)
print(add_numbers(3,2,3,2))

"""Write a function `greet(name="World")` that returns `"Hello, <name>!"`.
   Test with and without passing a name."""

def greet(name = "World"):
    return "Hello, <name>!"       
print(greet(name="ALI"))

print(greet(name="Ali"))



















