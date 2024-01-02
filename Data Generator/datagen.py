import random
import csv

# Get user input for column names
num_of_columns = int(input("Enter the number of columns"))
column_names = []
for i in range(num_of_columns):
    user_input = input(f"Enter column name for column {i+1}: ")
    column_names.append(user_input)

# Generate random values for an 8x8 grid
grid = [[random.randint(0, 999999) for _ in range(8)] for _ in range(8)]

# Print the column names
for name in column_names:
    print(name.ljust(8), end="")
print()

# Print the grid with column names
for row in grid:
    for value in row:
        print(str(value).zfill(6), end=" ")
    print()

# Get user input for the column name to analyze
point_to_analyze = input("Enter the data point you would like to analyze: ")

# Search for the value in the specified column
positions = []
column_index = column_names.index(point_to_analyze)
for i in range(8):
    if grid[i][column_index] == point_to_analyze:
        positions.append((i, column_index))

# Print the positions of the value
if positions:
    print(f"The value {point_to_analyze} is found at the following positions:")
    for position in positions:
        print(f"Row: {position[0]}, Column: {position[1]}")
else:
    print(f"The value {point_to_analyze} is not found in the specified column.")

# Save the grid to a CSV file
csv_filename = "grid_data.csv"
with open(csv_filename, "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(column_names)
    writer.writerows(grid)

print(f"The grid data has been saved to '{csv_filename}'.")
