import json

x = {
    "logins": [
    {"user": "admin", "pass": "password"},
    {"user": "admin", "pass": "Password"}
    ]
}

# json_object = json.dumps(x, indent = 2)
# with open("logins.json", "w") as outfile:
#     outfile.write(json_object)

f = open('logins.json')
data = json.load(f)

print(data['frontier'])