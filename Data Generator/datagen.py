import random
import csv
import string

def get_user_input(message):
    return input(message)

def generate_random_data(choice):
    if choice == "integer":
        return str(random.randint(0, 999999)).zfill(6)
    elif choice == "string":
        return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

def generate_column_data(choice, size):
    return [generate_random_data(choice) for _ in range(size)]

def generate_grid(num_columns, column_names, choice):
    return {col_name: generate_column_data(choice, 8) for col_name in column_names[:num_columns]}

def print_grid(grid):
    for col_name, data in grid.items():
        print(col_name.ljust(8), end="")
    print()
    for i in range(8):
        for col_name, data in grid.items():
            print(str(data[i]).ljust(8), end="")
        print()

def find_positions(grid, column_name, point):
    positions = []
    for i, value in enumerate(grid[column_name]):
        if value == point:
            positions.append(i)
    return positions

def save_to_csv(filename, grid):
    with open(filename, "w", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=grid.keys())
        writer.writeheader()
        writer.writerows(zip(*[grid[col_name] for col_name in grid]))

    print(f"The grid data has been saved to '{filename}'.")

def main():
    num_columns = int(get_user_input("Enter the number of columns: "))
    column_names = [get_user_input(f"Enter column name for column {i+1}: ") for i in range(num_columns)]

    choice = get_user_input("Enter 'integer' or 'string' for data type: ")
    while choice not in ['integer', 'string']:
        choice = get_user_input("Invalid input. Please enter 'integer' or 'string': ")

    grid = generate_grid(num_columns, column_names, choice)

    print_grid(grid)

    point_to_analyze = get_user_input("Enter the data point you would like to analyze: ")

    positions = []
    for col_name in column_names:
        if point_to_analyze in grid[col_name]:
            col_positions = find_positions(grid, col_name, point_to_analyze)
            positions.extend([(i, col_name) for i in col_positions])

    if positions:
        print(f"The value {point_to_analyze} is found at the following positions:")
        for position in positions:
            print(f"Row: {position[0]}, Column: {position[1]}")
    else:
        print(f"The value {point_to_analyze} is not found in any column.")

    csv_filename = "grid_data.csv"
    save_to_csv(csv_filename, grid)

if __name__ == "__main__":
    main()
