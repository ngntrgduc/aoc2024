from pathlib import Path

# Define the folder and file names
day = 
folder_name = f'day_{day}'
files = ['input.txt', 'part1.py', 'part2.py']

# Create the folder
folder_path = Path(folder_name)
folder_path.mkdir(exist_ok=True)

# Create each file inside the folder
for file_name in files:
    file_path = folder_path / file_name
    file_path.touch()  # Create the empty file

print('Created successfully')