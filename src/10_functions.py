# Write a function is_even that will return true if the passed-in number is even.

def even(num):
    return int(num) % 2 == 0 

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

print("EVEN!" if even(num) else "ODD")

