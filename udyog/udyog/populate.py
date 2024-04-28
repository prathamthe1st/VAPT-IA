# import sqlite3
# import json

# conn = sqlite3.connect('example.db')
# with open('example.json', 'r') as json_file:
#     data = json.load(json_file)
#     for item in data:
#         conn.execute("INSERT INTO example_table (field1, field2, field3) VALUES (?, ?, ?)", (item["field1"], item["field2"], item["field3"]))
# conn.commit()
# conn.close()

import sqlite3
import json

# Connect to the SQLite database
conn = sqlite3.connect('udyog\db.sqlite3')

# Open and load the JSON data
# with open('udyog\candidates.json', 'r') as json_file:
#     data = json.load(json_file)

# # Iterate over each item in the data
# for item in data:
#     # Prepare the data for insertion
#     fields = item['fields']
#     # Assuming the table structure matches the JSON structure
#     conn.execute("INSERT INTO candidates_profile (full_name, country, location, resume, grad_year, looking_for, gender, slug) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (fields['full_name'], fields['country'], fields['location'], fields['resume'], fields['grad_year'], fields['looking_for'], fields['gender'], fields['slug']))

with open('udyog/auth.user.json', 'r') as json_file:
    data = json.load(json_file)

    # Iterate over each item in the data
    for item in data:
        # Prepare the data for insertion
        fields = item['fields']
        # Assuming the table structure matches the JSON structure
        conn.execute("INSERT INTO auth_user (password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (fields['password'], fields['last_login'], fields['is_superuser'], fields['username'], fields['first_name'], fields['last_name'], fields['email'], fields['is_staff'], fields['is_active'], fields['date_joined']))



# Commit the changes and close the connection
conn.commit()
conn.close()
