print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N

# creating vars
small = 15
medium = 20
large = 25
  
def calc_cost(sizes,pepperoni,cheese):
  final_cost  = 0 
# checking sizes
  if sizes == "S":
    final_cost += small
  elif sizes == "M":
    final_cost += medium
  elif sizes == "L":
    final_cost += large
  else:
    print("Invalid size, enter S, M or L.")

#checking for extras
  if sizes == 'S' and pepperoni == 'Y':
    final_cost += 2
  elif sizes == 'M' or sizes == 'L' and pepperoni == 'Y':
    final_cost +=3
  if cheese == 'Y':
    final_cost += 1
      
  return final_cost
  

total_cost = calc_cost(size,add_pepperoni,extra_cheese)

print (f"Your final bill is: ${total_cost}.")
