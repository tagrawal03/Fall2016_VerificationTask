#Add files based on twitter ids
# Input postsSeperateIds.txt and post_features.txt, user_features.txt
# Output combined file 

import json

data  = []
d = {}
with open('postUserCombined.json','r') as f:
	for line in f:
		data.append(json.loads(line))
fake = ["Image_fake"]
real = ["Image_real"]
NotKnown = ["N.A"]
	
with open('WithImageLabel.json', 'w') as f:
	for row in data:
		if 'fake' in row[3] or 'passport_02' in row[3] or 'passport_01' in row[3] or 'livr_01' in row[3] or 'livr_02' in row[3] or 'livr_03' in row[3] or 'livr_04' in row[3] or 'pigFish_01' in row[3] :
			json.dump(row + fake, f)
			f.write('\n')
		elif 'real' in row[3]:
			json.dump(row + real, f)
			f.write('\n')
		else:
			json.dump(row + NotKnown, f)
			f.write('\n')
			print row[3]
			

