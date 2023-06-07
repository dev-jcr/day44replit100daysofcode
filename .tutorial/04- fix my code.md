# Fix My Code

👉 Try and fix this code which is *full* of errors.

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

## My Remove Doesn't Work And There's No Error?

👉 Add a record to this code and then try to remove it. Why is the record still there?


```python

listOfShame = [] 

while True: 
  menu = input("Add or Remove?") 

  if(menu.strip().lower()[0]=="a"): 
    
    name = input("What is your name? ")
    age = input("What is your age? ")
    pref = input("What is your computer platform? ")
    
    row = [name, age, pref] 
  
    listOfShame.append(row) 
    

  else: 
    name = input("What is the name of the record to delete?") 
    
    if name in listOfShame: 
      listOfShame.remove(name) # remove the whole row if name is in it


  print(listOfShame)
```

<details> <summary> 👀 Answer </summary>

I did not use a loop to extract each row at a time and then check each item for a matching name. Therefore, the code never finds an exact match for 'name', and doesn't remove anything.

*I only included the changes to make after the 'else' statement, not the entire code.*

```python
    for row in listOfShame: # Use a loop to extract one row at a time
      
      if name in row: # Check if the name is in the extracted row.
        listOfShame.remove(row) # remove the whole row if name is in it

  print(listOfShame)
```

</details>

### Extra points if you can add a prettyPrint subroutine!