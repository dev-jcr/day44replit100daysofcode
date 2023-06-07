# Add or Remove?

We can add records, but let's expand to give the user the choice of whether to add OR remove. Do we want to remove the entire row or just one item?


We ask the user to choose between adding and removing. If they choose remove, we:
- ask for a name on the list (make sure it is spelled correctly)
- extract each row, one at a time, from the list
- check the row to see if it contains the name
- if the name is in the row, use the `.remove()` method to remove the **whole row**, not just the name.

👉 *In the code below, I've only shown the loop that works with the list.  I've left out the `prettyPrint` subroutine so we can focus on the changes. Again, check the comments for explanations.*

```python

listOfShame = [] 

while True: 
  menu = input("Add or Remove?") # Gives the user a choice prompt and stores their input.

  if(menu.strip().lower()[0]=="a"): # Uses selection to run the 'add' code if user inputs 'a'. I've "sanitized" the input here too.
    
    name = input("What is your name? ")
    age = input("What is your age? ")
    pref = input("What is your computer platform? ")
    
    row = [name, age, pref] 
  
    listOfShame.append(row) 
    # All the 'add' code is now indented, so it's part of the 'add' branch and will only run if the user enters 'a'.

  else: # If the user doesn't choose 'a', run this new remove code instead.
    name = input("What is the name of the record to delete?") # Get the input of a name
    for row in listOfShame: # Use a loop to extract one row at a time
      
      if name in row: # Check if the name is in the extracted row.
        listOfShame.remove(row) # remove the whole row if name is in it

  prettyPrint()
```



### Get removing and see what you can do!