import os
import json

# Create dictionary
with open("info.json", "r") as file:
    values = json.load(file)

# To get and update people's info
class Directory:
    def __init__(self, id):

        # The ID taken from the arg "ID". Used as the dictionary key in info.json
        self.id = id

        # Create user dictionary
        self.user_dict = {}

    # Add basic values to to the dictionary
    def create(self):

        with open("info.json", "r") as file:
            values = json.load(file)
        
        self.user_dict = {
            "name": "N/A",
            "address": "N/A",
            "age": "N/A",
            "grade": "N/A",
            "birthday": "N/A",
            "school": "N/A",
            "color": 0,
            "email": "N/A",
            "ice cream": "N/A",
            "about": "N/A"
        }
        values[str(self.id)] = self.user_dict

        with open("info.json", "w+") as i:
            json.dump(values, i)

    # Edit values for the dictionary
    def edit(self, dict_key, dict_value):
 
        with open("info.json", "r") as file:
            values = json.load(file)

        user = str(self.id)
        values[user][dict_key] = dict_value

        with open("info.json", "w+") as i:
            json.dump(values, i)
