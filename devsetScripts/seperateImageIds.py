#File to seperate comma seperated values in 3rd column to two seperate lines

import json

posts = []
post1 = []
post2 = []
j = 1
with open('../posts.txt','r') as f:
	LoL=[x.strip().split('\t') for x in f]
for i in range(1, len(LoL)):
#for i in range(1, 2):
	if "," in LoL[i][3]:
		imageId = [image for image in LoL[i][3].split(',')]
		del LoL[i][3]
		post1 = LoL[i][:]
		post2 = LoL[i][:]
		post1.insert(3,imageId[0])
		post1.append(0) #not duplicate
		post2.insert(3,imageId[1])
		post2.append(1) #duplicate
		posts.append(post1)
		posts.append(post2)
	else:
		LoL[i].append(0)  #not duplicate
		posts.append(LoL[i][:])
with open('postsSepIds.txt', 'a') as outfile:
	for item in posts:
		json.dump(item, outfile)
		outfile.write('\n')

#print posts
		

