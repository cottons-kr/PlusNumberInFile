import sys, os, re

linelist = []
numlist = []
num = 0
target = sys.argv[1]

def sumnum(list):
	templist = []
	for i in list:
		i = int(i)
		templist.append(i)
	return sum(templist)

if os.path.isfile(target):
	with open(target, 'r') as file:
		file = file.readlines()
		for string in file:
			if '\n' in string:
				string = string.rstrip('\n')
			linelist.append(string)
	for data in linelist:
		numlist.extend(re.findall('\d+', data))
	num = sumnum(numlist)
	print(num)
	with open('result.txt', 'w') as result:
		result.write(str(num))
else:
	print('없는 파일입니다')
