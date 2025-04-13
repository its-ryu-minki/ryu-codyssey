filename = 'Mars_Base_Inventory_List.csv' # Path
danger_filename = 'Mars_Base_Inventory_danger.csv' # Danger CSV Path
binary_filename = 'Mars_Base_Inventory_List.bin' # Binary File Path (BONUS)

data = [] # List

# Read CSV
with open(filename, 'r', encoding='utf-8') as file:
    for line in file:
        row = line.strip().split(',') # Seperate by comma
        data.append(row)
        print(row) # Print CSV

print(data) # Print List

# Separation Header
header = data[0]
rows = data[1:]

# Flammability
flammability_index = -1

# Sort Descending
rows.sort(key=lambda x: float(x[flammability_index]), reverse=True)

# Filtering Flammability
danger_rows = [row for row in rows if float(row[flammability_index]) >= 0.7]

# Print Dangerous List
print("\n=== Dangerous List ===")
for row in danger_rows:
    print(row)

# Save Dangerous List as CSV
with open(danger_filename, 'w', encoding='utf-8') as file:
    file.write(','.join(header) + '\n')
    for row in danger_rows:
        file.write(','.join(row) + '\n')

print(f"\nSaved '{danger_filename}'")


# Save Dangerous List as bin (BONUS)
with open(binary_filename, 'wb') as file:
    for row in rows:
        line = ','.join(row) + '\n'
        file.write(line.encode('utf-8'))

print(f"\nSaved '{binary_filename}'")

# Read Binary File (BONUS)
loaded_rows = []
with open(binary_filename, 'rb') as file:
    lines = file.readlines()
    for line in lines:
        decoded = line.decode('utf-8').strip()
        row = decoded.split(',')
        loaded_rows.append(row)

# Print Binary File (BONUS)
print("\n=== Binary File ===")
for row in loaded_rows:
    print(row)