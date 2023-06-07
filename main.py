# Bingo. Use of prettytable and dictionaries

import random, pprint, os, time
from prettytable import PrettyTable, ALL, FRAME
bingo=[]

def ran():
  num=random.randint(1,90)
  return num

def prettyPrint():
  for row in bingo:
    print(row)

nums=[]

for i in range(8):
  nums.append(ran())

nums.sort()

bingo=[[f"{nums[0]}",f"{nums[1]}",f"{nums[2]}"],[f"{nums[3]}","BINGO",f"{nums[4]}"],[f"{nums[5]}",f"{nums[6]}",f"{nums[7]}"]]

Xcounter=0
while Xcounter<8:
  p=PrettyTable()
  p.field_names=["num1","num2","num3"]
  p.padding_width=2
  p.hrules=ALL
  p.vrules=ALL
  p.add_row(bingo[0])
  p.add_row(bingo[1])
  p.add_row(bingo[2])
  print(p.get_string(header=False))
  print()
  
  t="Next Number: "
  n=input(f"{t:^20}")
  str(n)
  l=0
  k=0
  while True:
    if k==3:
      break
    if l<3:
      if bingo[k][l]==n:
        bingo[k][l]=("X")
        Xcounter+=1
        l+=1
      else:
        l+=1
    else:
      if l==3 and k==3:
        break
      else:
        l=0
        k+=1
print("\nYou won!")
time.sleep(1)
os.system("clear")

# Course solution

# import random, os, time

# bingo = []

# def ran():
#   number = random.randint(1,90)
#   return number

# def prettyPrint():
#   for row in bingo:
#     for item in row:
#       print(item, end="\t|\t")
#     print()

# def createCard():
#   global bingo
#   numbers = []
#   for i in range(8):
#     num = ran()
#     while num in numbers:
#       num = ran()
#     numbers.append(ran())
  
#   numbers.sort()
  
#   bingo = [ [ numbers[0], numbers[1], numbers[2]],
#             [ numbers[3], "BG", numbers[4] ],
#             [ numbers [5], numbers[6], numbers[7]]
#           ]

# createCard()
# while True:
#   prettyPrint()
#   num = int(input("Next Number: "))
#   for row in range(3):
#     for item in range(3):
#       if bingo[row][item] == num:
#         bingo[row][item] = "X"

#   exes = 0
#   for row in bingo:
#     for item in row:
#       if item=="X":
#         exes+=1

#   if exes == 8:
#     print("You have won")
#     break

#   time.sleep(1)
#   os.system("clear")