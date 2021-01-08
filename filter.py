# import json module for parsing
import json

filtering = []
# define a list of keywords
with open('out.json') as out_json:
    words = json.load(out_json)
    for num, toBeFiltered in words[0].items():
        continue
with open('skillsets.json') as skills_json:
    skills = json.load(skills_json)
    for p in skills.values():
        if (toBeFiltered.lower().find(p.lower()) != -1):
            filtering.append(p)
filtered = list(dict.fromkeys(filtering))
# dictionary where the lines from 
# text will be stored 
dict1 = {} 
# creating dictionary
i = 1
for item in filtered:
    dict1[i] = item.rstrip()
    i=i+1
# creating json file 
# the JSON file is named as test1 
out_file = open("filtered.json", "w") 
json.dump(dict1, out_file)
out_file.close()
