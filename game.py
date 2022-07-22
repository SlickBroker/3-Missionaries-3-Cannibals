from IPython.display import clear_output

# Setup the inital game conditions and display your game board in the below format
boat_side="Right"
missionaries_on_right=3
cannibals_on_right=3
missionaries_on_left=0
cannibals_on_left=0

print('\U0001f482'*missionaries_on_left + '\U0001f479'*cannibals_on_left + " | " + '\U0001f30a'*2 + '\U0001f6A2' + '\U0001f30a'*2 + " | " + '\U0001f482'*missionaries_on_right + '\U0001f479'*cannibals_on_right)

i=0
while(i==0) :
  if boat_side=="Right" :
    print("boat is on right side")
    # boat_side == "Right":

    missionaries=int(input('Enter number of missionaries on boat '))
    cannibals=int(input('Enter number of cannibals on boat '))

    # Check the maximum number of people permitted to travel on the boat.
    if missionaries+cannibals<0 or missionaries+cannibals>2 :
      print("Invalid move 1") 
      continue

    # Now check if the number of missionaries or cannibals entered on the boat are more than the available missionaries and cannibals on the  right side
    if missionaries>missionaries_on_right or cannibals>cannibals_on_right :
      print ("Invalid move 2")
      continue

    # When the boat travels from the right side, missionaries and cannibals reduce from the right side and increase on the left side.  
    missionaries_on_right = missionaries_on_right-missionaries
    cannibals_on_right = cannibals_on_right-cannibals
    missionaries_on_left = missionaries_on_left+missionaries
    cannibals_on_left = cannibals_on_left+cannibals

    clear_output()
    print('\U0001f482'*missionaries_on_left + '\U0001f479'*cannibals_on_left + " | " + '\U0001f30a'*2 + '\U0001f6A2' + '\U0001f30a'*2 + " | " + '\U0001f482'*missionaries_on_right + '\U0001f479'*cannibals_on_right)
    boat_side= "Left"
    
  # Check the winning and losing condition
  if missionaries_on_right>0 and missionaries_on_right<cannibals_on_right :
    print("YOU LOSE")
    break
  elif missionaries_on_left>0 and missionaries_on_left<cannibals_on_left :
    print("YOU LOSE") 
    break

  if missionaries_on_left==3 and cannibals_on_left==3 :
    print("YOU WIN")
    break

  # boat_side == "Left":
  if boat_side=="Left" :
    print("boat is on left side")
    missionaries=int(input('Enter number of missionaries on boat '))
    cannibals=int(input('Enter number of cannibals on boat '))

    # Check the maximum number of people permitted to travel on the boat.
    if missionaries+cannibals<0 or missionaries+cannibals>2 :
      print("Invalid move 1") 
      continue

    # Now check if the number of missionaries or cannibals entered on the boat are more than the available missionaries and cannibals on the left side.
    if missionaries>missionaries_on_left or cannibals>cannibals_on_left :
      print ("Invalid move 2")
      continue

    # When the boat travels from the left side, missionaries and cannibals reduce from the left side and increase on the right side. 
    missionaries_on_right = missionaries_on_right+missionaries
    cannibals_on_right = cannibals_on_right+cannibals
    missionaries_on_left = missionaries_on_left-missionaries
    cannibals_on_left = cannibals_on_left-cannibals

    clear_output()
    print('\U0001f482'*missionaries_on_left + '\U0001f479'*cannibals_on_left + " | " + '\U0001f30a'*2 + '\U0001f6A2' + '\U0001f30a'*2 + " | " + '\U0001f482'*missionaries_on_right + '\U0001f479'*cannibals_on_right)
    boat_side= "Right"
  
  # Check the winning and losing condition
  if missionaries_on_right>0 and missionaries_on_right<cannibals_on_right :
    print("YOU LOSE")
    break
  elif missionaries_on_left>0 and missionaries_on_left<cannibals_on_left :
    print("YOU LOSE") 
    break

  if missionaries_on_left==3 and cannibals_on_left==3 :
    print("YOU WIN")
    break
  
print("GAME OVER")
