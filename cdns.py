import os
import requests
import tkinter as tk
from tkinter import messagebox, scrolledtext

# Default folder paths without "assets" folder
default_js_folder = "js/plugins"
default_css_folder = "css/plugins"

# Create folders if they don't exist
os.makedirs(default_js_folder, exist_ok=True)
os.makedirs(default_css_folder, exist_ok=True)

# Download a file and save it to the specified folder
def download_file(url, folder):
    filename = url.split("/")[-1]
    filepath = os.path.join(folder, filename)
    
    if os.path.exists(filepath):
        print(f"Skipped {filename}, already exists at {filepath}")
        return None  # Return None if file already exists to skip downloading
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(filepath, "wb") as file:
            file.write(response.content)
        print(f"Downloaded {filename} to {filepath}")
        return filename
    except requests.exceptions.RequestException as e:
        print(f"Failed to download {url}: {e}")
        return None

# Process CDN links, download them, and generate local declarations
def process_cdns():
    # Get updated folder paths from entry fields
    js_folder = js_folder_entry.get()
    css_folder = css_folder_entry.get()

    # Ensure folders exist
    os.makedirs(js_folder, exist_ok=True)
    os.makedirs(css_folder, exist_ok=True)
    
    cdns = input_text.get("1.0", tk.END).strip().splitlines()
    css_declarations = []
    js_declarations = []
    skipped_files = []
    
    for cdn in cdns:
        # Extract the URL from <link> or <script> tags
        if 'href="' in cdn:  # CSS link
            url = cdn.split('href="')[1].split('"')[0]
            filename = download_file(url, css_folder)
            if filename:
                css_declarations.append(f'<link rel="stylesheet" href="{{{{ asset(\'{css_folder}/{filename}\') }}}}">')
            else:
                skipped_files.append(url)
        elif 'src="' in cdn:  # JavaScript link
            url = cdn.split('src="')[1].split('"')[0]
            filename = download_file(url, js_folder)
            if filename:
                js_declarations.append(f'<script src="{{{{ asset(\'{js_folder}/{filename}\') }}}}"></script>')
            else:
                skipped_files.append(url)

    # Display the new declarations in the output text box
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, "CSS Declarations:\n" + "\n".join(css_declarations) + "\n\n")
    output_text.insert(tk.END, "JavaScript Declarations:\n" + "\n".join(js_declarations) + "\n\n")
    
    # Show skipped files if any
    if skipped_files:
        output_text.insert(tk.END, "Skipped Files (Already Downloaded):\n" + "\n".join(skipped_files) + "\n")

    # Show success message
    messagebox.showinfo("Process Complete", "CDNs have been processed and files downloaded.")

# Function to clear input and output fields
def reset_fields():
    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)

# Set up GUI window
root = tk.Tk()
root.title("CDN Downloader")
root.geometry("700x600")

# Folder paths input
folder_label = tk.Label(root, text="Set Folder Paths:")
folder_label.pack(pady=5)

js_folder_label = tk.Label(root, text="JavaScript Folder:")
js_folder_label.pack()
js_folder_entry = tk.Entry(root, width=80)
js_folder_entry.insert(0, default_js_folder)  # Default value
js_folder_entry.pack(padx=10, pady=5)

css_folder_label = tk.Label(root, text="CSS Folder:")
css_folder_label.pack()
css_folder_entry = tk.Entry(root, width=80)
css_folder_entry.insert(0, default_css_folder)  # Default value
css_folder_entry.pack(padx=10, pady=5)

# Input text box for CDN links with example CDN links
input_label = tk.Label(root, text="Enter CDN Links:")
input_label.pack(pady=5)
input_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=10)
input_text.insert(tk.END, """<link href="https://example.com/styles.css" rel="stylesheet">
<script src="https://example.com/script.js"></script>""")  # Example CDN links
input_text.pack(padx=10, pady=5)

# Process button
process_button = tk.Button(root, text="Process CDNs", command=process_cdns)
process_button.pack(pady=10)

# Reset button
reset_button = tk.Button(root, text="Clear", command=reset_fields)
reset_button.pack(pady=5)

# Output text box for generated declarations and skipped files
output_label = tk.Label(root, text="Generated Local Declarations:")
output_label.pack(pady=5)
output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=10)
output_text.pack(padx=10, pady=5)

root.mainloop()
