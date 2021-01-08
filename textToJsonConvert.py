import json 
  
  
# the file to be converted to  
# json format 
filename = 'skills.txt'
  
# dictionary where the lines from 
# text will be stored 
dict1 = {} 
  
# creating dictionary 
with open(filename) as fh: 
    i = 1
    for line in fh:
        dict1[i] = line.rstrip()
        i=i+1
# creating json file 
# the JSON file is named as test1 
out_file = open("skillsets.json", "w") 
json.dump(dict1, out_file)
out_file.close()
