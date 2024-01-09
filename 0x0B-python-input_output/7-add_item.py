#!/usr/bin/python3
"""Module: add_items_to_list
Script that adds all command-line arguments to a Python list and saves them to a JSON file.
"""

import json
import sys
import os.path

# Importing functions from other modules
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

new_file = "add_item.json"
new_list = []

# Load existing data from the JSON file if it exists and is not empty
if os.path.exists(new_file) and os.path.getsize(new_file) > 0:
    new_list = load_from_json_file(new_file)

# Add command-line arguments to the list
if len(sys.argv) > 1:
    for elem in sys.argv[1:]:
        new_list.append(elem)

# Save the updated list to the JSON file
save_to_json_file(new_list, new_file)

