#Add files based on twitter ids
# Input postsSeperateIds.txt and post_features.txt, user_features.txt
# Output combined file 

import json

data  = []
d = {}
with open('postsSepIds.json','r') as f:
	for line in f:
		data.append(json.loads(line))
with open('post_features.txt','r') as p:
	postF =[x.strip().split(',') for x in p]
	
for row in postF:
	d[row[0]] = (row[1:])


with open('post_postFeaturesCombined.json', 'w') as f:
	for row in data:
		if row[0] in d:
			json.dump(row + d[row[0]], f)
			f.write('\n')

