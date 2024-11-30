import json
f=open('intrebari.json')
data=json.load(f)
for i in data['quiz']:
 for j in i['answers']:
    print(j)

