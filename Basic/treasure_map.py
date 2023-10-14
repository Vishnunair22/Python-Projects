row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]

position = input("Enter the position where you would like to place the treasure?\n")
horizontal = int(position[0])
vertical = int(position[1])

# Check if the input is within valid range.
if 1 <= horizontal <= 3 and 1 <= vertical <= 3:
    # Get the selected row as a list, not a string.
    selected_row = map[vertical - 1]

    # Place the treasure on the selected row.
    selected_row[horizontal - 1] = "X"

    # Print the map.
    for row in map:
        print(" ".join(row))
else:
    print("Invalid input. Please enter a position within the range 11 to 33.")
