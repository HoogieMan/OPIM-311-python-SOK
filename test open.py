daFile = open('test.txt','r')
lines = daFile.readlines()
for line in lines:
	print(line)
daFile.close()


