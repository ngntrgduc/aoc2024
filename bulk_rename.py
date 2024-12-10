from pathlib import Path

directory = Path('.')
for folder in directory.iterdir():
    if folder.is_dir() and folder.name.startswith('day_') and len(folder.name) == 5:
        try:
            day_number = int(folder.name.split('_')[1])  # Extract the number
            if 1 <= day_number < 10:  # Only for single-digit days
                new_path = directory / f'day_0{day_number}'
                folder.rename(new_path)
                print(f'Renamed: {folder} -> {new_path}')
        except ValueError:
            print(f'Skipping non-numeric folder: {folder}')
