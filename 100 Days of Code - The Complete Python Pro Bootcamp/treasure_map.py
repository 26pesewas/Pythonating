line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")

         
letter = position[0].lower()
letters = ['a','b','c']
letter_index = letters.index(letter)

number_index = int(position[1]) - 1

map[number_index][letter_index] ='X'

print(f"{line1}\n{line2}\n{line3}")
