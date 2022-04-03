# Python program to read
# json file


import json

# Opening JSON file
f = open('data.json')

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
for i in data:
    print(i[1])
# print(data[0])

file_object  = open("filename", "mode")

# Closing file
f.close()
