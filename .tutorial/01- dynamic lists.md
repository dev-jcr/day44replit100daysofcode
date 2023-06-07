# 2D Dynamic Lists

Dynamic lists are lists that we populate as we go, getting user input and adding it to the list as we go.

We're combining several techniques here. I've left detailed code comments to help. Remember, comments can be found with `# comment` in green inside the code.

## Loops, append() and break

Here's an example to get some simple user details(name, age, computer preference) and add it to a list as a full row. This list will keep taking input until the user answers 'y' to the 'exit?' question. 


Once we collect the user's input in a row, we will `append` the entire row to the list. The columns are maintained and we are keeping the structure of 2D lists. 

![](resources/day44.001.png)
##

👉 Let's try it:

```python
listOfShame = [] 
# Creates an empty list.

while True: 
  # Starts a never ending loop (until we end it)
  name = input("What is your name? ")
  age = input("What is your age? ")
  pref = input("What is your computer platform? ")
  # Get the user input.

  row = [name, age, pref] 
  # Assigns the 3 variables into a single row.

  listOfShame.append(row) 
  # Adds the contents of the row variable at the end of the list

  exit = input("Exit? y/n") 
  # Get user choice to quit, yes or no?

  if (exit.strip().lower()[0] == "y"): 
    # strip removes unwanted spaces from the input. lower()[0] makes sure the first character of the input is lower case so it can be compared to 'y'
    break # break ends a loop and jumps to the next line of code that is not part of the loop.
    
print(listOfShame) # Outputs the list. Note this is NOT part of the loop (not indented), it only runs once the loop ends.
```






### Try it out. Can you add David's Nan too?