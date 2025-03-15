import os
import tkinter as tk
from tkinter import filedialog

def count_tokens(text):
    """Estimate the number of tokens in the text."""
    return len(text.split())

def get_file_size(file_path):
    """Returns the size of the file in bytes."""
    return os.path.getsize(file_path)

def clean_text(text):
    """Performs basic cleaning of the text."""
    # Remove unwanted characters (e.g., non-printable characters)
    cleaned_text = ''.join(char for char in text if char.isprintable())

    # Convert to lowercase to standardize (optional)
    cleaned_text = cleaned_text.lower()

    # Additional cleaning steps can be added here

    return cleaned_text

# Create a Tkinter root window (hidden as we just need the file dialog)
root = tk.Tk()
root.withdraw()  # Hide the main window

# Ask the user to select a folder
directory = filedialog.askdirectory(title="Select Folder Containing .txt Files")

# Check if a directory was selected
if not directory:
    print("No folder selected. Exiting script.")
else:
    # Maximum number of tokens for each combined file
    max_tokens = 2_000_000

    # File counter for naming the output files
    file_counter = 1

    # Initialize the token count of the current combined file
    current_token_count = 0

    # List to keep track of combined file details (token count and file size)
    combined_files_info = []

    # Start with the first output file
    current_file_path = os.path.join(directory, f'combined_{file_counter}.txt')
    current_file = open(current_file_path, 'w')

    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        # Check if the file is a .txt file
        if filename.endswith('.txt'):
            file_path = os.path.join(directory, filename)

            # Open the .txt file for reading with utf-8 encoding
            with open(file_path, 'r', encoding='utf-8') as file:
                # Read, clean, and estimate the number of tokens in this file
                content = clean_text(file.read())
                file_token_count = count_tokens(content)

                # Check if adding this file would exceed the maximum token limit
                if current_token_count + file_token_count > max_tokens:
                    # Close the current file and record its details
                    current_file.close()
                    combined_files_info.append((current_token_count, get_file_size(current_file_path)))

                    # Start a new combined file
                    file_counter += 1
                    current_file_path = os.path.join(directory, f'combined_{file_counter}.txt')
                    current_file = open(current_file_path, 'w')
                    current_token_count = 0

                # Write the cleaned content to the current combined file
                current_file.write(content + "\n")
                # Update the token count of the current combined file
                current_token_count += file_token_count

    # Close the last output file and record its details
    current_file.close()
    combined_files_info.append((current_token_count, get_file_size(current_file_path)))

    # Print the details of each combined file
    for i, (tokens, size) in enumerate(combined_files_info, 1):
        print(f"Combined file {i}: {tokens} tokens, {size} bytes")

    print(f"Completed. Created {file_counter} combined file(s) in '{directory}'.")
