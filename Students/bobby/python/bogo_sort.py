import random

def rand_list(n): # Geverates a random list of numbers
    random_list = []
    for _ in range (n):
        random_list.append(random.randint(0, 101))
    return random_list
  
def is_sorted(numbs):
    for x in range (len(numbs)- 1): # loop for the list -1 from the length of that list
        if numbs[x] > numbs[x + 1]: # Check that each number is greater than the number to the right of it
            return False
    return True

def shuffle(some_list):
   for current_value in some_list:
      random_index = random.randint(0, len(some_list) - 1) #chooses a number between 0 and 8--let's say 4
      random_value = some_list[random_index] # finds the number at index 4--in this case, 2
      some_list[random_index] = current_value #changes the value of the number at index 4 to current value (5)
      some_list[some_list.index(current_value)] = random_value #changes the number at current index (5) to number at index 4 (2)
   return some_list
             
def bogosort(a_list):
    while is_sorted(a_list) == False: # check for the sorted list
        shuffle(a_list) # If false sends it back up to be shuffled
    return a_list
    
numbers_list = rand_list(200) # Calls rand list function for a list of 200 integers
print(f"unsorted list: {numbers_list}") # Prints the unsorted list
sorted_list = bogosort(numbers_list) # Calls the function bogosort   
print(f"sorted list: {sorted_list}") # Prints the sorted list
