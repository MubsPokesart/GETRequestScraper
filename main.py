import random
from urllib import request

naturelist = ['Adamant', 'Bashful', 'Bold', 'Brave', 'Calm Nature', 'Careful', 'Docile', 'Gentle', 'Hardy', 'Hasty', 'Impish', 'Jolly', 'Lax', 'Lonely', 'Mild', 'Modest', 'Naive', 'Naughty', 'Quiet', 'Quirky', 'Rash', 'Relaxed', 'Sassy', 'Serious', 'Timid']
spantypeexport = ['<span class="type-normal">', '<span class="type-fire">', '<span class="type-water">', '<span class="type-grass">', '<span class="type-electric">', '<span class="type-ice">', '<span class="type-fighting">', '<span class="type-poison">', '<span class="type-ground">', '<span class="type-flying">', '<span class="type-psychic">', '<span class="type-bug">', '<span class="type-rock">', '<span class="type-ghost">', '<span class="type-dark">', '<span class="type-dragon">', '<span class="type-steel">', '<span class="type-fairy">']
spanstatexport = ['<span class="stat-hp">' , '<span class="stat-atk">', '<span class="stat-def">', '<span class="stat-spa">', '<span class="stat-spd">', '<span class="stat-spe">', '<span class="gender-m">', '<span class="gender-f">']

MonFormat = input('What format are you creating these for? ')

pastelist = []
monlist = []

importfile = open('import.txt', 'r')
importline = importfile.readline()
while (importline): 
	importlen = len(importline)
	if (importline.find('pokepast') > -1):
		if (importline.find('\n') > -1):
			importvar = importlen - 1
			importreplace = str(importline[:importvar])
			pastelist.append(importreplace)
			importline = importfile.readline()
		else:
			pastelist.append(importline)
			importline = importfile.readline()
	else:
		print("Error")
		importline = importfile.readline()
importfile.close()

for index in range (len(pastelist)):
	monlist.append('\n=== [' + MonFormat +  '] Titled ' + str(random.randint(0, 10000)) + ' ===\n')
	resp = request.urlopen(pastelist[index])
	data = resp.read()
	html = data.decode("UTF-8")
	resp.close()

	inFile = open('html.txt', 'w')
	inFile.write(html)
	inFile.close()

	htmllist = []
	htmlfile = open('html.txt', 'r')
	htmlline = htmlfile.readline()
	while (htmlline):
		htmllen = len(htmlline)
		if (htmlline.find('\n') > -1):
			htmlvar = htmllen - 1
			htmlreplace = str(htmlline[:htmlvar])
			htmllist.append(htmlreplace)
		else:
			htmllist.append(htmlline)
		htmlline = htmlfile.readline()
	htmlfile.close()

	htmllistlen = len(htmllist)
	htmlcounter = 0
	teamlist = []
	fullline = ""
	while (htmlcounter < htmllistlen):
		countline = htmllist[htmlcounter]
		if (countline.find('<pre>') > -1):
			counttext = ""
			while (countline.find('</pre>') == -1 and htmlcounter < htmllistlen):
				counttext = counttext + countline
				htmlcounter = htmlcounter + 1
				countline = htmllist[htmlcounter]
			counttext = counttext.replace('</span>', '')
			for item in spantypeexport:
				if (counttext.find(item) > -1):
					counttext = counttext.replace(item, '')
			for item in spanstatexport:
				if (counttext.find(item) > -1):
					counttext = counttext.replace(item, '')
			for item in naturelist:
				if (counttext.find(item) > -1):
					counttext = counttext.replace(item, '\n' + item)
			counttext = counttext.replace('- ',  '\n- ')
			counttext = counttext.replace('&#39;', "'")
			counttext = counttext.replace('<span class="attr">', '\n')
			counttext = counttext.replace('<pre>', '\n\n')
			fullline = fullline + counttext
		else:
			htmlcounter = htmlcounter + 1
	monlist.append(fullline + '\n')


resultfile = open('result.txt', 'w')
for item in monlist:
	resultfile.write(item)
resultfile.close()

print("Done")