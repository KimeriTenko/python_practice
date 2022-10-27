# 1. A function named hello() that prints a greeting to the user. 
# This function should accept no arguments and returns nothing.

def hello():
    print("Greetings")

# 2. A function named pack that accepts 3 arguments, 
# and returns a single list with the 3 arguments inside as list elements

def pack(Tomato, Lettuce, Bacon):
    return[Tomato, Lettuce, Bacon]

# 3. A function that should accept a list of any length,
# and print out a series of strings "First I eat __" (the first element of the list), 
# and "Next I eat ___" (for the following elements in the list). 
# If the list is empty, print "My lunchbox is empty!". 
# The function should not return anything.

def eat_lunch(my_lst):
  if len(my_lst) == 0:
    print("My lunchbox is empty!")
  else:
    for i in range(len(my_lst)):
      if i == 0:
        print(f"First I eat {my_lst[0]}")
      else:
        print(f"Next I eat {my_lst[i]}")

# hello()
# print(pack("a","b","c"))
# print(pack(1,2,3))
eat_lunch([])
eat_lunch(["BLT"])
eat_lunch(["bacon","lettuce","tomato","bread"])





