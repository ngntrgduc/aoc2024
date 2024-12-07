from pathlib import Path

# Auto update day
day = sum(1 for folder in Path('.').iterdir() 
          if folder.is_dir() and folder.name.startswith('day_')) + 1
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