import json

data = {}
names = 'people'
name = 'name'
dataa = ["test","testtes"]
data[names] = []

data[names].append({
    name: dataa
})

print(type(data))
with open('./testCode/json/data.json', 'w') as outfile:
    json.dump(data, outfile)



# import json

# person_string = '{"name": "Bob", "languages": "English", "numbers": [2, 1.6, null]}'
# person_dict = json.loads(person_string)
# print(json.dumps(person_dict, indent = 4, sort_keys=True))