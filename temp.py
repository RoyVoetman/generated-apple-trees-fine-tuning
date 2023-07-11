import os

folder_path = "/Users/royvoetman/Desktop/datasets_nhl/roy/labels"  # Replace with the actual path to your folder

# Get a list of all files in the folder
files = os.listdir(folder_path)

for file_name in files:
    if file_name.startswith("testing") and file_name.endswith(".txt"):
        # Extract the number from the file name
        number = file_name[7:-4]  # Assuming the number is always after "testing" and before ".png"

        # Generate the new file name
        new_file_name = f"{number}_apple_sd.txt"

        # Construct the old and new file paths
        old_path = os.path.join(folder_path, file_name)
        new_path = os.path.join(folder_path, new_file_name)

        # Rename the file
        os.rename(old_path, new_path)
