# ------------------------------------------------------
#        Name: Caroline Ricketts
# ------------------------------------------------------

# Task 1.1:
#  Complete the function "read_two_ints" below:
def read_two_ints():
    """Takes in two integers and returns them as a and b. """
    # ADD a Docstring for this function
    # the return shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below
    # Getting integer inputs, assigning and returning variables
    a = int(input("give me x: "))
    b = int(input("give me y: "))
    return a,b

# Task 2.1:
#  Complete the function "compute_multadd" below:
def compute_multadd(a, b):
    """Multiplies and sums a and b, prints those results, then returns their product divided by their sum as ab_multadd."""
    # the pass shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below
    # Multilpying and summing results, printing them, then returning product/sum
    mult_result = a*b
    print(f"mult result: {mult_result}")
    add_result = a+b
    print(f"add result: {add_result}")
    ab_multadd = (mult_result/add_result)
    return ab_multadd


# Task 3.1:
#  Complete the function "print_fancy" below:
def print_fancy(a, b, ab_multadd):
    """Formats and prints the results of the two previous functions: a, b, and ab_multadd."""
    # the pass shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below
    # Formatting and printing results of previous functions
    print("****************")
    print("RESULTS:")
    print(f"first number: {a}")
    print(f"second number: {b}")
    print(f"multadd result: {ab_multadd}")
    print("================")

def main ():
    """Calls the three previous functions. Stores the returned values into variables for the first two functions."""
    # Task 1.2:
    #  Add one line below to call read_two_ints (note that it returns two values)
    #  the call should provide no arguments
    #  store the returned values into two variables: x and y
  
    # Calling first function
    x, y = read_two_ints()

    # Task 2.2:
    #  Add one line below to call multadd (note that it returns one value)
    #  the call should provide the arguments x, and y you obtained above;
    #  store the returned value in a variable called xy_multadd
    
    # Calling second function and giving arguments
    xy_multadd = compute_multadd(x,y)

    # Task 3.2:
    #  Complete The line below to call print_fancy
    #  the call should provide the arguments x, y, and xy_multadd you obtained above;
    
    # Calling third function and giving arguments
    print_fancy(x,y,xy_multadd)


    # Do not modify this final print statement
    print("The End")

# Do not modify these two lines
if __name__ == "__main__":
    main()
